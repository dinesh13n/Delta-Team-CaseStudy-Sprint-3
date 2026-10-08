# ruff: noqa: E501
"""Drift and continuous-evaluation check (runbook P3).

    python -m scripts.drift_check --reference evaluation/reference-data-profile.json --report data/reports/latest.json --audit logs/audit-v2.log --out out.json
    python -m scripts.drift_check --write-reference evaluation/reference-data-profile.json --report data/reports/latest.json

Exit code: 0 all clear, 1 INVESTIGATE (a person looks), 2 CHANGE-BLOCK (a prompt/model/evaluation guard failed: do not promote).
Checks: data profile against a reference; prompt and model locks; evaluation thresholds; runtime behaviour from the audit log.
Thresholds: evaluation/drift-thresholds.json (proposed, not tuned on production data).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from apps.api.ai import registry
from apps.api.config import ROOT

THRESHOLDS = ROOT / "evaluation" / "drift-thresholds.json"
OK, INVESTIGATE, BLOCK = "OK", "INVESTIGATE", "CHANGE-BLOCK"


def profile(report: dict[str, Any]) -> dict[str, Any]:
    ents = {}
    for name, e in report["entities"].items():
        n = max(1, e["processed"])
        ents[name] = {
            "processed": e["processed"],
            "quarantined": e["quarantined"],
            "flag_rates": {k: round(v / n, 4) for k, v in e["flags"].items()},
        }
    return {"load_id": report.get("load_id"), "quarantine_ratio": report["quarantine_ratio"], "entities": ents}


def data_drift(ref: dict[str, Any], cur: dict[str, Any], th: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    d_q = cur["quarantine_ratio"] - ref["quarantine_ratio"]
    if cur["quarantine_ratio"] > th["quarantine_ratio_hard_limit"]:
        out.append(
            {
                "check": "data.quarantine_ratio",
                "status": INVESTIGATE,
                "detail": f"{cur['quarantine_ratio']:.4f} above the contract limit {th['quarantine_ratio_hard_limit']}",
            }
        )
    elif d_q > th["quarantine_ratio_abs_increase_investigate"]:
        out.append({"check": "data.quarantine_ratio", "status": INVESTIGATE, "detail": f"rose {d_q:+.4f} from the reference"})
    else:
        out.append(
            {
                "check": "data.quarantine_ratio",
                "status": OK,
                "detail": f"{cur['quarantine_ratio']:.4f} (reference {ref['quarantine_ratio']:.4f})",
            }
        )
    for name, c in cur["entities"].items():
        r = ref["entities"].get(name)
        if r is None:
            out.append({"check": f"data.entity.{name}", "status": INVESTIGATE, "detail": "entity not in reference"})
            continue
        change = abs(c["processed"] - r["processed"]) / max(1, r["processed"])
        status, detail = (
            (INVESTIGATE, f"row count changed {change:.0%}")
            if change > th["entity_row_count_change_investigate"]
            else (OK, f"rows {c['processed']} (reference {r['processed']})")
        )
        new_flags = sorted(set(c["flag_rates"]) - set(r["flag_rates"]))
        moved = sorted(
            k
            for k in c["flag_rates"]
            if k in r["flag_rates"] and abs(c["flag_rates"][k] - r["flag_rates"][k]) > th["flag_rate_abs_change_investigate"]
        )
        if th["new_flag_investigate"] and new_flags:
            status, detail = INVESTIGATE, detail + f"; new flags {new_flags}"
        if moved:
            status, detail = INVESTIGATE, detail + f"; flag rate moved {moved}"
        out.append({"check": f"data.entity.{name}", "status": status, "detail": detail})
    return out


def lock_checks() -> list[dict[str, Any]]:
    out = []
    try:
        registry.load()
        out.append({"check": "prompt.lock", "status": OK, "detail": "prompt matches prompts.lock.json"})
    except registry.PromptIntegrityError as exc:
        out.append({"check": "prompt.lock", "status": BLOCK, "detail": str(exc)})
    try:
        for n, v in json.loads(registry.MODEL_LOCK_PATH.read_text(encoding="utf-8")).items():
            registry.verify_model(n, v)
        out.append({"check": "model.lock", "status": OK, "detail": "models.lock.json readable and self-consistent"})
    except (registry.PromptIntegrityError, OSError, ValueError) as exc:
        out.append({"check": "model.lock", "status": BLOCK, "detail": str(exc)})
    return out


def eval_check() -> dict[str, Any]:
    from evaluation.run_eval import run

    res = run(["golden", "edge", "adversarial", "failure"], "drift")
    return {
        "check": "evaluation.thresholds",
        "status": OK if res["overall"] == "PASS" else BLOCK,
        "detail": f"overall {res['overall']}, {len(res['failures'])} failing case(s) of {res['metrics']['cases_total']}",
    }


def runtime_drift(audit: Path, th: dict[str, Any]) -> list[dict[str, Any]]:
    events = [json.loads(x) for x in audit.read_text(encoding="utf-8").splitlines() if x.strip()] if audit.exists() else []
    ai = [e for e in events if e["action"] == "ai.summary"]
    dec = [e for e in events if e["action"] == "ai.decision"]
    leaks = sum(1 for e in ai if (e.get("detail") or {}).get("fallback_reason") == "output_policy_violation")
    out = [
        {
            "check": "runtime.leaks",
            "status": INVESTIGATE if leaks >= th["leak_events_investigate"] else OK,
            "detail": f"{leaks} blocked leak(s) in {len(ai)} AI events",
        }
    ]
    if len(ai) >= th["min_requests_for_rates"]:
        fb = sum(1 for e in ai if (e.get("detail") or {}).get("generated_by") == "fallback") / len(ai)
        out.append(
            {
                "check": "runtime.fallback_rate",
                "status": INVESTIGATE if fb > th["fallback_rate_investigate"] else OK,
                "detail": f"{fb:.1%}",
            }
        )
    else:
        out.append(
            {
                "check": "runtime.fallback_rate",
                "status": OK,
                "detail": f"only {len(ai)} AI events; below the {th['min_requests_for_rates']} needed for a rate",
            }
        )
    if len(dec) >= th["min_requests_for_rates"]:
        rj = sum(1 for e in dec if (e.get("detail") or {}).get("decision") == "reject") / len(dec)
        out.append(
            {
                "check": "runtime.reject_share",
                "status": INVESTIGATE if rj > th["reject_share_investigate"] else OK,
                "detail": f"{rj:.1%}",
            }
        )
    else:
        out.append(
            {
                "check": "runtime.reject_share",
                "status": OK,
                "detail": f"only {len(dec)} decisions; below the {th['min_requests_for_rates']} needed for a share",
            }
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", type=Path, default=ROOT / "data" / "reports" / "latest.json")
    ap.add_argument("--reference", type=Path, default=ROOT / "evaluation" / "reference-data-profile.json")
    ap.add_argument("--write-reference", type=Path, default=None)
    ap.add_argument("--audit", type=Path, default=None)
    ap.add_argument("--with-eval", action="store_true", help="also run the evaluation sets (about 30 s)")
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    report = json.loads(a.report.read_text(encoding="utf-8"))
    if a.write_reference:
        a.write_reference.write_text(json.dumps(profile(report), indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
        print("reference written:", a.write_reference)
        return 0
    th = json.loads(THRESHOLDS.read_text(encoding="utf-8"))
    results = data_drift(json.loads(a.reference.read_text(encoding="utf-8")), profile(report), th["data"]) + lock_checks()
    if a.with_eval:
        results.append(eval_check())
    if a.audit:
        results += runtime_drift(a.audit, th["runtime"])
    worst = (
        BLOCK
        if any(r["status"] == BLOCK for r in results)
        else INVESTIGATE
        if any(r["status"] == INVESTIGATE for r in results)
        else OK
    )
    out = {
        "run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "load_id": report.get("load_id"),
        "overall": worst,
        "results": results,
    }
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    for r in results:
        print(f"{r['status']:<13} {r['check']:<28} {r['detail']}")
    print("OVERALL", worst)
    return {OK: 0, INVESTIGATE: 1, BLOCK: 2}[worst]


if __name__ == "__main__":
    sys.exit(main())
