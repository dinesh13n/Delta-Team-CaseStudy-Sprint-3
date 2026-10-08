# ruff: noqa: E501
"""Benefit, ROI and NPV model (runbook O3). An ASSUMPTION model, not a measurement: no verified improvement exists to price (O1/O2).

    python -m scripts.benefit_model --out ../evidence/36-benefits/EVD-O-03-benefit-model.json

Everything is expressed in analyst-hours so that no wage, price or currency has to be invented (OQ-09). Multiply by a labour rate when
one is supplied. Parameter values are ILLUSTRATIVE spread points chosen to show how the answer moves, not estimates of this business.
The model returns break-even values, which do not depend on the illustrative picks, alongside scenario results, which do.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

HORIZON_MONTHS = 36
ANNUAL_DISCOUNT = 0.10
BASE_VOLUME = 354  # AI-assisted exceptions per month at 1x: the fixture's invocation count used as a planning unit [ASM]

SCENARIOS: dict[str, dict[str, float]] = {
    # minutes_saved: review minutes saved per approved outcome (negative = the control adds time)
    "optimistic": {
        "volume_x": 10,
        "adoption": 0.80,
        "approval": 0.90,
        "minutes_saved": 5.0,
        "ops_hours_month": 16,
        "build_hours": 600,
    },
    "expected": {
        "volume_x": 1,
        "adoption": 0.50,
        "approval": 0.70,
        "minutes_saved": 2.0,
        "ops_hours_month": 16,
        "build_hours": 600,
    },
    "downside": {
        "volume_x": 1,
        "adoption": 0.20,
        "approval": 0.50,
        "minutes_saved": -1.0,
        "ops_hours_month": 40,
        "build_hours": 1200,
    },
}


def monthly_net_hours(p: dict[str, float]) -> float:
    outcomes = BASE_VOLUME * p["volume_x"] * p["adoption"] * p["approval"]
    return outcomes * p["minutes_saved"] / 60.0 - p["ops_hours_month"]


def npv(p: dict[str, float]) -> float:
    r = (1 + ANNUAL_DISCOUNT) ** (1 / 12) - 1
    net = monthly_net_hours(p)
    return float(-p["build_hours"] + sum(net / (1 + r) ** m for m in range(1, HORIZON_MONTHS + 1)))


def payback_months(p: dict[str, float]) -> float | None:
    net = monthly_net_hours(p)
    return None if net <= 0 else round(p["build_hours"] / net, 1)


def break_even_minutes(p: dict[str, float]) -> float | None:
    """Minutes saved per approved outcome at which monthly net hours = 0 (ignores the build cost)."""
    outcomes = BASE_VOLUME * p["volume_x"] * p["adoption"] * p["approval"]
    return None if outcomes == 0 else round(p["ops_hours_month"] * 60.0 / outcomes, 2)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    a = ap.parse_args()
    results = {
        n: {
            "parameters": p,
            "monthly_net_hours": round(monthly_net_hours(p), 1),
            "npv_hours_36m": round(npv(p), 1),
            "payback_months": payback_months(p),
            "break_even_minutes_saved": break_even_minutes(p),
            "roi_36m": round((monthly_net_hours(p) * HORIZON_MONTHS - p["build_hours"]) / p["build_hours"], 2),
        }
        for n, p in SCENARIOS.items()
    }
    base = SCENARIOS["expected"]
    sens: list[dict[str, Any]] = []
    for k, lo, hi in (
        ("minutes_saved", -1.0, 5.0),
        ("adoption", 0.2, 0.8),
        ("approval", 0.5, 0.9),
        ("volume_x", 1, 10),
        ("ops_hours_month", 8, 40),
        ("build_hours", 300, 1200),
    ):
        v_lo, v_hi = npv({**base, k: lo}), npv({**base, k: hi})
        sens.append(
            {
                "parameter": k,
                "low": lo,
                "high": hi,
                "npv_at_low": round(v_lo, 1),
                "npv_at_high": round(v_hi, 1),
                "swing": round(abs(v_hi - v_lo), 1),
            }
        )
    sens.sort(key=lambda r: -r["swing"])
    grid = []
    for vol in (1, 10, 100):
        for ms in (0.0, 1.0, 2.0, 5.0):
            p = {**base, "volume_x": vol, "minutes_saved": ms}
            grid.append(
                {
                    "volume_x": vol,
                    "minutes_saved": ms,
                    "monthly_net_hours": round(monthly_net_hours(p), 1),
                    "payback_months": payback_months(p),
                    "npv_hours_36m": round(npv(p), 1),
                }
            )
    out = {
        "run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "ASSUMPTION MODEL: no verified benefit exists (see EVD-O-01/O-02); parameters are illustrative",
        "unit": "analyst-hours (multiply by a labour rate when OQ-09 is answered)",
        "horizon_months": HORIZON_MONTHS,
        "annual_discount": ANNUAL_DISCOUNT,
        "base_volume_per_month": BASE_VOLUME,
        "scenarios": results,
        "sensitivity_on_expected": sens,
        "volume_vs_minutes_grid": grid,
        "excluded_to_avoid_double_counting": [
            "error-avoidance value counted only through minutes saved, not again as separate rework savings",
            "audit effort saved is NOT added: it is the same review time seen from the auditor's side and has no measured basis",
            "token cost: 271 tokens per request is below 0.001 analyst-hours at any plausible wage and is omitted",
        ],
        "not_modelled": [
            "revenue effects",
            "risk-reduction value (no loss data)",
            "the cost of the incident the controls prevent",
            "ongoing governance and compliance effort beyond ops_hours_month",
        ],
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    for n, r in results.items():
        print(
            n,
            "net h/mo",
            r["monthly_net_hours"],
            "npv h",
            r["npv_hours_36m"],
            "payback",
            r["payback_months"],
            "break-even min",
            r["break_even_minutes_saved"],
        )
    print("top sensitivities:", [(s["parameter"], s["swing"]) for s in sens[:3]])
    return 0


if __name__ == "__main__":
    sys.exit(main())
