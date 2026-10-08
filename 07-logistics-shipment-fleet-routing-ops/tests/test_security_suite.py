"""K3 / K-X5: repeatable security tests (runs in CI). Each test names the threat it covers (docs/24-security-privacy)."""

import base64
import json
import re
import time

import jwt
import pytest
from fastapi.testclient import TestClient

from tests.conftest import SECRET, auth


def _tok(**claims: object) -> dict[str, str]:
    now = int(time.time())
    payload = {"sub": "attacker", "role": "dispatcher", "iat": now, "exp": now + 600, **claims}
    return {"Authorization": "Bearer " + jwt.encode(payload, SECRET, algorithm="HS256")}


# ---- S: spoofing / identity -------------------------------------------------------------------------------------------
def test_alg_none_token_is_rejected(client: TestClient) -> None:
    now = int(time.time())
    t = jwt.encode({"sub": "x", "role": "admin", "exp": now + 600}, None, algorithm="none")  # type: ignore[arg-type]
    assert client.get("/records/SHI-00002", headers={"Authorization": "Bearer " + t}).status_code == 401


def test_tampered_payload_with_original_signature_is_rejected(client: TestClient) -> None:
    head, payload, sig = auth("dispatcher")["Authorization"].split(" ")[1].split(".")
    body = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))
    body["role"] = "admin"
    forged = base64.urlsafe_b64encode(json.dumps(body).encode()).rstrip(b"=").decode()
    r = client.get("/records/SHI-00002", headers={"Authorization": f"Bearer {head}.{forged}.{sig}"})
    assert r.status_code == 401


@pytest.mark.parametrize("missing", ["exp", "sub"])
def test_token_without_required_claims_is_rejected(client: TestClient, missing: str) -> None:
    now = int(time.time())
    claims = {"sub": "x", "role": "dispatcher", "exp": now + 600}
    claims.pop(missing)
    t = jwt.encode(claims, SECRET, algorithm="HS256")
    assert client.get("/records/SHI-00002", headers={"Authorization": "Bearer " + t}).status_code == 401


def test_token_without_role_or_with_non_string_role_is_rejected(client: TestClient) -> None:
    now = int(time.time())
    for role in (None, 5, ["admin"], ""):
        c = {"sub": "x", "exp": now + 600}
        if role is not None:
            c["role"] = role  # type: ignore[assignment]
        t = jwt.encode(c, SECRET, algorithm="HS256")
        assert client.get("/records/SHI-00002", headers={"Authorization": "Bearer " + t}).status_code == 401


def test_identity_headers_other_than_the_token_are_ignored(client: TestClient) -> None:
    spoof = {"X-User-Role": "admin", "X-Forwarded-User": "root", "X-Role": "admin", "Remote-User": "root"}
    assert client.get("/records/SHI-00002", headers=spoof).status_code == 401
    r = client.get("/records/SHI-00002", headers={**_tok(role="dispatcher"), **spoof})
    assert r.status_code == 200 and r.json()["customer_id"] == "***"  # still the token's persona rules, not the spoofed admin


def test_metrics_and_audit_verify_need_platform_roles(client: TestClient) -> None:
    assert client.get("/metrics", headers=auth("dispatcher")).status_code == 403
    assert client.get("/audit/verify", headers=auth("dispatcher")).status_code == 403
    assert client.get("/metrics", headers=auth("ops")).status_code == 200
    assert client.get("/audit/verify", headers=auth("ops")).status_code == 403  # roles do not imply each other


# ---- T/I: tampering, injection, traversal ---------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "rid",
    [
        "..%2f..%2fetc%2fpasswd",
        "SHI-00002'%20OR%20'1'='1",
        "SHI-00002%00",
        "%3Cscript%3E",
        "SHI-0000%0d%0aX-Injected:1",
        "A" * 5000,
    ],
)
def test_hostile_identifiers_never_reach_data_access(client: TestClient, rid: str) -> None:
    r = client.get(f"/records/{rid}", headers=auth("dispatcher"))
    assert r.status_code in {404, 422} and "SHI-0" not in r.text.replace("SHI-0000", "")
    assert "x-injected" not in {k.lower() for k in r.headers}


def test_unsupported_methods_are_not_routed(client: TestClient) -> None:
    h = auth("dispatcher")
    for m in ("put", "delete", "patch"):
        assert getattr(client, m)("/records/SHI-00002", headers=h).status_code == 405


def test_attacker_chosen_correlation_id_is_not_echoed_unless_well_formed(client: TestClient) -> None:
    r = client.get("/health", headers={"X-Correlation-ID": "bad id; <script>"})
    assert re.fullmatch(r"corr-[0-9a-f]{16}", r.headers["x-correlation-id"])
    ok = client.get("/health", headers={"X-Correlation-ID": "trace-abc-12345"})
    assert ok.headers["x-correlation-id"] == "trace-abc-12345"


def test_extra_fields_in_decision_body_cannot_set_server_fields(client: TestClient) -> None:
    s = client.post("/ai/summarize/SHI-00027", headers=auth("dispatcher")).json()
    r = client.post(
        f"/ai/summaries/{s['summary_id']}/decision",
        headers=auth("dispatcher", subject="alice"),
        json={"decision": "approve", "decided_by": "ceo", "approval_id": "apr-forged", "decided_at": "2000-01-01T00:00:00Z"},
    )
    assert r.status_code == 200 and r.json()["decided_by"] == "alice" and r.json()["approval_id"] != "apr-forged"


# ---- R/D: repudiation, DoS ------------------------------------------------------------------------------------------------
def test_ai_rate_limit_returns_429_with_retry_after(settings) -> None:  # type: ignore[no-untyped-def]
    from apps.api.config import Settings
    from apps.api.main import create_app

    c = TestClient(create_app(Settings(**{**settings.__dict__, "ai_rate_per_minute": 3})))
    codes = [c.post("/ai/summarize/SHI-00027", headers=auth("dispatcher", subject="flood")).status_code for _ in range(5)]
    assert codes == [200, 200, 200, 429, 429]
    r = c.post("/ai/summarize/SHI-00027", headers=auth("dispatcher", subject="flood"))
    assert r.headers["retry-after"] == "60"
    assert c.post("/ai/summarize/SHI-00027", headers=auth("dispatcher", subject="other")).status_code == 200  # per subject


def test_page_size_is_bounded(client: TestClient) -> None:
    assert client.get("/shipments?limit=100000", headers=auth("dispatcher")).status_code == 422
    assert client.get("/shipments?limit=100", headers=auth("dispatcher")).status_code == 200


# ---- I: information disclosure --------------------------------------------------------------------------------------------
def test_unexpected_errors_do_not_leak_internals(settings, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    from apps.api.main import create_app

    app = create_app(settings)

    def boom(*a: object, **k: object) -> None:
        raise RuntimeError("secret-internal-path /srv/app/data.csv")

    monkeypatch.setattr(app.state.svc.repo, "get", boom)
    r = TestClient(app, raise_server_exceptions=False).get("/records/SHI-00002", headers=auth("dispatcher"))
    assert r.status_code == 500 and "secret-internal" not in r.text and "Traceback" not in r.text
    assert r.json()["correlation_id"]


def test_no_cors_headers_for_foreign_origins(client: TestClient) -> None:
    r = client.options("/records/SHI-00002", headers={"Origin": "https://evil.example", "Access-Control-Request-Method": "GET"})
    assert "access-control-allow-origin" not in {k.lower() for k in r.headers}


def test_secrets_never_appear_in_openapi_metrics_or_ready(client: TestClient) -> None:
    for resp in (client.get("/openapi.json"), client.get("/ready"), client.get("/metrics", headers=auth("ops"))):
        assert SECRET not in resp.text and "AUTH_SECRET" not in resp.text


def test_ai_output_never_contains_customer_or_driver_identifiers(client: TestClient) -> None:
    h = auth("dispatcher")
    items = client.get("/shipments?limit=40", headers=h).json()["items"]
    assert items
    for it in items:
        body = client.post(f"/ai/summarize/{it['shipment_id']}", headers=h).text
        assert not re.search(r"CUS-\d{5}|DRI-\d{5}|VEH-\d{5}", body), it["shipment_id"]


def test_masked_fields_are_masked_for_every_list_item(client: TestClient) -> None:
    items = client.get("/shipments?limit=50", headers=auth("dispatcher")).json()["items"]
    assert all(i["customer_id"] in ("***", None, "") for i in items)


def test_unauthenticated_and_forged_attempts_are_audited(client: TestClient) -> None:
    from pathlib import Path

    client.get("/records/SHI-00002")
    client.get("/records/SHI-00002", headers={"Authorization": "Bearer not.a.jwt"})
    log = [json.loads(x) for x in Path(client.app.state.svc.settings.audit_path).read_text().splitlines()]  # type: ignore[attr-defined]
    assert [e["action"] for e in log[:2]] == ["auth.denied", "auth.denied"] and log[0]["actor"]["subject"] == "anonymous"


def test_oversized_request_body_is_rejected_before_processing(client: TestClient) -> None:
    s = client.post("/ai/summarize/SHI-00027", headers=auth("dispatcher")).json()
    big = {"decision": "approve", "reason": "x" * (70 * 1024)}
    r = client.post(f"/ai/summaries/{s['summary_id']}/decision", headers=auth("dispatcher"), json=big)
    assert r.status_code == 413


def test_api_documentation_endpoints_are_off_outside_local(settings) -> None:  # type: ignore[no-untyped-def]
    from apps.api.config import Settings
    from apps.api.main import create_app

    prod = TestClient(create_app(Settings(**{**settings.__dict__, "app_env": "prod", "auth_secret": SECRET})))
    for path in ("/openapi.json", "/docs", "/redoc"):
        assert prod.get(path).status_code == 404, path
    assert prod.get("/health").status_code == 200


def test_api_responses_are_not_cacheable_and_not_sniffable(client: TestClient) -> None:
    for r in (
        client.get("/records/SHI-00002", headers=auth("dispatcher")),
        client.get("/records/SHI-00002"),
        client.get("/health"),
    ):
        assert r.headers["cache-control"] == "no-store" and r.headers["x-content-type-options"] == "nosniff"
