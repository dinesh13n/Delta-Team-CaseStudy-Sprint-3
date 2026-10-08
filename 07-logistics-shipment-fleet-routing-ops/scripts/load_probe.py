"""Small load probe (runbook M2 capacity plan, N1 SLO baselines).

    python -m scripts.load_probe --base-url http://127.0.0.1:8803 --token <dispatcher token> \
        --out evidence/28-resilience/EVD-M-02-load-probe.json

It measures one process on one machine with the deterministic provider: it is a sanity check of the order of magnitude, not a
capacity test of a deployment. Numbers say nothing about a real model, a network or another host.
"""

from __future__ import annotations

import argparse
import json
import statistics
import threading
import time
from pathlib import Path
from typing import Any

import httpx


def pct(values: list[float], q: float) -> float:
    s = sorted(values)
    return round(s[min(len(s) - 1, int(q * len(s)))], 2)


def probe(base: str, token: str, name: str, method: str, path: str, total: int, workers: int) -> dict[str, Any]:
    lat: list[float] = []
    codes: dict[int, int] = {}
    lock = threading.Lock()
    per = total // workers

    def work() -> None:
        with httpx.Client(base_url=base, timeout=20, headers={"Authorization": f"Bearer {token}"}) as c:
            for _ in range(per):
                t0 = time.perf_counter()
                r = c.request(method, path)
                dt = (time.perf_counter() - t0) * 1000
                with lock:
                    lat.append(dt)
                    codes[r.status_code] = codes.get(r.status_code, 0) + 1

    ts = [threading.Thread(target=work) for _ in range(workers)]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    wall = time.perf_counter() - t0
    return {
        "name": name,
        "request": f"{method} {path}",
        "workers": workers,
        "requests": len(lat),
        "status_codes": codes,
        "wall_s": round(wall, 2),
        "throughput_rps": round(len(lat) / wall, 1),
        "latency_ms": {
            "p50": pct(lat, 0.5),
            "p95": pct(lat, 0.95),
            "p99": pct(lat, 0.99),
            "max": round(max(lat), 2),
            "mean": round(statistics.mean(lat), 2),
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--token", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--requests", type=int, default=400)
    a = ap.parse_args()
    runs = []
    for workers in (1, 8):
        runs.append(
            probe(a.base_url, a.token, f"record lookup, {workers} worker(s)", "GET", "/records/SHI-00027", a.requests, workers)
        )
        runs.append(
            probe(
                a.base_url,
                a.token,
                f"shipment list page, {workers} worker(s)",
                "GET",
                "/shipments?limit=100",
                a.requests,
                workers,
            )
        )
        runs.append(
            probe(
                a.base_url,
                a.token,
                f"AI summary (deterministic), {workers} worker(s)",
                "POST",
                "/ai/summarize/SHI-00027",
                a.requests,
                workers,
            )
        )
    out = {
        "note": "one uvicorn process, loopback, deterministic provider, 354 rows per entity; not a deployment capacity test",
        "run_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "runs": runs,
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    for r in runs:
        print(r["name"], r["status_codes"], r["throughput_rps"], "rps", r["latency_ms"])


if __name__ == "__main__":
    main()
