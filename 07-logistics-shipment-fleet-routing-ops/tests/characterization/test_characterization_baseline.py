import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest

from apps.api.services import domain_service

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "synthetic"

pytestmark = pytest.mark.characterization


def _rows(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_unknown_id_returns_first_row():
    """DEFECT-SCHEDULED (F-32, F-51): an unknown id silently returns the first shipments row."""
    row = domain_service.load_record("DOES-NOT-EXIST")
    assert row["shipment_id"] == "REC-0001"
    assert row["customer_id"] == "CUS-00001"
    assert row == _rows("shipments.csv")[0]


def test_rec0001_is_first_row_key_of_all_six_entities():
    """DEFECT-SCHEDULED (F-30): REC-0001 is the first-row primary key of all six datasets."""
    first = {
        "shipments.csv": "shipment_id",
        "tracking_events.csv": "event_id",
        "vehicles.csv": "vehicle_id",
        "routes.csv": "route_id",
        "carrier_bookings.csv": "booking_id",
        "ai_invocations.csv": "ai_call_id",
    }
    for name, key in first.items():
        assert _rows(name)[0][key] == "REC-0001", name
    assert domain_service.load_record("REC-0001")["shipment_id"] == "REC-0001"


def test_lookup_matches_non_key_column():
    """DEFECT-SCHEDULED (F-31): load_record scans every column, so a customer id finds a shipment."""
    row = domain_service.load_record("CUS-00002")
    assert row["customer_id"] == "CUS-00002"
    assert row["shipment_id"] == "SHI-00002"


def test_records_without_role_header_succeeds(client):
    """DEFECT-SCHEDULED (F-17): with no X-User-Role header the role defaults to operator and the call succeeds."""
    r = client.get("/records/SHI-00002")
    assert r.status_code == 200
    assert r.json()["shipment_id"] == "SHI-00002"


def test_records_clinician_role_succeeds(client):
    """DEFECT-SCHEDULED (F-19): a persona from another domain is on the allow-list."""
    r = client.get("/records/SHI-00002", headers={"X-User-Role": "clinician"})
    assert r.status_code == 200
    assert r.json()["shipment_id"] == "SHI-00002"


def test_unknown_role_is_forbidden_with_http_200():
    """INTENDED-LEGACY (partly DEFECT, F-18): a role outside the list gets an error body, still HTTP 200."""
    from fastapi.testclient import TestClient

    from apps.api.main import app

    r = TestClient(app).get("/records/SHI-00002", headers={"X-User-Role": "stranger"})
    assert r.status_code == 200
    assert r.json() == {"error": "forbidden"}


def test_ai_summary_without_any_role(client):
    """DEFECT-SCHEDULED (F-20): the AI endpoint needs no role at all."""
    r = client.post("/ai/summarize/SHI-00002")
    assert r.status_code == 200
    assert r.json()["model"] == "local-sim-v1"


def test_ai_guardrail_status_not_enforced(client):
    """DEFECT-SCHEDULED (F-24): every AI response states the guardrail is not enforced."""
    r = client.post("/ai/summarize/SHI-00002")
    assert r.json()["guardrail_status"] == "not_enforced"


def test_ai_summary_echoes_first_column(client):
    """DEFECT-SCHEDULED (F-29): the summary only echoes the record's first column value."""
    r = client.post("/ai/summarize/SHI-00002")
    assert r.json()["summary"] == "Synthetic summary for SHI-00002"
    assert r.json()["recommendation"] == "Review and approve before action"


def test_audit_event_has_no_actor_or_correlation(client, tmp_path):
    """DEFECT-SCHEDULED (F-43): the audit line holds only ts, action and details (record id and role)."""
    client.get("/records/SHI-00002", headers={"X-User-Role": "operator"})
    line = json.loads((tmp_path / "audit.log").read_text().splitlines()[-1])
    assert set(line) == {"ts", "action", "details"}
    assert line["action"] == "record.read"
    assert set(line["details"]) == {"record_id", "role"}


def test_health_ok_without_data_layer(client, tmp_path, monkeypatch):
    """DEFECT-SCHEDULED (F-46): /health returns ok even when the data directory is missing."""
    monkeypatch.setattr(domain_service, "DATA_DIR", tmp_path / "missing")
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_etl_reports_malformed_and_exits_zero():
    """INTENDED-LEGACY for counting; DEFECT-SCHEDULED (F-40) for the lack of quarantine and non-zero exit."""
    p = subprocess.run([sys.executable, "etl/run_daily_batch.py", "--sample"], cwd=ROOT, capture_output=True, text=True)
    assert p.returncode == 0
    assert "'processed': 354" in p.stdout
    assert "'malformed': 1" in p.stdout
