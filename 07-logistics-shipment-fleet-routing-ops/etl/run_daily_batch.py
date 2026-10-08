"""Daily batch ETL (FR-06, FR-07, FR-08; F-33..F-41, F-54).

Reads the immutable fixture data/synthetic, validates every row against the semantic-layer rules, writes a curated
layer and a quarantine layer, and a per-run data-quality report. Exit code 1 when the quarantine ratio exceeds the
threshold (DQ-09). The fixture is never modified.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import os
import shutil
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from apps.api.config import _semantic_dir  # noqa: E402
from etl.validation import evaluate_entity, load_semantics  # noqa: E402

DEFAULT_THRESHOLD = 0.05
EXTRA = ["load_id", "source_row", "data_quality_flags"]
STAGING = ".staging"


SHAPE_RULE = "ROW-SHAPE"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]], set[int]]:
    """Rows as dicts, made safe for validation, plus the indexes of rows whose column count is wrong (M3 drill 5).

    csv.DictReader gives None for missing trailing fields and a list under key None for extra ones; either would crash
    the rule engine. Such a row is normalised (None -> "") and reported so that run() can quarantine it with ROW-SHAPE.
    """
    with path.open(newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh)
        header = list(rd.fieldnames or [])
        rows: list[dict[str, str]] = []
        bad: set[int] = set()
        for i, raw_row in enumerate(rd):
            if None in raw_row or any(v is None for v in raw_row.values()):
                bad.add(i)
            rows.append({k: ("" if v is None else v) for k, v in raw_row.items() if k is not None})
        return header, rows, bad


def input_hash(paths: list[Path]) -> str:
    h = hashlib.sha256()
    for p in sorted(paths):
        h.update(p.name.encode())
        h.update(hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()


def run(data_dir: Path, out_dir: Path, semantic_dir: Path, threshold: float, sample: bool) -> dict[str, Any]:
    """Run the batch; on any failure the staging area is removed and the published layers are left exactly as they were."""
    try:
        return _run(data_dir, out_dir, semantic_dir, threshold, sample)
    except BaseException:
        shutil.rmtree(out_dir / STAGING, ignore_errors=True)
        raise


def _run(data_dir: Path, out_dir: Path, semantic_dir: Path, threshold: float, sample: bool) -> dict[str, Any]:
    sem = load_semantics(semantic_dir)
    synth = data_dir / "synthetic"
    files = {e: synth / d["dataset"] for e, d in sem["entities"].items()}
    names = ("business-rules.yaml", "relationships.yaml", "status-taxonomy.yaml", "entities.yaml")
    rule_files = [semantic_dir / n for n in names]
    ih = input_hash(list(files.values()) + rule_files)
    load_id = "ld-" + ih[:12]
    raw: dict[str, tuple[list[str], list[dict[str, str]], set[int]]] = {e: read_csv(p) for e, p in files.items()}
    data = {e: rows for e, (_, rows, _bad) in raw.items()}
    # M3 (drill 5): outputs are written to a staging area first and published file by file with os.replace, so a
    # failure part-way through a run leaves the previously published layers untouched (no half-written mix).
    stage = out_dir / STAGING
    shutil.rmtree(stage, ignore_errors=True)
    cur_dir, q_dir, rep_dir = stage / "curated", stage / "quarantine", stage / "reports"
    for d in (cur_dir, q_dir, rep_dir):
        d.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "run_id": "run-" + datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ"),
        "load_id": load_id,
        "input_hash": ih,
        "sample": sample,
        "threshold": threshold,
        "entities": {},
    }
    total = bad = 0
    for ent, (header, rows, shape_bad) in raw.items():
        verdicts, counts, flag_counts = evaluate_entity(ent, rows, data, sem)
        for i in shape_bad:
            verdicts[i].rules_block.append(SHAPE_RULE)
        if shape_bad:
            counts[SHAPE_RULE] = len(shape_bad)
        cur_rows, q_rows = [], []
        for i, (r, v) in enumerate(zip(rows, verdicts, strict=True), start=1):
            if v.rules_block:
                q_rows.append(
                    {
                        "load_id": load_id,
                        "entity": ent,
                        "source_file": files[ent].name,
                        "source_row": i,
                        "rules": sorted(set(v.rules_block)),
                        "row": r,
                    }
                )
            else:
                cur_rows.append({**r, "load_id": load_id, "source_row": i, "data_quality_flags": ";".join(v.flags)})
        with (cur_dir / files[ent].name).open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=header + EXTRA, lineterminator="\n")
            w.writeheader()
            w.writerows(cur_rows)
        with (q_dir / (files[ent].stem + ".jsonl")).open("w", encoding="utf-8") as fh:
            for q in q_rows:
                fh.write(json.dumps(q, sort_keys=True) + "\n")
        total += len(rows)
        bad += len(q_rows)
        report["entities"][ent] = {
            "processed": len(rows),
            "curated": len(cur_rows),
            "quarantined": len(q_rows),
            "rule_offending_rows": counts,
            "flags": flag_counts,
            "quarantine_by_rule": dict(collections.Counter(x for q in q_rows for x in q["rules"])),
        }
    ship_rows = data["shipments"]
    legacy_malformed = sum(1 for r in ship_rows if any(v == "" for v in r.values()))
    multi = collections.Counter(
        r["shipment_id"] for r in data["carrier_bookings"] if r.get("status") not in ("closed", "failed") and r.get("shipment_id")
    )
    report["multiple_active_bookings"] = {k: n for k, n in multi.items() if n > 1}
    report["totals"] = {"processed": total, "quarantined": bad}
    report["quarantine_ratio"] = round(bad / total, 6) if total else 0.0
    report["status"] = "pass" if report["quarantine_ratio"] <= threshold else "fail"
    report["legacy_compat"] = {"processed": len(ship_rows), "malformed": legacy_malformed, "sample": sample}
    (rep_dir / f"etl-{load_id}.json").write_text(json.dumps(report, indent=1, sort_keys=True), encoding="utf-8")
    (rep_dir / "latest.json").write_text(json.dumps(report, indent=1, sort_keys=True), encoding="utf-8")
    publish(stage, out_dir)
    return report


def publish(stage: Path, out_dir: Path) -> None:
    """Move staged files into place. Data first, the report last, so a visible report implies the data it describes."""
    for sub in ("curated", "quarantine", "reports"):
        dest = out_dir / sub
        dest.mkdir(parents=True, exist_ok=True)
        for f in sorted((stage / sub).iterdir(), key=lambda p: p.name == "latest.json"):
            os.replace(f, dest / f.name)
    shutil.rmtree(stage, ignore_errors=True)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", action="store_true")
    ap.add_argument("--data-dir", type=Path, default=ROOT / "data")
    ap.add_argument("--out-dir", type=Path, default=None, help="default: same as --data-dir")
    ap.add_argument("--semantic-dir", type=Path, default=None)
    ap.add_argument("--max-quarantine-ratio", type=float, default=DEFAULT_THRESHOLD)
    a = ap.parse_args(argv)
    rep = run(a.data_dir, a.out_dir or a.data_dir, a.semantic_dir or _semantic_dir(), a.max_quarantine_ratio, a.sample)
    print(rep["legacy_compat"])  # backward-compatible first line (keys processed, malformed, sample)
    print(json.dumps({k: rep[k] for k in ("run_id", "load_id", "totals", "quarantine_ratio", "status")}))
    return 0 if rep["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
