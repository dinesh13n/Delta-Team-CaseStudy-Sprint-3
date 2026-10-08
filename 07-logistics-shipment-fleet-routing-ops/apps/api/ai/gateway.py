"""AI gateway (ADR-0007; F-22..F-29): allow-listed context, safe prompt, schema-validated output,
abstention, deterministic fallback. Suggest-only: nothing here executes an action."""

from __future__ import annotations

import json
import math
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import jsonschema

from apps.api.ai import registry
from apps.api.ai.providers import (
    DeterministicProvider,
    ModelProvider,
    PromptParts,
    ProviderUnavailable,
)
from apps.api.ai.sanitize import ENUM_FIELDS, clean_enum, clean_value
from apps.api.audit_chain import canonical, sha256_hex
from apps.api.data.repository import DataRepository
from apps.api.resilience import CallTimeoutError, CircuitBreaker, CircuitOpenError, guarded

SCHEMA_PATH = Path(__file__).resolve().parents[3] / "data" / "contracts" / "schemas" / "ai-summary-output.schema.json"
MAX_EVENTS = 10
CHARS_PER_TOKEN = 4


class NotFoundError(Exception):
    pass


@dataclass
class GatewayResult:
    output: dict[str, Any]
    input_hash: str
    model: dict[str, Any]
    signals: list[str] = field(default_factory=list)


def _allowed(policy: dict[str, Any], entity: str) -> list[str]:
    return list((policy.get("allowed_fields") or {}).get(entity, []))


def _pick(
    row: dict[str, Any], fields: list[str], signals: list[str], entity: str = "", enums: dict[str, set[str]] | None = None
) -> dict[str, Any]:
    enum_map = ENUM_FIELDS.get(entity, {})
    out: dict[str, Any] = {}
    for f in fields:
        if f not in row:
            continue
        if f in enum_map and enums is not None:
            out[f] = clean_enum(row.get(f), enums.get(enum_map[f]), signals)
        else:
            out[f] = clean_value(row.get(f), signals)
    return out


class AiGateway:
    def __init__(
        self,
        repo: DataRepository,
        ai_policy: dict[str, Any],
        provider: ModelProvider,
        fallback: ModelProvider | None = None,
        schema_path: Path = SCHEMA_PATH,
        enums: dict[str, set[str]] | None = None,
        breaker: CircuitBreaker | None = None,
        timeout_s: float | None = None,
    ) -> None:
        self.enums = enums
        self.breaker, self.timeout_s = breaker, timeout_s
        self.repo, self.policy = repo, ai_policy
        self.provider = provider
        self.fallback: ModelProvider = fallback or DeterministicProvider()
        self.schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.prompt = registry.load()
        self.max_record_tokens = int(ai_policy.get("max_record_tokens", 2000))
        jsonschema.Draft202012Validator.check_schema(self.schema)

    # ---- context ---------------------------------------------------------------------------
    def build_context(self, shipment_id: str) -> tuple[dict[str, Any], list[dict[str, str]], list[str]]:
        facts, sources, signals, _ = self._ctx(shipment_id)
        return facts, sources, signals

    def _forbidden_values(self, ship: dict[str, Any], events: list[dict[str, Any]]) -> list[str]:
        """Values of ai-context-policy forbidden_fields present in this record; they must never appear in an output."""
        rows = {"shipments": [ship], "tracking_events": events}
        vals: set[str] = set()
        for spec in self.policy.get("forbidden_fields", []):
            entity, _, fld = str(spec).partition(".")
            for r in rows.get(entity, []):
                v = r.get(fld)
                if isinstance(v, str) and len(v) >= 3:
                    vals.add(v.lower())
        return sorted(vals)

    def _ctx(self, shipment_id: str) -> tuple[dict[str, Any], list[dict[str, str]], list[str], list[str]]:
        ship = self.repo.get("shipments", shipment_id)
        if ship is None:
            raise NotFoundError(shipment_id)
        signals: list[str] = []
        events = sorted(self.repo.events_for(shipment_id), key=lambda e: str(e.get("event_time")))
        keep = events[-MAX_EVENTS:] + [e for e in events[:-MAX_EVENTS] if e.get("event_type") == "exception"]
        bookings = self.repo.related("carrier_bookings", "shipment_id", shipment_id)
        facts: dict[str, Any] = {
            "shipment": _pick(ship, _allowed(self.policy, "shipments"), signals, "shipments", self.enums),
            "events": [_pick(e, _allowed(self.policy, "tracking_events"), signals, "tracking_events", self.enums) for e in keep],
            "event_total": len(events),
            "carrier_bookings": [_pick(b, _allowed(self.policy, "carrier_bookings"), signals) for b in bookings],
        }
        sources = [{"dataset": "shipments", "record_id": shipment_id}]
        sources += [{"dataset": "tracking_events", "record_id": str(e.get("event_id"))} for e in keep if e.get("event_id")]
        sources += [
            {"dataset": "carrier_bookings", "record_id": str(b.get("booking_id"))} for b in bookings if b.get("booking_id")
        ]
        return facts, sources, signals, self._forbidden_values(ship, events)

    def _fit_budget(self, facts: dict[str, Any]) -> tuple[PromptParts, int]:
        events = list(facts["events"])
        while True:
            parts = PromptParts(self.prompt.text, json.dumps({**facts, "events": events}, sort_keys=True))
            tokens = math.ceil(len(parts.render()) / CHARS_PER_TOKEN)
            if tokens <= self.max_record_tokens or not events:
                facts["events"] = events
                return parts, tokens
            events = events[1:]

    # ---- output ----------------------------------------------------------------------------
    def _wrap(
        self,
        core: dict[str, Any],
        *,
        provider: ModelProvider,
        generated_by: str,
        fallback_reason: str | None,
        sources: list[dict[str, str]],
        tokens: int,
        token_source: str,
        cfg: str,
        cid: str,
        guardrail: str,
    ) -> dict[str, Any]:
        abstained = bool(core.get("abstained"))
        return {
            "summary_id": "sum-" + uuid.uuid4().hex[:16],
            "model": provider.name,
            "model_version": provider.version,
            "prompt_version": self.prompt.prompt_version,
            "summary": None if abstained else core.get("summary"),
            "recommendation": None if abstained else core.get("recommendation"),
            "abstained": abstained,
            "abstain_reason": core.get("abstain_reason") if abstained else None,
            "guardrail_status": guardrail,
            "generated_by": generated_by,
            "fallback_reason": fallback_reason,
            "source_count": len(sources),
            "sources": sources,
            "token_estimate": tokens,
            "token_source": token_source,
            "confidence": core.get("confidence"),
            "requires_human_approval": True,
            "config_hash": cfg,
            "correlation_id": cid,
        }

    def _valid(self, out: dict[str, Any]) -> bool:
        return not list(jsonschema.Draft202012Validator(self.schema).iter_errors(out))

    def _abstain(
        self,
        reason: str,
        provider: ModelProvider,
        sources: list[dict[str, str]],
        tokens: int,
        cfg: str,
        cid: str,
        guardrail: str,
        fallback_reason: str | None,
    ) -> dict[str, Any]:
        core = {"abstained": True, "abstain_reason": reason}
        return self._wrap(
            core,
            provider=provider,
            generated_by="fallback" if fallback_reason else "deterministic",
            fallback_reason=fallback_reason,
            sources=sources,
            tokens=tokens,
            token_source="estimate",  # noqa: S106 (label, not a credential)
            cfg=cfg,
            cid=cid,
            guardrail=guardrail,
        )

    def _parse(self, text: str) -> dict[str, Any] | None:
        try:
            core = json.loads(text)
        except (json.JSONDecodeError, TypeError):
            return None
        if not isinstance(core, dict) or not isinstance(core.get("abstained"), bool):
            return None
        if not core["abstained"] and not (isinstance(core.get("summary"), str) and isinstance(core.get("recommendation"), str)):
            return None
        conf = core.get("confidence")
        if conf is not None and not (isinstance(conf, int | float) and 0 <= conf <= 1):
            return None
        return core

    @staticmethod
    def _leaks(core: dict[str, Any], forbidden: list[str]) -> bool:
        text = f"{core.get('summary') or ''} {core.get('recommendation') or ''}".lower()
        return any(v in text for v in forbidden)

    def summarize(self, shipment_id: str, correlation_id: str) -> GatewayResult:
        facts, sources, signals, forbidden = self._ctx(shipment_id)
        parts, tokens = self._fit_budget(facts)
        input_hash = sha256_hex(canonical(facts))
        cfg = registry.config_hash(self.prompt, self.provider.name, self.provider.version, self.max_record_tokens)
        used: ModelProvider = self.provider
        generated_by, fb_reason = ("deterministic" if isinstance(self.provider, DeterministicProvider) else "model"), None
        core: dict[str, Any] | None = None
        token_source, total_tokens = "estimate", tokens
        try:
            if isinstance(self.provider, DeterministicProvider):  # local and instant: no breaker or thread needed
                res = self.provider.complete(parts, facts)
            else:
                res = guarded(lambda: self.provider.complete(parts, facts), self.breaker, self.timeout_s)
            core = self._parse(res.text)
            if core is not None and self._leaks(core, forbidden):
                core, fb_reason = None, "output_policy_violation"
                signals.append("output_policy_violation")
            if res.prompt_tokens is not None and res.completion_tokens is not None:
                token_source, total_tokens = "provider", res.prompt_tokens + res.completion_tokens
            if core is None and fb_reason is None:
                fb_reason = "invalid_output"
        except CircuitOpenError:
            fb_reason = "circuit_open"
        except CallTimeoutError:
            fb_reason = "provider_timeout"
        except ProviderUnavailable:
            fb_reason = "provider_unavailable"
        except Exception:  # provider bug or transport error must not break the request
            fb_reason = "provider_error"
        if core is None:
            used, generated_by = self.fallback, "fallback"
            core = self._parse(self.fallback.complete(parts, facts).text)
            token_source, total_tokens = "estimate", tokens
        model = {
            "name": used.name,
            "version": used.version,
            "prompt_version": self.prompt.prompt_version,
            "generated_by": generated_by,
            "config_hash": cfg,
        }
        if core is None:
            out = self._abstain("schema_violation", used, sources, tokens, cfg, correlation_id, "blocked", fb_reason)
            return GatewayResult(out, input_hash, model, signals)
        if not core["abstained"] and core.get("confidence") is not None and core["confidence"] < 0.5:
            core = {"abstained": True, "abstain_reason": "low_confidence"}
        out = self._wrap(
            core,
            provider=used,
            generated_by=generated_by,
            fallback_reason=fb_reason,
            sources=sources,
            tokens=total_tokens,
            token_source=token_source,  # noqa: S106
            cfg=cfg,
            cid=correlation_id,
            guardrail="enforced",
        )
        if not self._valid(out):
            out = self._abstain("schema_violation", used, sources, tokens, cfg, correlation_id, "blocked", fb_reason)
            if not self._valid(out):  # last resort: never emit an invalid body
                raise RuntimeError("abstention output violates the schema")
        return GatewayResult(out, input_hash, model, signals)
