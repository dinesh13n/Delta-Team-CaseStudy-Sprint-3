# ruff: noqa: E501
"""FinOps measurements and estimate model (runbook N4). MEASURES what the running system produces per request (tokens estimate,
audit bytes, metric series, response bytes) over every shipment in the fixture, then applies VOLUME scenarios and PRICE parameters.

    python -m scripts.finops_estimate --out ../evidence/32-finops/EVD-N-04-finops-model.json

No model price is known or quoted. Prices enter only as symbolic parameters and as clearly labelled illustrative sensitivity points.
Token numbers are the gateway's own character-based estimate: no provider was called, so no billed usage exists.
"""

from __future__ import annotations

import argparse
import json
import shutil
import statistics
import sys
import tempfile
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from fastapi.testclient import TestClient

import etl.run_daily_batch as batch
from apps.api.config import ROOT, Settings, _semantic_dir
from apps.api.main import create_app
from apps.api.security.tokens import issue_dev_token

SECRET = "finops-secret-" + "x" * 40  # secret-scan: allow (throw-away value for an in-process run)
VOLUMES = {"1x (354 per period)": 354, "10x": 3540, "100x": 35400}
ILLUSTRATIVE_USD_PER_MTOK = (
    1.0,
    5.0,
    15.0,
)  # NOT quotes: spread points so the owner can see the order of magnitude once a model is chosen
REVIEW_SHARE = {"all suggestions reviewed": 1.0, "half reviewed": 0.5}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        data = tmp / "data"
        shutil.copytree(ROOT / "data" / "synthetic", data / "synthetic")
        batch.run(data, data, _semantic_dir(), 0.05, False)
        st = Settings(
            app_env="local",
            auth_mode="hs256",
            auth_secret=SECRET,
            data_dir=data,
            audit_path=tmp / "audit.log",
            approvals_path=tmp / "approvals.jsonl",
            semantic_dir=_semantic_dir(),
            ai_rate_per_minute=100000,
        )
        c = TestClient(create_app(st))
        h = {"Authorization": "Bearer " + issue_dev_token(SECRET, "alice", "dispatcher", ttl=3600)}
        ids = sorted(
            {ln.split(",")[0] for ln in (data / "curated" / "shipments.csv").read_text(encoding="utf-8").splitlines()[1:] if ln}
        )
        toks: list[int] = []
        resp_bytes: list[int] = []
        by_producer: dict[str, int] = {}
        t0 = time.perf_counter()
        for sid in ids:
            r = c.post(f"/ai/summarize/{sid}", headers=h)
            if r.status_code != 200:
                continue
            j = r.json()
            toks.append(int(j["token_estimate"]))
            resp_bytes.append(len(r.content))
            by_producer[j["generated_by"]] = by_producer.get(j["generated_by"], 0) + 1
        wall = time.perf_counter() - t0
        audit_bytes = st.audit_path.stat().st_size
        audit_events = len(st.audit_path.read_text(encoding="utf-8").splitlines())
        appr_bytes = st.approvals_path.stat().st_size
        metrics_text = c.get(
            "/metrics", headers={"Authorization": "Bearer " + issue_dev_token(SECRET, "oncall", "ops", ttl=3600)}
        ).text
        series = sum(1 for ln in metrics_text.splitlines() if ln and not ln.startswith("#"))
        n = len(toks)
        mean_tok = statistics.mean(toks)
        per_req = {
            "requests_measured": n,
            "tokens_est_mean": round(mean_tok, 1),
            "tokens_est_p95": sorted(toks)[int(0.95 * n)],
            "tokens_est_max": max(toks),
            "response_bytes_mean": round(statistics.mean(resp_bytes), 1),
            "by_producer": by_producer,
        }
        storage = {
            "audit_bytes_per_ai_request": round(audit_bytes / max(1, n), 1),
            "audit_events": audit_events,
            "audit_bytes_total": audit_bytes,
            "approval_bytes_per_ai_request": round(appr_bytes / max(1, n), 1),
            "metric_series_exposed": series,
        }
        scen: list[dict[str, Any]] = []
        for vname, v in VOLUMES.items():
            row: dict[str, Any] = {
                "volume": vname,
                "ai_requests_per_period": v,
                "tokens_per_period_est": round(v * mean_tok),
                "audit_mb_per_period": round(v * storage["audit_bytes_per_ai_request"] / 1e6, 2),
            }
            row["usd_per_period_at_illustrative_usd_per_million_tokens"] = {
                str(p): round(v * mean_tok * p / 1e6, 4) for p in ILLUSTRATIVE_USD_PER_MTOK
            }
            scen.append(row)
        out = {
            "run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "basis": "every shipment id in the fixture summarised once with the deterministic provider; no model called; token numbers are len/4 estimates",
            "measured_per_request": per_req,
            "measured_storage_and_telemetry": storage,
            "wall_seconds_for_all_requests": round(wall, 2),
            "envelope_from_A6": {
                "tokens_typical_max": 3000,
                "tokens_hard_cap": 5000,
                "baseline_mean_tokens_per_request": 2562,
                "baseline_cost_units_per_request": 2.245,
            },
            "within_envelope": {"mean_vs_typical": mean_tok <= 3000, "max_vs_hard_cap": max(toks) <= 5000},
            "scenarios": scen,
            "review_share_scenarios": REVIEW_SHARE,
            "price_note": "prices are parameters, not facts: the three USD-per-million-token points are illustrative spread values, not quotes from any provider; a real model changes input/output split, adds a system prompt and may use more tokens than this estimate",
            "not_included": [
                "model price, input/output split, caching",
                "compute, storage and network of any platform (none exists)",
                "human review time (largest real cost, unmeasured)",
                "evaluation and red-team runs",
                "engineering and operations effort",
            ],
        }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"per_request": per_req, "storage": storage, "within": out["within_envelope"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
