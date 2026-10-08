"""N1: the metric families the alerts and dashboards depend on exist, and safety counters exist at zero before any event."""

import json
import re
from pathlib import Path

import yaml
from fastapi.testclient import TestClient

from apps.api.config import ROOT
from tests.conftest import auth

REQUIRED = {
    "http_requests_total",
    "http_request_duration_seconds_bucket",
    "ai_request_duration_seconds_bucket",
    "ai_requests_total",
    "ai_tokens_total",
    "ai_fallback_total",
    "ai_guardrail_blocked_total",
    "ai_decisions_total",
    "audit_chain_valid",
    "data_load_age_seconds",
    "ai_circuit_open",
}


def _names(text: str) -> set[str]:
    return {m.group(1) for ln in text.splitlines() if (m := re.match(r"^([a-zA-Z_:][a-zA-Z0-9_:]*)", ln))}


def test_metric_families_and_zero_initialised_safety_counters(client: TestClient) -> None:
    client.post("/ai/summarize/SHI-00027", headers=auth("dispatcher"))
    text = client.get("/metrics", headers=auth("ops")).text
    assert _names(text) >= REQUIRED
    # present as a series whatever its value: the alert on the first leak needs a baseline sample
    assert re.search(r'^ai_fallback_total\{reason="output_policy_violation"\} \d', text, re.M)
    assert re.search(r"^ai_guardrail_blocked_total \d", text, re.M)


def test_every_metric_used_by_alerts_and_dashboards_is_exported(client: TestClient) -> None:
    client.post("/ai/summarize/SHI-00027", headers=auth("dispatcher"))
    client.get("/records/SHI-00027")  # 401 -> auth_denied_total (label-dynamic, so not zero-initialised)
    client.get("/records/SHI-00002", headers=auth("clinician"))  # 403 -> policy_denied_total
    exported = {re.sub(r"_(bucket|count|sum)$", "", n) for n in _names(client.get("/metrics", headers=auth("ops")).text)}
    exprs = [
        r["expr"]
        for g in yaml.safe_load((ROOT / "observability/alerts/alerts.yaml").read_text(encoding="utf-8"))["groups"]
        for r in g["rules"]
    ]
    for f in Path(ROOT / "observability/dashboards").glob("*.json"):
        exprs += [t["expr"] for p in json.loads(f.read_text(encoding="utf-8"))["panels"] for t in p["targets"]]
    used = {m for e in exprs for m in re.findall(r"\b([a-z]+(?:_[a-z]+)*_(?:total|seconds|bucket|open|valid))\b", e)}
    assert used, "no metric names found in alert/dashboard expressions"
    assert {re.sub(r"_(bucket|count|sum)$", "", u) for u in used} <= exported
