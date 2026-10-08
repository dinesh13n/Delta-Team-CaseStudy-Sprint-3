"""Saga simulation (J5 evidence).

Replays a retry-storm and duplicate-request workload against the saga with a flaky simulated carrier.

python -m scripts.saga_simulation --out evidence/21-integration/EVD-J-05-saga-simulation.json
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from collections import Counter
from pathlib import Path

from apps.api.config import ROOT
from apps.api.integration.carrier_saga import BookingStore, CarrierSaga, InFlightError, SagaConfig, SimulatedCarrier


def baseline_from_data() -> dict[str, int | None]:
    p = ROOT / "data" / "synthetic" / "carrier_bookings.csv"
    with p.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    retries = []
    for r in rows:
        try:
            retries.append(int(float(r["retry_count"])))
        except (ValueError, KeyError):
            continue
    keys = Counter(r["booking_id"] for r in rows if r.get("booking_id"))
    return {
        "rows": len(rows),
        "max_retry_count": max(retries) if retries else None,
        "duplicate_booking_ids": sum(1 for v in keys.values() if v > 1),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--requests", type=int, default=1000)
    a = ap.parse_args()
    rng = random.Random(20261008)  # noqa: S311
    carrier = SimulatedCarrier(p_transient=0.35, rng=random.Random(11))  # noqa: S311
    saga = CarrierSaga(carrier, BookingStore(), SagaConfig(max_attempts=3), sleep=lambda _s: None)
    shipments = [f"SHI-{i:05d}" for i in range(1, 401)]
    states: Counter[str] = Counter()
    in_flight = suppressed = 0
    attempts_max = 0
    for _ in range(a.requests):
        sid = rng.choice(shipments)  # 1000 requests over 400 shipments: many repeats
        try:
            o = saga.book(sid, "CarrierX")
        except InFlightError:
            in_flight += 1
            continue
        states[o.state] += 1
        suppressed += int(o.duplicate_suppressed)
        attempts_max = max(attempts_max, o.attempts)
    per_ship = Counter(carrier.live.values())
    result = {
        "run_note": "deterministic simulation with a scripted flaky carrier; no real carrier was called",
        "requests": a.requests,
        "unique_shipments_requested": len({s for s in shipments}),
        "outcomes_by_state": dict(states),
        "duplicate_requests_suppressed": suppressed,
        "carrier_book_calls": carrier.calls,
        "live_bookings_at_carrier": len(carrier.live),
        "shipments_with_more_than_one_live_booking": sum(1 for v in per_ship.values() if v > 1),
        "max_attempts_for_any_booking": attempts_max,
        "configured_max_attempts": 3,
        "hard_retry_ceiling": 5,
        "baseline_in_fixture": baseline_from_data(),
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
