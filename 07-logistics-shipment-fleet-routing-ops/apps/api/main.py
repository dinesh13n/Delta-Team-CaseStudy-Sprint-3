"""Logistics: Shipment, Fleet, Routing & Exception Operations API (target contract: data/contracts/openapi.yaml)."""

from __future__ import annotations

import json
import logging
import re
import secrets
import time
from collections import defaultdict, deque
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from fastapi import Depends, FastAPI, Query, Request, Response
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from apps.api import correlation, kpis
from apps.api.ai import registry
from apps.api.ai.gateway import AiGateway, NotFoundError
from apps.api.ai.providers import DeterministicProvider, UnconfiguredModelProvider
from apps.api.ai.sanitize import load_enums
from apps.api.approvals import AlreadyDecidedError, ApprovalStore
from apps.api.audit_chain import AuditSink, JsonlAuditSink, build_event
from apps.api.config import ROOT, Settings, load_settings
from apps.api.data.repository import CsvRepository, DataRepository, load_entities
from apps.api.errors import ApiError, install, problem
from apps.api.metrics import Metrics
from apps.api.resilience import CircuitBreaker
from apps.api.security.policy import Decision, PolicyEngine
from apps.api.security.tokens import Claims, Hs256Verifier, JwksVerifier, TokenError, TokenVerifier

log = logging.getLogger("api")
PLATFORM_ROLES = {"ops": "metrics", "auditor": "audit_verify"}  # [ASM] not in access-semantics; see D-012
STATUS_FLAG_ENTITY = "shipments"


class DecisionBody(BaseModel):
    decision: str = Field(pattern="^(approve|reject)$")
    reason: str | None = Field(default=None, max_length=500)


class Services:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.policy = PolicyEngine.from_dir(settings.semantic_dir)
        self.entities = load_entities(settings.semantic_dir)
        self.repo: DataRepository = CsvRepository(settings.data_dir, settings.data_layer, self.entities)
        secret = settings.auth_secret or secrets.token_urlsafe(48)  # ephemeral in local mode only
        self.ephemeral_secret = settings.auth_secret is None
        self.secret = secret
        self.verifier: TokenVerifier = JwksVerifier() if settings.auth_mode == "jwks" else Hs256Verifier(secret)
        self.audit: AuditSink = JsonlAuditSink(settings.audit_path)
        self.approvals = ApprovalStore(settings.approvals_path)
        provider = DeterministicProvider() if settings.ai_provider == "deterministic" else UnconfiguredModelProvider()
        registry.verify_model(provider.name, provider.version)  # P-X3: an unlisted model cannot be put into service
        self.gateway = AiGateway(
            self.repo,
            self.policy.ai_policy,
            provider,
            enums=load_enums(settings.semantic_dir),
            breaker=CircuitBreaker(settings.ai_breaker_threshold, settings.ai_breaker_reset_s),
            timeout_s=settings.ai_timeout_s,
        )
        self.metrics = Metrics()
        self._load: tuple[float, str] = (-1.0, "unknown")
        self.ai_calls: dict[str, deque[float]] = defaultdict(deque)

    def data_load_id(self) -> str:
        """Identity of the ETL load being served (M3 drill 4): lets a reader tie a response to a data version."""
        path = self.settings.data_dir / "reports" / "latest.json"
        try:
            mtime = path.stat().st_mtime
            if mtime != self._load[0]:
                self._load = (mtime, str(json.loads(path.read_text(encoding="utf-8")).get("load_id", "unknown")))
        except (OSError, ValueError):
            return "unknown"
        return self._load[1]


MAX_BODY_BYTES = 64 * 1024


def data_age_seconds(data_dir: Path) -> float:
    """Seconds since the last published ETL run, or -1 when no readable report exists."""
    try:
        run_id = json.loads((data_dir / "reports" / "latest.json").read_text(encoding="utf-8"))["run_id"]
        ran = datetime.strptime(run_id, "run-%Y%m%dT%H%M%SZ").replace(tzinfo=UTC)
    except (OSError, ValueError, KeyError):
        return -1.0
    return max(0.0, (datetime.now(UTC) - ran).total_seconds())


def data_is_fresh(data_dir: Path, max_age_s: float) -> bool:
    """True when the last published ETL report is not older than max_age_s; no readable report means freshness cannot be shown."""
    age = data_age_seconds(data_dir)
    return age >= 0 and age <= max_age_s


def create_app(settings: Settings | None = None) -> FastAPI:
    st = settings or load_settings()
    svc = Services(st)
    app = FastAPI(
        title="Logistics: Shipment, Fleet, Routing & Exception Operations",
        version="1.1.0",
        # M1 hardening: interactive docs and the schema are a local convenience, not a production surface
        docs_url="/docs" if st.is_local else None,
        redoc_url="/redoc" if st.is_local else None,
        openapi_url="/openapi.json" if st.is_local else None,
    )
    app.state.svc = svc
    # N1: a counter that does not exist until its first event makes increase()/rate() alerts miss that first event, so the
    # security- and safety-relevant series are created at zero.
    svc.metrics.inc("ai_guardrail_blocked_total", 0.0)
    fallback_reasons = (
        "output_policy_violation",
        "invalid_output",
        "circuit_open",
        "provider_timeout",
        "provider_unavailable",
        "provider_error",
    )
    for reason in fallback_reasons:
        svc.metrics.inc("ai_fallback_total", 0.0, labels={"reason": reason})
    for decision in ("approve", "reject"):
        svc.metrics.inc("ai_decisions_total", 0.0, labels={"decision": decision})
    install(app)
    web_dir = ROOT / "apps" / "web" / "public"
    if (
        web_dir.is_dir()
    ):  # thin read-only operations view (OQ-06 ruling); static shell only, data comes from the authenticated API
        app.mount("/ops", StaticFiles(directory=web_dir, html=True), name="ops")

    @app.middleware("http")
    async def observe(request: Request, call_next: Any) -> Response:
        cid = correlation.accept_or_generate(request.headers.get(correlation.HEADER))
        correlation.set_current(cid)
        request.state.cid = cid
        t0 = time.perf_counter()
        try:
            declared = request.headers.get("content-length", "0")
            if (
                declared.isdigit() and int(declared) > MAX_BODY_BYTES
            ):  # security-spec item 6 (chunked bodies are not covered here)
                response: Response = problem(413, "Payload too large", f"request body exceeds {MAX_BODY_BYTES} bytes")
            else:
                response = await call_next(request)
        except Exception:
            response = problem(500, "Internal error", "unexpected error")
        dt = time.perf_counter() - t0
        route = request.scope.get("route")
        path = getattr(route, "path", "unmatched")
        response.headers[correlation.HEADER] = cid
        response.headers["X-Data-Load-Id"] = svc.data_load_id()
        if not request.url.path.startswith("/ops"):  # M1: API responses are data; never cache or sniff them
            response.headers.setdefault("Cache-Control", "no-store")
            response.headers.setdefault("X-Content-Type-Options", "nosniff")
        if request.url.path.startswith("/ops"):
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; "
                "frame-ancestors 'none'; base-uri 'none'; form-action 'none'"
            )
            response.headers["X-Content-Type-Options"] = "nosniff"
            response.headers["Referrer-Policy"] = "no-referrer"
        svc.metrics.inc("http_requests_total", labels={"route": path, "status": str(response.status_code)})
        svc.metrics.observe("http_request_duration_seconds", dt, labels={"route": path})
        log.info(
            json.dumps(
                {
                    "ts": time.time(),
                    "level": "info",
                    "correlation_id": cid,
                    "method": request.method,
                    "route": path,
                    "status": response.status_code,
                    "latency_ms": round(dt * 1000, 1),
                    "actor_role": getattr(getattr(request.state, "claims", None), "role", "none"),
                    "data_load_id": svc.data_load_id(),
                }
            )
        )
        return response

    def audit(
        request: Request, claims: Claims | None, action: str, rtype: str, rid: str, d: Decision | None, outcome: str, **kw: Any
    ) -> dict[str, Any]:
        ev = build_event(
            action=action,
            subject=claims.subject if claims else "anonymous",
            role=claims.role if claims else "none",
            correlation_id=request.state.cid,
            tenant=claims.tenant if claims else st.tenant,
            resource_type=rtype,
            resource_id=rid,
            decision=("allow" if (d is None or d.allow) else "deny"),
            rule=d.rule if d else "n/a",
            decision_id=d.decision_id if d else None,
            outcome=outcome,
            auth_method=("jwt" if claims and st.auth_mode != "legacy_header" else ("service" if claims else "anonymous")),
            **kw,
        )
        return svc.audit.append(ev)

    def current_claims(request: Request) -> Claims:
        if st.auth_mode == "legacy_header":  # FF-01, local only (F-17 is the reason this is not the default)
            role = request.headers.get("X-User-Role", "operator")
            return Claims(subject="legacy-header", role=role, tenant=st.tenant)
        header = request.headers.get("Authorization", "")
        m = re.fullmatch(r"Bearer\s+(\S+)", header)
        try:
            if not m:
                raise TokenError("MissingBearer")
            claims = svc.verifier.verify(m.group(1))
        except TokenError as exc:
            svc.metrics.inc("auth_denied_total", labels={"reason": re.sub(r"[^A-Za-z0-9_]", "", str(exc))[:40] or "unknown"})
            audit(request, None, "auth.denied", "token", "n/a", None, "denied", detail={"reason": str(exc)})
            raise ApiError(
                401, "Unauthorized", "missing or invalid bearer token", headers={"WWW-Authenticate": "Bearer"}
            ) from exc
        request.state.claims = claims
        return claims

    def authorize(request: Request, claims: Claims, entity: str, action: str, audit_action: str, rid: str) -> Decision:
        d = svc.policy.decide(claims.role, entity, action, claims.purpose)
        if not d.allow:
            svc.metrics.inc("policy_denied_total", labels={"entity": entity})
            audit(request, claims, audit_action + ".denied", entity, rid, d, "denied", detail={"reason": d.reason})
            raise ApiError(403, "Forbidden", "policy denied the request", policy_decision_id=d.decision_id)
        return d

    def check_key(entity: str, key: str) -> None:
        if not svc.entities[entity].key_pattern.fullmatch(key):
            raise ApiError(422, "Validation error", "identifier does not match the key pattern for this entity")

    def platform_role(claims: Claims, request: Request, needed: str) -> None:
        if PLATFORM_ROLES.get(claims.role) != needed:
            audit(request, claims, f"{needed}.denied", "platform", needed, None, "denied")
            raise ApiError(403, "Forbidden", "role is not allowed for this endpoint")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "repo": "07-logistics-shipment-fleet-routing-ops"}

    @app.get("/ready")
    def ready() -> Response:
        checks = {f"data:{k}": v for k, v in svc.repo.ready().items()}
        checks["auth_configured"] = bool(st.auth_secret) or st.is_local
        if st.data_max_age_s > 0:
            checks["data_fresh"] = data_is_fresh(st.data_dir, st.data_max_age_s)
        try:
            st.audit_path.parent.mkdir(parents=True, exist_ok=True)
            checks["audit_writable"] = st.audit_path.parent.is_dir()
        except OSError:
            checks["audit_writable"] = False
        if all(checks.values()):
            return Response(json.dumps({"status": "ready", "checks": checks}), media_type="application/json")
        return problem(503, "Not ready", "failing: " + ", ".join(k for k, v in checks.items() if not v))

    @app.get("/metrics", response_class=PlainTextResponse)
    def metrics(request: Request, claims: Claims = Depends(current_claims)) -> str:
        platform_role(claims, request, "metrics")
        svc.metrics.set_gauge("audit_chain_valid", 1.0 if svc.audit.verify()["valid"] else 0.0)
        svc.metrics.set_gauge("data_load_age_seconds", data_age_seconds(st.data_dir))
        breaker = svc.gateway.breaker
        svc.metrics.set_gauge("ai_circuit_open", 1.0 if breaker is not None and breaker.state != "closed" else 0.0)
        return svc.metrics.render()

    @app.get("/shipments")
    def list_shipments(
        request: Request,
        limit: int = Query(20, ge=1, le=100),
        offset: int = Query(0, ge=0),
        status: str | None = Query(None, max_length=40),
        claims: Claims = Depends(current_claims),
    ) -> dict[str, Any]:
        d = authorize(request, claims, "shipments", "read", "shipment.list", "list")
        items, total = svc.repo.list_page("shipments", limit, offset, status)
        audit(request, claims, "shipment.list", "shipments", "list", d, "success")
        return {
            "items": [svc.policy.filter_row(claims.role, "shipments", r) for r in items],
            "total": total,
            "limit": limit,
            "offset": offset,
        }

    @app.get("/shipments/{shipment_id}/events")
    def shipment_events(shipment_id: str, request: Request, claims: Claims = Depends(current_claims)) -> list[dict[str, Any]]:
        check_key("shipments", shipment_id)
        d = authorize(request, claims, "tracking_events", "read", "event.list", shipment_id)
        if svc.repo.get("shipments", shipment_id) is None:
            raise ApiError(404, "Not found", "no such shipment")
        audit(request, claims, "event.list", "shipment", shipment_id, d, "success")
        return [svc.policy.filter_row(claims.role, "tracking_events", e) for e in svc.repo.events_for(shipment_id)]

    @app.get("/records/{record_id}")
    def get_record(record_id: str, request: Request, claims: Claims = Depends(current_claims)) -> dict[str, Any]:
        if st.lookup_mode == "legacy":  # FF-02, local only
            from apps.api.services import domain_service

            legacy: dict[str, Any] = domain_service.load_record(record_id)
            return legacy
        check_key("shipments", record_id)
        d = authorize(request, claims, "shipments", "read", "record.read", record_id)
        row = svc.repo.get("shipments", record_id)
        if row is None:
            audit(request, claims, "record.read", "shipment", record_id, d, "error", detail={"reason": "not_found"})
            raise ApiError(404, "Not found", "no such record")
        audit(request, claims, "record.read", "shipment", record_id, d, "success")
        return svc.policy.filter_row(claims.role, "shipments", row)

    def rate_limited(subject: str) -> bool:
        q, now = svc.ai_calls[subject], time.monotonic()
        while q and now - q[0] > 60:
            q.popleft()
        if len(q) >= st.ai_rate_per_minute:
            return True
        q.append(now)
        return False

    @app.post("/ai/summarize/{record_id}")
    def ai_summary(record_id: str, request: Request, claims: Claims = Depends(current_claims)) -> dict[str, Any]:
        check_key("shipments", record_id)
        d = authorize(request, claims, "shipments", "read", "ai.summary", record_id)
        if not st.ai_enabled:
            raise ApiError(503, "AI disabled", "the AI endpoint is switched off")
        if rate_limited(claims.subject):
            audit(request, claims, "ai.summary.rate_limited", "shipment", record_id, d, "denied")
            raise ApiError(429, "Too many requests", "AI rate limit exceeded", headers={"Retry-After": "60"})
        ai = svc.policy.decide("ai_agent", "shipments", "read", "exception_summary")
        if not ai.allow:
            raise ApiError(503, "AI unavailable", "AI persona is not permitted by policy")
        t_ai = time.perf_counter()
        try:
            res = svc.gateway.summarize(record_id, request.state.cid)
        except NotFoundError as exc:
            audit(request, claims, "ai.summary", "shipment", record_id, d, "error", detail={"reason": "not_found"})
            raise ApiError(404, "Not found", "no such record") from exc
        out = res.output
        ai_seconds = time.perf_counter() - t_ai
        svc.metrics.observe("ai_request_duration_seconds", ai_seconds, labels={"generated_by": str(out["generated_by"])})
        svc.approvals.register(out["summary_id"], record_id, claims.subject, request.state.cid)
        svc.metrics.inc(
            "ai_requests_total", labels={"generated_by": out["generated_by"], "abstained": str(out["abstained"]).lower()}
        )
        svc.metrics.inc("ai_tokens_total", float(out["token_estimate"]))
        if out["generated_by"] == "fallback":
            svc.metrics.inc("ai_fallback_total", labels={"reason": str(out["fallback_reason"])})
        if out["guardrail_status"] == "blocked":
            svc.metrics.inc("ai_guardrail_blocked_total")
        audit(
            request,
            claims,
            "ai.summary",
            "shipment",
            record_id,
            d,
            "success",
            model=res.model,
            input_hash=res.input_hash,
            retention_class="ai_trace",
            detail={
                "summary_id": out["summary_id"],
                "abstained": out["abstained"],
                "signals": sorted(set(res.signals)),
                "token_source": out["token_source"],
                # M4 tabletop / N2: an investigator must be able to tell from the audit alone what the AI did and from which data
                "generated_by": out["generated_by"],
                "fallback_reason": out["fallback_reason"],
                "guardrail_status": out["guardrail_status"],
                "prompt_version": out["prompt_version"],
                "data_load_id": svc.data_load_id(),
                "latency_ms": round(ai_seconds * 1000, 1),
            },
        )
        return out

    @app.post("/ai/summaries/{summary_id}/decision")
    def decide(summary_id: str, body: DecisionBody, request: Request, claims: Claims = Depends(current_claims)) -> dict[str, Any]:
        d = authorize(request, claims, "shipments", "write", "ai.decision", summary_id)
        if not svc.approvals.known(summary_id):
            raise ApiError(404, "Not found", "no such suggestion")
        try:
            rec = svc.approvals.decide(summary_id, body.decision, claims.subject, body.reason)
        except AlreadyDecidedError as exc:
            raise ApiError(409, "Conflict", "suggestion already decided") from exc
        svc.metrics.inc("ai_decisions_total", labels={"decision": body.decision})
        audit(
            request,
            claims,
            "ai.decision",
            "ai_summary",
            summary_id,
            d,
            "success",
            approval_id=rec["approval_id"],
            detail={"decision": body.decision},
        )
        return {k: rec[k] for k in ("approval_id", "summary_id", "decision", "decided_by", "decided_at")}

    @app.get("/audit/verify")
    def audit_verify(request: Request, claims: Claims = Depends(current_claims)) -> dict[str, Any]:
        platform_role(claims, request, "audit_verify")
        return svc.audit.verify()

    @app.get("/kpis")
    def get_kpis(request: Request, claims: Claims = Depends(current_claims)) -> dict[str, Any]:
        d = authorize(request, claims, "shipments", "read", "kpi.read", "kpis")
        audit(request, claims, "kpi.read", "kpis", "K1-K10", d, "success")
        from apps.api.audit_chain import utc_now

        return {"as_of": utc_now(), "kpis": kpis.compute(st.data_dir, st.data_layer)}

    return app


app = create_app()
