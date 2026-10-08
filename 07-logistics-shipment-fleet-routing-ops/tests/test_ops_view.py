"""J4 / AC-26: the thin operations view is served, safe, and its workflow works end to end through the API it calls."""

import re
from pathlib import Path

from fastapi.testclient import TestClient

from apps.api.config import ROOT
from tests.conftest import auth

PUBLIC = ROOT / "apps" / "web" / "public"


def test_view_is_served_with_security_headers(client: TestClient) -> None:
    r = client.get("/ops/")
    assert r.status_code == 200 and "Operations view" in r.text
    csp = r.headers["content-security-policy"]
    assert "default-src 'self'" in csp and "frame-ancestors 'none'" in csp and "unsafe-inline" not in csp
    assert r.headers["x-content-type-options"] == "nosniff"
    assert client.get("/ops/app.js").status_code == 200


def test_view_has_no_unsafe_dom_sinks() -> None:
    js = (PUBLIC / "app.js").read_text()
    html = (PUBLIC / "index.html").read_text()
    for sink in ("innerHTML", "outerHTML", "insertAdjacentHTML", "document.write", "eval(", "new Function"):
        assert sink not in js, sink
    assert not re.search(r"<script(?![^>]*\bsrc=)", html)
    assert not re.search(r"\son[a-z]+=", html)


def test_every_api_path_the_view_calls_is_in_the_contract(client: TestClient) -> None:
    js = (PUBLIC / "app.js").read_text()
    paths = client.get("/openapi.json").json()["paths"]
    for called in ("/shipments", "/records/", "/ai/summarize/", "/ai/summaries/"):
        assert called in js
    assert "/shipments" in paths and "/records/{record_id}" in paths and "/ai/summarize/{record_id}" in paths
    assert "/ai/summaries/{summary_id}/decision" in paths and "/shipments/{shipment_id}/events" in paths


def test_end_to_end_workflow_list_record_summarize_decide(client: TestClient) -> None:
    h = auth("dispatcher")
    page = client.get("/shipments", params={"limit": 5, "status": "exception"}, headers=h).json()
    assert page["items"] and all(i["status"] == "exception" for i in page["items"])
    sid = page["items"][0]["shipment_id"]
    rec = client.get(f"/records/{sid}", headers=h).json()
    assert rec["customer_id"] == "***"  # masked for this persona
    assert isinstance(client.get(f"/shipments/{sid}/events", headers=h).json(), list)
    s = client.post(f"/ai/summarize/{sid}", headers=h)
    assert s.status_code == 200 and s.json()["requires_human_approval"] is True
    sum_id = s.json()["summary_id"]
    d = client.post(f"/ai/summaries/{sum_id}/decision", headers=h, json={"decision": "approve", "reason": "checked"})
    assert d.status_code == 200 and d.json()["decided_by"] == "u-test"
    again = client.post(f"/ai/summaries/{sum_id}/decision", headers=h, json={"decision": "reject"})
    assert again.status_code == 409  # one decision per suggestion
    v = client.get("/audit/verify", headers=auth("auditor")).json()
    assert v["valid"] is True


def test_view_requires_a_token_for_data(client: TestClient) -> None:
    assert client.get("/shipments").status_code == 401


def test_playwright_spec_is_not_vacuous() -> None:
    spec = Path(ROOT / "tests" / "playwright" / "operations.spec.ts").read_text()
    assert "Summarize exception" in spec and "Recorded:" in spec  # F-52: asserts real content, not just <body>
