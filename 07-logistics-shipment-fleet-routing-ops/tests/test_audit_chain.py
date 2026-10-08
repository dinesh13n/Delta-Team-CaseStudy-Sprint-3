"""FEAT-05: audit and correlation (AC-18, AC-19, AC-20; F-42..F-45)."""

import json
import re
from pathlib import Path

import jsonschema
from fastapi.testclient import TestClient

from apps.api.audit_chain import GENESIS, JsonlAuditSink, build_event
from tests.conftest import auth

SCHEMA = json.loads(
    (Path(__file__).resolve().parents[1] / "data" / "contracts" / "schemas" / "audit-event.schema.json").read_text()
)


def _log(client: TestClient) -> list[dict]:
    return [json.loads(x) for x in Path(client.app.state.svc.settings.audit_path).read_text().splitlines()]  # type: ignore[attr-defined]


def test_ac18_every_protected_request_writes_a_schema_valid_event(client: TestClient) -> None:
    client.get("/records/SHI-00002", headers=auth("dispatcher", subject="alice"))
    client.post("/ai/summarize/SHI-00027", headers=auth("dispatcher", subject="alice"))
    log = _log(client)
    assert [e["action"] for e in log] == ["record.read", "ai.summary"]
    for e in log:
        assert not list(jsonschema.Draft202012Validator(SCHEMA).iter_errors(e)), e
        assert e["actor"]["subject"] == "alice" and e["actor"]["role"] == "dispatcher"
        assert e["tenant"] == "default" and e["resource"]["id"] in {"SHI-00002", "SHI-00027"}
        assert e["policy_decision"]["decision"] == "allow" and e["policy_decision"]["rule"].startswith("access:")
        assert re.fullmatch(r"\d{4}-\d\d-\d\dT[\d:.]+Z", e["ts"])  # timezone-aware UTC (F-45)
    ai = log[1]
    assert (
        ai["model"]["name"] == "deterministic"
        and ai["model"]["prompt_version"]
        and re.fullmatch("[a-f0-9]{64}", ai["input_hash"])
    )
    assert client.get("/audit/verify", headers=auth("auditor")).json()["valid"] is True


def test_denied_and_unauthenticated_requests_are_audited(client: TestClient) -> None:
    client.get("/records/SHI-00002")
    client.get("/records/SHI-00002", headers=auth("clinician"))
    log = _log(client)
    assert log[0]["action"] == "auth.denied" and log[0]["actor"]["subject"] == "anonymous"
    assert log[1]["action"] == "record.read.denied" and log[1]["outcome"] == "denied"
    for e in log:
        assert not list(jsonschema.Draft202012Validator(SCHEMA).iter_errors(e)), e


def test_ac19_tampering_is_detected(client: TestClient) -> None:
    for _ in range(3):
        client.get("/records/SHI-00002", headers=auth("dispatcher"))
    p = Path(client.app.state.svc.settings.audit_path)  # type: ignore[attr-defined]
    lines = p.read_text().splitlines()
    rec = json.loads(lines[1])
    rec["actor"]["subject"] = "mallory"
    lines[1] = json.dumps(rec, sort_keys=True, separators=(",", ":"))
    p.write_text("\n".join(lines) + "\n")
    v = client.get("/audit/verify", headers=auth("auditor")).json()
    assert v["valid"] is False and v["first_bad_index"] == 1


def test_deleted_line_and_truncated_json_are_detected(tmp_path: Path) -> None:
    s = JsonlAuditSink(tmp_path / "a.log")
    for i in range(4):
        s.append(
            build_event(
                action="x.y",
                subject="u",
                role="r",
                correlation_id="corr-000000001",
                tenant="default",
                resource_type="t",
                resource_id=str(i),
                decision="allow",
                rule="r",
                decision_id=None,
                outcome="success",
            )
        )
    lines = (tmp_path / "a.log").read_text().splitlines()
    (tmp_path / "b.log").write_text("\n".join([lines[0], lines[2], lines[3]]) + "\n")
    assert JsonlAuditSink(tmp_path / "b.log").verify()["first_bad_index"] == 1
    (tmp_path / "c.log").write_text(lines[0] + "\n" + lines[1][:20] + "\n")
    assert JsonlAuditSink(tmp_path / "c.log").verify()["valid"] is False
    assert JsonlAuditSink(tmp_path / "missing.log").verify() == {"valid": True, "records": 0, "first_bad_index": None}


def test_chain_continues_across_restarts(tmp_path: Path) -> None:
    ev = dict(
        action="x.y",
        subject="u",
        role="r",
        correlation_id="corr-000000001",
        tenant="default",
        resource_type="t",
        resource_id="1",
        decision="allow",
        rule="r",
        decision_id=None,
        outcome="success",
    )
    JsonlAuditSink(tmp_path / "a.log").append(build_event(**ev))
    s2 = JsonlAuditSink(tmp_path / "a.log")
    second = s2.append(build_event(**ev))
    assert second["prev_hash"] != GENESIS and s2.verify() == {"valid": True, "records": 2, "first_bad_index": None}


def test_ac20_correlation_id_is_echoed_and_recorded(client: TestClient) -> None:
    cid = "my-corr-id-12345"
    r = client.get("/records/SHI-00002", headers={**auth("dispatcher"), "X-Correlation-ID": cid})
    assert r.headers["X-Correlation-ID"] == cid
    assert _log(client)[-1]["correlation_id"] == cid


def test_ac20_generated_when_missing_or_malformed(client: TestClient) -> None:
    for hdr in ({}, {"X-Correlation-ID": "bad id with spaces"}, {"X-Correlation-ID": "x"}):
        r = client.get("/records/SHI-00002", headers={**auth("dispatcher"), **hdr})
        assert re.fullmatch(r"corr-[0-9a-f]{16}", r.headers["X-Correlation-ID"])
    assert all(re.fullmatch(r"corr-[0-9a-f]{16}", e["correlation_id"]) for e in _log(client))


def test_errors_carry_the_correlation_id(client: TestClient) -> None:
    r = client.get("/records/SHI-99999", headers={**auth("dispatcher"), "X-Correlation-ID": "trace-abcdef-01"})
    assert r.status_code == 404 and r.json()["correlation_id"] == "trace-abcdef-01"


def test_audit_verify_and_metrics_need_platform_roles(client: TestClient) -> None:
    assert client.get("/audit/verify", headers=auth("dispatcher")).status_code == 403
    assert client.get("/metrics", headers=auth("dispatcher")).status_code == 403
    assert client.get("/audit/verify").status_code == 401
