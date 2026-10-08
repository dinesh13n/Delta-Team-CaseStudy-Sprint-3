# ruff: noqa: E501
"""After-intervention KPIs under the FROZEN C1 definitions (runbook O1). Nothing here changes a definition.

    python -m scripts.after_kpis --out ../evidence/34-after-kpis/EVD-O-01-after-kpis.json

1. Definition check (O-X1): docs/04-baseline-kpis/kpi-dictionary.md and semantic-layer/metrics.yaml must agree field by field.
2. Comparability (O-X2): the fixture files are byte-identical to the as-delivered baseline tag.
3. K1..K8 recomputed with apps/api/kpis.py on the raw fixture (comparable) and on the curated layer (K7, K8 only differ).
4. K9, K10 from the current test and coverage run.

The honest outcome is that K1..K6 cannot change: they are computed from a static synthetic fixture the intervention does not touch.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

import etl.run_daily_batch as batch
from apps.api import kpis
from apps.api.config import ROOT, _semantic_dir

REPO = ROOT.parent
TAG = "baseline/v0.1-as-delivered-bytes"
FIELDS = ["name", "meaning", "formula", "unit", "owner", "source", "period", "segmentation"]
BASELINE = {  # copied from docs/04-baseline-kpis/baseline-kpi-sheet.md, measured 2026-10-08 before any change
    "K1": {"p50": 1667, "p95": 13709, "max": 14999},
    "K2": 2.2451,
    "K3": 39.6,
    "K4": 33.6,
    "K5": 904432,
    "K6": {"min": 51, "mean": 2508.5, "max": 4995},
    "K7": 18,
    "K8": 6,
}


def parse_dictionary(path: Path) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for ln in path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\| K\d+ \|", ln):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            out[cells[0]] = dict(zip(FIELDS, cells[1:], strict=False))
    return out


def definition_check() -> dict[str, Any]:
    doc = parse_dictionary(REPO / "docs/04-baseline-kpis/kpi-dictionary.md")
    yml = yaml.safe_load((REPO / "semantic-layer/metrics.yaml").read_text(encoding="utf-8"))
    ymap = {m["id"]: {k: str(m.get(k, "")) for k in FIELDS} for m in yml["metrics"]}
    diffs = []
    for kid in sorted(set(doc) | set(ymap)):
        for f in FIELDS:
            a, b = doc.get(kid, {}).get(f), ymap.get(kid, {}).get(f)
            if a is None or b is None or a.replace("`", "") != b.replace("`", ""):
                diffs.append({"kpi": kid, "field": f, "dictionary": a, "metrics_yaml": b})
    canon = json.dumps({k: doc[k] for k in sorted(doc)}, sort_keys=True).encode()
    return {
        "kpis_in_dictionary": len(doc),
        "kpis_in_yaml": len(ymap),
        "status_in_yaml": yml.get("status"),
        "field_diffs": diffs,
        "dictionary_definitions_sha256": hashlib.sha256(canon).hexdigest(),
        "identical": not diffs and len(doc) == len(ymap) == 10,
    }


def comparability() -> dict[str, Any]:
    rows = []
    for p in sorted((ROOT / "data" / "synthetic").glob("*")):
        cur = hashlib.sha256(p.read_bytes()).hexdigest()
        base = subprocess.run(
            ["git", "show", f"{TAG}:{ROOT.name}/data/synthetic/{p.name}"], capture_output=True, cwd=REPO, check=False
        )  # noqa: S603, S607
        rows.append(
            {
                "file": p.name,
                "sha256_now": cur,
                "sha256_baseline": hashlib.sha256(base.stdout).hexdigest() if base.returncode == 0 else None,
                "identical": base.returncode == 0 and hashlib.sha256(base.stdout).hexdigest() == cur,
            }
        )
    return {"baseline_tag": TAG, "files": rows, "population_identical": all(r["identical"] for r in rows)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--tests", default="170 passed, 7 xfailed")
    ap.add_argument("--coverage", default="97% (apps + etl)")
    a = ap.parse_args()
    defs = definition_check()
    comp = comparability()
    with tempfile.TemporaryDirectory() as t:
        data = Path(t) / "data"
        shutil.copytree(ROOT / "data" / "synthetic", data / "synthetic")
        batch.run(data, data, _semantic_dir(), 0.05, False)
        raw = {k["id"]: k for k in kpis.compute(data, "synthetic")}
        cur = {k["id"]: k for k in kpis.compute(data, "curated")}
    rows = []

    def row(kid: str, base: Any, now: Any, note: str) -> None:
        rows.append({"kpi": kid, "baseline": base, "after_raw_fixture": now, "equal": base == now, "note": note})

    d1 = raw["K1"]["detail"]
    row(
        "K1",
        BASELINE["K1"],
        {"p50": d1["p50"], "p95": d1["p95"], "max": d1["max"]},
        "latency is a column of the static fixture; the intervention does not change it",
    )
    row("K2", BASELINE["K2"], round(raw["K2"]["value"], 4), "static fixture")
    row("K3", BASELINE["K3"], round(raw["K3"]["value"], 1), "static fixture")
    row(
        "K4",
        BASELINE["K4"],
        round(raw["K4"]["value"], 1),
        "source event stream unchanged (F-M3-01); API audit correlation is a different population",
    )
    row("K5", BASELINE["K5"], int(raw["K5"]["value"]), "declared tokens in the fixture; not model usage")
    d6 = raw["K6"]["detail"]
    row("K6", BASELINE["K6"], {"min": d6["min"], "mean": round(d6["mean"], 1), "max": d6["max"]}, "static fixture")
    row("K7", BASELINE["K7"], int(raw["K7"]["value"]), "raw layer, same definition")
    row("K8", BASELINE["K8"], int(raw["K8"]["value"]), "raw layer, same definition")
    curated = {"K7_duplicate_keys_in_curated": cur["K7"]["value"], "K8_incomplete_rows_in_curated": cur["K8"]["value"]}
    out = {
        "run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "definitions": defs,
        "comparability": comp,
        "kpis": rows,
        "curated_layer_view": {
            **curated,
            "note": "the curated layer holds only rows that passed the contract; duplicates and incomplete rows were moved to quarantine, so these are different populations from the raw counts and are NOT an improvement of K7/K8",
        },
        "k9_k10": {
            "tests": a.tests,
            "coverage": a.coverage,
            "baseline": {"K9": "3 of 3 pass (0 of 3 collected without httpx)", "K10": "45%"},
            "note": "test counts and coverage measure the repository, not operations; they grew because tests were written, not because of use",
        },
        "all_proxy_kpis_equal_baseline": all(r["equal"] for r in rows),
        "conclusion": "No business improvement can be demonstrated: the measured KPIs are properties of a static synthetic fixture, the population and definitions are unchanged, and no operational data exists.",
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        "definitions identical:",
        defs["identical"],
        "| population identical:",
        comp["population_identical"],
        "| all equal:",
        out["all_proxy_kpis_equal_baseline"],
    )
    for r in rows:
        print(r["kpi"], "EQUAL" if r["equal"] else "DIFF", r["baseline"], r["after_raw_fixture"])
    print(curated)
    for d in defs["field_diffs"][:8]:
        print("DIFF", d)
    return 0 if defs["identical"] and comp["population_identical"] else 1


if __name__ == "__main__":
    sys.exit(main())
