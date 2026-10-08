"""Contract tests of the original repository (kept; adapted for the approved behaviour changes in H4/H5).

Approved change (docs/15-modernization/approved-behavior-changes.md AB-02): /ai/summarize needs a verified token and a
well-formed shipment id; the original test posted REC-0001 without any identity.
"""

from fastapi.testclient import TestClient

from tests.conftest import auth


def test_health_contract(client: TestClient) -> None:
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_ai_summary_has_minimum_contract(client: TestClient) -> None:
    r = client.post("/ai/summarize/SHI-00002", headers=auth("dispatcher"))
    assert r.status_code == 200
    body = r.json()
    assert "summary" in body
    assert "model" in body
    assert "guardrail_status" in body
