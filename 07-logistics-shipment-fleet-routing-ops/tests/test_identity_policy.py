"""FEAT-02: identity and policy (AC-04..AC-07; F-17..F-21)."""

import json
import subprocess
import sys
from itertools import product
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from apps.api.config import ROOT, _semantic_dir
from apps.api.security.policy import MASK, PolicyEngine
from apps.api.security.tokens import Hs256Verifier, TokenError, issue_dev_token
from tests.conftest import SECRET, auth

ENGINE = PolicyEngine.from_dir(_semantic_dir())


def test_ac04_no_token_is_401(client: TestClient) -> None:
    r = client.get("/records/SHI-00002")
    assert r.status_code == 401
    assert r.headers["www-authenticate"] == "Bearer"
    assert r.json()["correlation_id"]


def test_ac05_role_header_is_ignored(client: TestClient) -> None:
    assert client.get("/records/SHI-00002", headers={"X-User-Role": "admin"}).status_code == 401


def test_clinician_token_is_denied(client: TestClient) -> None:
    assert client.get("/records/SHI-00002", headers=auth("clinician")).status_code == 403


def test_f20_ai_endpoint_requires_auth(client: TestClient) -> None:
    assert client.post("/ai/summarize/SHI-00002").status_code == 401


def test_expired_and_wrong_key_tokens_are_401(client: TestClient) -> None:
    assert client.get("/records/SHI-00002", headers=auth("dispatcher", ttl=-3600)).status_code == 401
    assert client.get("/records/SHI-00002", headers=auth("dispatcher", secret="y" * 40)).status_code == 401


def test_alg_none_token_is_rejected() -> None:
    import base64

    def b64(d: dict[str, object]) -> str:
        return base64.urlsafe_b64encode(json.dumps(d).encode()).rstrip(b"=").decode()

    tok = b64({"alg": "none", "typ": "JWT"}) + "." + b64({"sub": "x", "role": "dispatcher", "exp": 4102444800}) + "."
    with pytest.raises(TokenError):
        Hs256Verifier(SECRET).verify(tok)


def test_token_without_role_is_rejected() -> None:
    import jwt

    tok = jwt.encode({"sub": "u", "exp": 4102444800}, SECRET, algorithm="HS256")
    with pytest.raises(TokenError):
        Hs256Verifier(SECRET).verify(tok)


def test_ac06_customer_id_masked_for_dispatcher_allowed_for_support(client: TestClient) -> None:
    d = client.get("/records/SHI-00002", headers=auth("dispatcher")).json()
    s = client.get("/records/SHI-00002", headers=auth("customer_support")).json()
    assert d["customer_id"] == MASK
    assert s["customer_id"].startswith("CUS-")


def test_denied_field_is_absent(client: TestClient) -> None:
    w = client.get("/records/SHI-00002", headers=auth("warehouse_ops")).json()
    assert "customer_id" not in w


def test_ac07_denial_is_403_problem_and_audited(client: TestClient) -> None:
    r = client.get("/records/SHI-00002", headers=auth("carrier_partner", purpose="marketing"))
    assert r.status_code == 403 and r.headers["content-type"].startswith("application/problem+json")
    assert r.json()["policy_decision_id"].startswith("pd-")
    lines = [json.loads(x) for x in Path(client.app.state.svc.settings.audit_path).read_text().splitlines()]  # type: ignore[attr-defined]
    last = lines[-1]
    assert last["policy_decision"]["decision"] == "deny" and last["action"] == "record.read.denied"


def test_policy_unknown_persona_and_action_denied() -> None:
    assert not ENGINE.decide("admin", "shipments", "read").allow
    assert not ENGINE.decide("dispatcher", "shipments", "delete").allow
    assert not ENGINE.decide("ai_agent", "vehicles", "read").allow


def test_write_requires_write_level() -> None:
    assert ENGINE.decide("dispatcher", "shipments", "write", "dispatch").allow
    assert not ENGINE.decide("customer_support", "shipments", "write").allow


def test_scope_is_reported_not_enforced_for_narrow_scopes() -> None:
    d = ENGINE.decide("warehouse_ops", "shipments", "read")
    assert d.allow and d.scope == "own hub" and d.scope_enforced is False


def test_issued_token_round_trip() -> None:
    c = Hs256Verifier(SECRET).verify(issue_dev_token(SECRET, "abc", "dispatcher", purpose="dispatch"))
    assert (c.subject, c.role, c.purpose) == ("abc", "dispatcher", "dispatch")


# ---- policy as code parity (ADR-0005) --------------------------------------------------------------
def test_generated_rego_is_current() -> None:
    assert subprocess.run([sys.executable, str(ROOT / "scripts" / "generate_rego.py"), "--check"]).returncode == 0


def _opa() -> str | None:
    import shutil

    return shutil.which("opa") or (str(Path.home() / "fde" / "opa") if (Path.home() / "fde" / "opa").exists() else None)


@pytest.mark.skipif(_opa() is None, reason="opa binary not available: Rego evaluation parity is CONDITIONAL")
def test_python_engine_and_rego_agree_on_full_grid(tmp_path: Path) -> None:
    m = ENGINE.matrix()
    personas = sorted(m) + ["admin", "clinician"]
    entities = sorted({e for p in m.values() for e in p}) + ["unknown_entity"]
    purposes = sorted({x for p in m.values() for e in p.values() for x in e["purposes"]}) + ["marketing"]
    grid = [
        {"persona": p, "entity": e, "action": a, "purpose": u}
        for p, e, a, u in product(personas, entities, ["read", "write"], purposes)
    ]
    (tmp_path / "grid.json").write_text(json.dumps({"grid": grid}))
    q = (
        '{k: v | some i in data.grid; k := sprintf("%s|%s|%s|%s", [i.persona, i.entity, i.action, i.purpose]); '
        "v := data.logistics.access.allow with input as i}"
    )
    out = subprocess.run(
        [
            _opa() or "opa",
            "eval",
            "-f",
            "json",
            "-d",
            str(ROOT / "policy" / "opa" / "access.rego"),
            "-d",
            str(tmp_path / "grid.json"),
            q,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    rego = json.loads(out.stdout)["result"][0]["expressions"][0]["value"]
    mism = [k for k, v in rego.items() if v != ENGINE.decide(*k.split("|")[:3], k.split("|")[3]).allow]
    assert len(rego) == len(grid) and not mism, mism[:5]
