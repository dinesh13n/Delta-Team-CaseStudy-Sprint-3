"""K1 / K-X2: human control is enforced in code, not stated in prose (F-26, F-36)."""

import json
from pathlib import Path

from fastapi.testclient import TestClient

from tests.conftest import auth

MUTATING = {"post", "put", "patch", "delete"}


def _summary(c: TestClient, sid: str = "SHI-00027", role: str = "dispatcher") -> dict:
    r = c.post(f"/ai/summarize/{sid}", headers=auth(role))
    assert r.status_code == 200, r.text
    return r.json()


def test_no_endpoint_lets_the_system_change_a_shipment_route_or_booking(client: TestClient) -> None:
    paths = client.get("/openapi.json").json()["paths"]
    mutating = {(p, m) for p, v in paths.items() for m in v if m in MUTATING}
    assert mutating == {("/ai/summarize/{record_id}", "post"), ("/ai/summaries/{summary_id}/decision", "post")}


def test_every_suggestion_requires_human_approval_even_when_abstained(client: TestClient) -> None:
    for sid in ("SHI-00027", "SHI-00002", "SHI-00010"):
        s = _summary(client, sid)
        assert s["requires_human_approval"] is True and s["guardrail_status"] in {"enforced", "blocked"}


def test_ai_persona_cannot_approve_its_own_suggestion(client: TestClient) -> None:
    s = _summary(client)
    r = client.post(f"/ai/summaries/{s['summary_id']}/decision", headers=auth("ai_agent"), json={"decision": "approve"})
    assert r.status_code == 403


def test_read_only_personas_cannot_decide(client: TestClient) -> None:
    s = _summary(client)
    for role in ("customer_support", "driver", "customs_agent", "carrier_partner"):
        r = client.post(f"/ai/summaries/{s['summary_id']}/decision", headers=auth(role), json={"decision": "approve"})
        assert r.status_code == 403, role


def test_only_one_decision_per_suggestion_and_it_is_final(client: TestClient) -> None:
    s = _summary(client)
    url = f"/ai/summaries/{s['summary_id']}/decision"
    h = auth("dispatcher", subject="alice")
    assert client.post(url, headers=h, json={"decision": "reject", "reason": "wrong carrier"}).status_code == 200
    assert client.post(url, headers=h, json={"decision": "approve"}).status_code == 409
    assert client.post(url, headers=auth("dispatcher", subject="bob"), json={"decision": "approve"}).status_code == 409


def test_decision_input_is_validated(client: TestClient) -> None:
    s = _summary(client)
    url = f"/ai/summaries/{s['summary_id']}/decision"
    h = auth("dispatcher")
    assert client.post(url, headers=h, json={"decision": "execute"}).status_code == 422
    assert client.post(url, headers=h, json={}).status_code == 422
    assert client.post(url, headers=h, json={"decision": "approve", "reason": "x" * 501}).status_code == 422
    assert client.post("/ai/summaries/sum-doesnotexist/decision", headers=h, json={"decision": "approve"}).status_code == 404


def test_decision_is_audited_with_actor_and_approval_id_and_chain_stays_valid(client: TestClient) -> None:
    s = _summary(client)
    d = client.post(
        f"/ai/summaries/{s['summary_id']}/decision", headers=auth("dispatcher", subject="alice"), json={"decision": "approve"}
    ).json()
    log = [json.loads(x) for x in Path(client.app.state.svc.settings.audit_path).read_text().splitlines()]  # type: ignore[attr-defined]
    dec = [e for e in log if e["action"] == "ai.decision"][-1]
    assert dec["approval_id"] == d["approval_id"] and dec["actor"]["subject"] == "alice"
    assert dec["detail"]["decision"] == "approve"
    assert client.get("/audit/verify", headers=auth("auditor")).json()["valid"] is True


def test_denied_decision_attempts_are_audited(client: TestClient) -> None:
    s = _summary(client)
    client.post(f"/ai/summaries/{s['summary_id']}/decision", headers=auth("ai_agent"), json={"decision": "approve"})
    log = [json.loads(x) for x in Path(client.app.state.svc.settings.audit_path).read_text().splitlines()]  # type: ignore[attr-defined]
    assert any(e["action"] == "ai.decision.denied" and e["actor"]["role"] == "ai_agent" for e in log)


def test_low_confidence_model_output_becomes_an_abstention(client: TestClient) -> None:
    from apps.api.ai.providers import ProviderResult
    from tests.test_ai_gateway import _gw  # reuse the gateway builder with a scripted provider

    class Unsure:
        name, version = "unsure", "1"

        def complete(self, parts, facts):  # type: ignore[no-untyped-def]
            return ProviderResult(json.dumps({"summary": "s", "recommendation": "r", "confidence": 0.2, "abstained": False}))

    out = _gw(client, Unsure()).summarize("SHI-00027", "corr-test-0001").output
    assert out["abstained"] is True and out["abstain_reason"] == "low_confidence" and out["recommendation"] is None


def test_ai_audit_event_records_what_the_ai_did_and_from_which_data(client: TestClient) -> None:
    s = _summary(client)
    log = [json.loads(x) for x in Path(client.app.state.svc.settings.audit_path).read_text().splitlines()]  # type: ignore[attr-defined]
    ev = [e for e in log if e["action"] == "ai.summary"][-1]
    d = ev["detail"]
    assert (
        d["summary_id"] == s["summary_id"]
        and d["generated_by"] == s["generated_by"]
        and d["guardrail_status"] == s["guardrail_status"]
    )
    assert d["prompt_version"] == s["prompt_version"] and d["data_load_id"].startswith("ld-") and "fallback_reason" in d
