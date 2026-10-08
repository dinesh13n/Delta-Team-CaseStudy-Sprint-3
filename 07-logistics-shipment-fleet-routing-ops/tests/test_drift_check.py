"""P3: the drift check distinguishes 'all clear', 'a person should look' and 'do not promote'."""

import json
from pathlib import Path

import pytest

from apps.api.ai import registry
from scripts import drift_check as dc


def _report(data_dir: Path) -> dict:  # type: ignore[type-arg]
    return json.loads((data_dir / "reports" / "latest.json").read_text(encoding="utf-8"))


def test_identical_profile_is_clear(data_dir: Path) -> None:
    rep = _report(data_dir)
    res = dc.data_drift(dc.profile(rep), dc.profile(rep), json.loads(dc.THRESHOLDS.read_text())["data"])
    assert {r["status"] for r in res} == {dc.OK}


def test_quarantine_jump_and_new_flag_and_row_loss_are_flagged(data_dir: Path) -> None:
    rep = _report(data_dir)
    ref = dc.profile(rep)
    bad = json.loads(json.dumps(rep))
    bad["quarantine_ratio"] = 0.12
    first = next(iter(bad["entities"]))
    bad["entities"][first]["flags"]["enum_violation:brand_new_field"] = 5
    bad["entities"][first]["processed"] = int(bad["entities"][first]["processed"] * 0.5)
    res = dc.data_drift(ref, dc.profile(bad), json.loads(dc.THRESHOLDS.read_text())["data"])
    by = {r["check"]: r for r in res}
    assert by["data.quarantine_ratio"]["status"] == dc.INVESTIGATE
    assert by[f"data.entity.{first}"]["status"] == dc.INVESTIGATE and "brand_new_field" in by[f"data.entity.{first}"]["detail"]


def test_prompt_change_blocks(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    (tmp_path / "exception_summary_v1.txt").write_text("changed", encoding="utf-8")
    monkeypatch.setattr(registry, "PROMPT_DIR", tmp_path)
    assert {r["check"]: r["status"] for r in dc.lock_checks()}["prompt.lock"] == dc.BLOCK


def test_runtime_leak_and_fallback_rate(tmp_path: Path) -> None:
    ev = [
        {"action": "ai.summary", "detail": {"generated_by": "fallback", "fallback_reason": "output_policy_violation"}}
        for _ in range(40)
    ]
    p = tmp_path / "a.log"
    p.write_text("\n".join(json.dumps(e) for e in ev), encoding="utf-8")
    res = {r["check"]: r["status"] for r in dc.runtime_drift(p, json.loads(dc.THRESHOLDS.read_text())["runtime"])}
    assert res["runtime.leaks"] == dc.INVESTIGATE and res["runtime.fallback_rate"] == dc.INVESTIGATE
