"""M3 follow-ups from the failure drills: ETL publishes atomically per run, /ready can report stale data."""

import hashlib
import json
import shutil
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

import etl.run_daily_batch as batch
from apps.api.config import ROOT, Settings, _semantic_dir
from apps.api.main import create_app


def _tree_hash(root: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(
        x for x in root.rglob("*") if x.is_file() and x.relative_to(root).parts[0] in {"curated", "quarantine", "reports"}
    ):
        h.update(str(p.relative_to(root)).encode())
        h.update(p.read_bytes())
    return h.hexdigest()


def test_a_failure_part_way_through_a_run_leaves_the_published_layers_untouched(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    shutil.copytree(ROOT / "data" / "synthetic", tmp_path / "synthetic")
    batch.run(tmp_path, tmp_path, _semantic_dir(), 0.05, False)
    before = _tree_hash(tmp_path)
    # change the input so a successful second run would differ, then make the run die while writing
    ship = tmp_path / "synthetic" / "shipments.csv"
    ship.write_text(ship.read_text(encoding="utf-8").replace(",queued,", ",new,", 5), encoding="utf-8")
    calls = {"n": 0}
    real = batch.evaluate_entity

    def dies_on_third_entity(*a: object, **k: object):  # type: ignore[no-untyped-def]
        calls["n"] += 1
        if calls["n"] == 3:
            raise RuntimeError("disk full (injected)")
        return real(*a, **k)

    monkeypatch.setattr(batch, "evaluate_entity", dies_on_third_entity)
    with pytest.raises(RuntimeError, match="injected"):
        batch.run(tmp_path, tmp_path, _semantic_dir(), 0.05, False)
    assert _tree_hash(tmp_path) == before  # curated, quarantine and reports exactly as the last good run left them
    assert not (tmp_path / batch.STAGING).exists() or not any(p.is_file() for p in (tmp_path / batch.STAGING).rglob("*"))


def test_a_successful_run_leaves_no_staging_files(tmp_path: Path) -> None:
    shutil.copytree(ROOT / "data" / "synthetic", tmp_path / "synthetic")
    batch.run(tmp_path, tmp_path, _semantic_dir(), 0.05, False)
    stage = tmp_path / batch.STAGING
    assert not stage.exists() or not any(p.is_file() for p in stage.rglob("*"))


def _with_run_id(data_dir: Path, tmp_path: Path, when: datetime) -> Path:
    d = tmp_path / "d"
    shutil.copytree(data_dir, d)
    rep = json.loads((d / "reports" / "latest.json").read_text())
    rep["run_id"] = "run-" + when.strftime("%Y%m%dT%H%M%SZ")
    (d / "reports" / "latest.json").write_text(json.dumps(rep))
    return d


def test_ready_reports_stale_data_only_when_a_max_age_is_configured(settings: Settings, data_dir: Path, tmp_path: Path) -> None:
    old = _with_run_id(data_dir, tmp_path, datetime.now(UTC) - timedelta(hours=30))
    off = TestClient(create_app(replace(settings, data_dir=old)))
    assert off.get("/ready").status_code == 200  # default: freshness not checked
    on = TestClient(create_app(replace(settings, data_dir=old, data_max_age_s=24 * 3600)))
    r = on.get("/ready")
    assert r.status_code == 503 and "data_fresh" in r.json()["detail"]


def test_ready_passes_when_data_is_fresh_and_fails_without_a_report(settings: Settings, data_dir: Path, tmp_path: Path) -> None:
    fresh = _with_run_id(data_dir, tmp_path, datetime.now(UTC) - timedelta(minutes=5))
    assert TestClient(create_app(replace(settings, data_dir=fresh, data_max_age_s=3600))).get("/ready").status_code == 200
    (fresh / "reports" / "latest.json").unlink()
    assert TestClient(create_app(replace(settings, data_dir=fresh, data_max_age_s=3600))).get("/ready").status_code == 503


def test_responses_carry_the_id_of_the_data_load_they_were_served_from(client: TestClient, data_dir: Path) -> None:
    from tests.conftest import auth

    load_id = json.loads((data_dir / "reports" / "latest.json").read_text())["load_id"]
    r = client.get("/records/SHI-00002", headers=auth("dispatcher"))
    assert r.headers["x-data-load-id"] == load_id
    assert client.get("/health").headers["x-data-load-id"] == load_id


def test_rows_with_the_wrong_column_count_are_quarantined_not_a_crash(tmp_path: Path) -> None:
    shutil.copytree(ROOT / "data" / "synthetic", tmp_path / "synthetic")
    p = tmp_path / "synthetic" / "shipments.csv"
    lines = p.read_text(encoding="utf-8").splitlines()
    lines[10] = lines[10].rsplit(",", 3)[0]  # three trailing fields missing
    lines[11] = lines[11] + ",extra,extra"  # two extra fields
    lines[-1] = lines[-1][: len(lines[-1]) // 2]  # truncated last row
    p.write_text("\n".join(lines), encoding="utf-8")
    rep = batch.run(tmp_path, tmp_path, _semantic_dir(), 0.05, False)
    sh = rep["entities"]["shipments"]
    assert sh["processed"] == sh["curated"] + sh["quarantined"]
    assert sh["quarantine_by_rule"][batch.SHAPE_RULE] == 3
    q = [json.loads(x) for x in (tmp_path / "quarantine" / "shipments.jsonl").read_text().splitlines()]
    assert {x["source_row"] for x in q if batch.SHAPE_RULE in x["rules"]} == {10, 11, len(lines) - 1}
