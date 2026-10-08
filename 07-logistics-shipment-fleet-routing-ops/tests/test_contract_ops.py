"""FEAT-06: operability and contract (AC-21, AC-22, AC-23, AC-25; F-46, F-50)."""

import re
from dataclasses import replace
from pathlib import Path

import yaml
from fastapi.testclient import TestClient

from apps.api.config import ROOT, Settings
from apps.api.main import create_app
from tests.conftest import auth

CONTRACT = yaml.safe_load((ROOT / "data" / "contracts" / "openapi.yaml").read_text())


def _ops(paths: dict) -> set[tuple[str, str]]:
    return {(m.upper(), p) for p, v in paths.items() for m in v if m in {"get", "post", "put", "patch", "delete"}}


def test_ac22_contract_matches_live_routes(client: TestClient) -> None:
    live = client.get("/openapi.json").json()
    assert _ops(live["paths"]) == _ops(CONTRACT["paths"])


def test_contract_covers_every_decorated_route_in_main() -> None:
    src = (ROOT / "apps" / "api" / "main.py").read_text()
    code = {(m.group(1).upper(), m.group(2)) for m in re.finditer(r'@app\.(get|post)\("([^"]+)"', src)}
    assert code and code <= _ops(CONTRACT["paths"])


def test_contract_is_valid_openapi() -> None:
    from openapi_spec_validator import validate

    validate(CONTRACT)


def test_documented_status_codes_for_record_lookup() -> None:
    assert set(CONTRACT["paths"]["/records/{record_id}"]["get"]["responses"]) == {"200", "401", "403", "404", "422"}
    assert {"200", "401", "403", "404", "422", "429", "503"} == set(
        CONTRACT["paths"]["/ai/summarize/{record_id}"]["post"]["responses"]
    )


def test_health_is_liveness_only_and_open(client: TestClient) -> None:
    r = client.get("/health")
    assert r.status_code == 200 and r.json()["status"] == "ok"


def test_ac21_ready_reflects_data_layer(settings: Settings, tmp_path: Path) -> None:
    ok = TestClient(create_app(settings))
    assert ok.get("/ready").status_code == 200 and ok.get("/ready").json()["status"] == "ready"
    broken = TestClient(
        create_app(
            replace(settings, data_dir=tmp_path / "nowhere", audit_path=tmp_path / "x.log", approvals_path=tmp_path / "y.jsonl")
        )
    )
    assert broken.get("/health").status_code == 200
    r = broken.get("/ready")
    assert r.status_code == 503 and r.headers["content-type"].startswith("application/problem+json")


def test_ac23_metrics_expose_ai_and_http_counters(client: TestClient) -> None:
    client.post("/ai/summarize/SHI-00027", headers=auth("dispatcher"))
    client.get("/records/SHI-00002", headers=auth("dispatcher"))
    text = client.get("/metrics", headers=auth("ops")).text
    for name in (
        "http_requests_total",
        "http_request_duration_seconds_bucket",
        "ai_requests_total",
        "ai_tokens_total",
        "audit_chain_valid 1",
    ):
        assert name in text, name


def test_kpis_endpoint(client: TestClient) -> None:
    body = client.get("/kpis", headers=auth("dispatcher")).json()
    ids = [k["id"] for k in body["kpis"]]
    assert ids == [f"K{i}" for i in range(1, 11)]
    k = {x["id"]: x for x in body["kpis"]}
    assert k["K4"]["value"] == 100 * 1008 / 3000  # fixture: 983 null + 1,009 empty = 1,992 unusable (D-012)
    assert k["K4"]["detail"]["non_null_pct"] == 100 * (3000 - 983) / 3000
    assert k["K7"]["value"] == 0 and k["K8"]["value"] == 0  # curated layer has no duplicate keys or blank rows
    assert k["K9"]["data_gap"] is True


def test_openapi_ui_does_not_leak_secrets(client: TestClient) -> None:
    assert "AUTH_SECRET" not in client.get("/openapi.json").text
