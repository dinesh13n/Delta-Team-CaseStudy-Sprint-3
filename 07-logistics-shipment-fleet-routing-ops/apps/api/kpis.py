"""KPI K1..K10 per semantic-layer/metrics.yaml (frozen definitions). K9, K10 are test-run results, not runtime data."""

from __future__ import annotations

import contextlib
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


def _pct(sorted_vals: list[float], p: float) -> float:
    return sorted_vals[min(int(p / 100 * len(sorted_vals)), len(sorted_vals) - 1)]


def compute(data_dir: Path, layer: str) -> list[dict[str, Any]]:
    synth = data_dir / "synthetic"
    events = [json.loads(line) for line in (synth / "events.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    lat = sorted(float(e["latency_ms"]) for e in events)
    out: list[dict[str, Any]] = [
        {
            "id": "K1",
            "name": "Event latency (p95)",
            "value": _pct(lat, 95),
            "detail": {"p50": _pct(lat, 50), "p95": _pct(lat, 95), "max": lat[-1]},
        },
        {"id": "K2", "name": "Cost per event", "value": sum(float(e["cost_units"]) for e in events) / len(events)},
        {
            "id": "K3",
            "name": "Severe-event share (%)",
            "value": 100 * sum(1 for e in events if e["severity"] in ("error", "critical")) / len(events),
        },
        {
            "id": "K4",
            "name": "Correlation completeness (%)",  # amended D-012: non-null AND non-empty
            "value": 100 * sum(1 for e in events if e.get("correlation_id")) / len(events),
            "detail": {"non_null_pct": 100 * sum(1 for e in events if e.get("correlation_id") is not None) / len(events)},
        },
    ]
    tokens = 0
    with (synth / "ai_invocations.csv").open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            with contextlib.suppress(ValueError, KeyError):
                tokens += int(r["token_count"])
    out.append({"id": "K5", "name": "Declared AI tokens", "value": float(tokens)})
    retries: list[float] = []
    with (synth / "carrier_bookings.csv").open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            with contextlib.suppress(ValueError, KeyError):
                retries.append(float(r["retry_count"]))
    out.append(
        {
            "id": "K6",
            "name": "Carrier retry level (max)",
            "value": max(retries) if retries else None,
            "detail": {"min": min(retries), "mean": sum(retries) / len(retries), "max": max(retries)} if retries else {},
        }
    )
    base = data_dir / ("curated" if layer == "curated" else "synthetic")
    dups = blanks = 0
    for p in sorted(base.glob("*.csv")):
        with p.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
        header, body = rows[0], rows[1:]
        keep = [i for i, h in enumerate(header) if h not in ("load_id", "source_row", "data_quality_flags")]
        keys = Counter(r[0] for r in body if r)
        dups += sum(1 for n in keys.values() if n > 1)
        blanks += sum(1 for r in body if any(not r[i].strip() for i in keep if i < len(r)))
    out.append({"id": "K7", "name": "Duplicate business keys", "value": float(dups), "detail": {"layer": layer}})
    out.append({"id": "K8", "name": "Incomplete rows", "value": float(blanks), "detail": {"layer": layer}})
    out.append({"id": "K9", "name": "Baseline test result", "value": None, "data_gap": True})
    out.append({"id": "K10", "name": "Baseline coverage", "value": None, "data_gap": True})
    return out
