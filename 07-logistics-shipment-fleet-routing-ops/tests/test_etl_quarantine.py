"""FEAT-03: ETL validation, quarantine, idempotency (AC-08..AC-11; F-33..F-41, F-54, F-58..F-62)."""

import csv
import hashlib
import json
import shutil
from pathlib import Path

import pytest

from apps.api.config import ROOT, _semantic_dir
from etl.run_daily_batch import main, run
from etl.validation import SEVERITY_OVERRIDE

ORACLE = Path(__file__).resolve().parents[2] / "evidence" / "11-data-context" / "EVD-D-05-rule-baseline.json"


def _report(data_dir: Path) -> dict:
    return json.loads((data_dir / "reports" / "latest.json").read_text())


def test_ac08_block_violations_are_quarantined_not_curated(data_dir: Path) -> None:
    ship = list(csv.DictReader((data_dir / "curated" / "shipments.csv").open()))
    ids = [r["shipment_id"] for r in ship]
    assert "REC-0001" not in ids and len(ids) == len(set(ids))
    assert all(r["promised_at"] > "2000-01-01" for r in ship)
    assert all(r["customer_id"] for r in ship)
    q = [json.loads(x) for x in (data_dir / "quarantine" / "shipments.jsonl").read_text().splitlines()]
    assert {r["source_row"] for r in q} and all(r["rules"] for r in q)
    assert {"BR-P-shipments", "BR-K-shipments", "BR-10", "BR-11"} <= {x for r in q for x in r["rules"]}


def test_nfr5_no_duplicates_or_blanks_in_curated(data_dir: Path) -> None:
    for p in sorted((data_dir / "curated").glob("*.csv")):
        rows = list(csv.DictReader(p.open()))
        keys = [r[next(iter(r))] for r in rows]
        assert len(keys) == len(set(keys)), p.name


@pytest.mark.skipif(not ORACLE.exists(), reason="oracle evidence file is outside the app subtree")
def test_etl_rule_counts_match_the_stage_d_oracle(data_dir: Path) -> None:
    oracle = json.loads(ORACLE.read_text())
    mine = {}
    for ent in _report(data_dir)["entities"].values():
        mine.update(ent["rule_offending_rows"])
    mism = {
        k: (v["violations"], mine.get(k))
        for k, v in oracle.items()
        if v["violations"] is not None and mine.get(k) != v["violations"]
    }
    assert not mism, mism


def test_flag_not_quarantine_for_overridden_and_flag_severity_rules(data_dir: Path) -> None:
    rep = _report(data_dir)["entities"]
    assert SEVERITY_OVERRIDE["BR-04"] == "flag"
    assert rep["tracking_events"]["flags"]["rule:BR-04"] == 354
    assert rep["carrier_bookings"]["flags"]["rule:BR-13"] > 300
    assert rep["shipments"]["flags"]["actual_gt_declared"] > 100


def test_ac09_threshold_breach_exits_non_zero(tmp_path: Path) -> None:
    shutil.copytree(ROOT / "data" / "synthetic", tmp_path / "synthetic")
    assert main(["--data-dir", str(tmp_path), "--max-quarantine-ratio", "0.001"]) == 1
    assert main(["--data-dir", str(tmp_path), "--max-quarantine-ratio", "0.05"]) == 0


def test_ac10_idempotent_and_fixture_untouched(tmp_path: Path) -> None:
    shutil.copytree(ROOT / "data" / "synthetic", tmp_path / "synthetic")
    before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (tmp_path / "synthetic").iterdir()}
    r1 = run(tmp_path, tmp_path, _semantic_dir(), 0.05, False)
    h1 = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (tmp_path / "curated").iterdir()}
    r2 = run(tmp_path, tmp_path, _semantic_dir(), 0.05, False)
    h2 = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (tmp_path / "curated").iterdir()}
    assert h1 == h2 and r1["load_id"] == r2["load_id"] and r1["input_hash"] == r2["input_hash"]
    assert before == {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (tmp_path / "synthetic").iterdir()}


def test_repo_fixture_matches_baseline_manifest() -> None:
    m = json.loads((ROOT / "data" / "manifest.json").read_text())
    for name, expected in m["csv_files"].items():
        with (ROOT / "data" / "synthetic" / name).open(newline="", encoding="utf-8") as fh:
            assert sum(1 for _ in csv.DictReader(fh)) == expected


def test_ac11_multiple_active_bookings_reported(data_dir: Path) -> None:
    multi = _report(data_dir)["multiple_active_bookings"]
    assert multi and all(n > 1 for n in multi.values())


def test_report_has_run_identity_and_legacy_keys(data_dir: Path) -> None:
    rep = _report(data_dir)
    assert rep["run_id"].startswith("run-") and rep["load_id"].startswith("ld-") and rep["status"] == "pass"
    assert rep["legacy_compat"] == {"processed": 354, "malformed": 1, "sample": False}
    assert rep["totals"]["processed"] == 6 * 354
    assert rep["quarantine_ratio"] <= 0.05


def test_provenance_columns_on_curated_rows(data_dir: Path) -> None:
    row = next(csv.DictReader((data_dir / "curated" / "shipments.csv").open()))
    assert row["load_id"].startswith("ld-") and row["source_row"].isdigit()
