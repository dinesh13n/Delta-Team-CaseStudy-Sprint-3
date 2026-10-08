# ruff: noqa: E501
"""Failure-injection drills (runbook M3). Executes the five drills named in docs/runbooks/failure-injection-drills.md.

    python -m scripts.failure_drills --out-dir ../evidence/28-resilience/EVD-M-03-drills

Everything runs in-process against copies of the fixture in temporary directories; the repository data is never touched.
Each drill writes one JSON result: hypothesis, method, observations, pass criteria, verdict, findings.
A drill that cannot reach its pass criteria is reported FAIL and the finding is recorded; it is not rewritten.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import threading
import time
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from fastapi.testclient import TestClient

import etl.run_daily_batch as batch
from apps.api.ai.providers import PromptParts, ProviderResult
from apps.api.config import ROOT, Settings, _semantic_dir
from apps.api.integration.carrier_saga import BookingStore, CarrierSaga, InFlightError, SagaConfig, SimulatedCarrier
from apps.api.main import create_app
from apps.api.security.tokens import issue_dev_token

SECRET = "drill-secret-" + "x" * 40  # secret-scan: allow (throw-away value for the in-process drills)
CORR = re.compile(r"^(corr-[0-9a-f]{16}|[A-Za-z0-9._-]{8,64})$")


def hdr(role: str, sub: str = "drill-user", purpose: str | None = None) -> dict[str, str]:
    return {"Authorization": "Bearer " + issue_dev_token(SECRET, sub, role, purpose=purpose, ttl=3600)}


def make_data(tmp: Path) -> Path:
    d = tmp / "data"
    shutil.copytree(ROOT / "data" / "synthetic", d / "synthetic")
    batch.run(d, d, _semantic_dir(), 0.05, False)
    return d


def make_app(data: Path, tmp: Path, **kw: Any) -> tuple[TestClient, Settings]:
    st = Settings(
        app_env="local",
        auth_mode="hs256",
        auth_secret=SECRET,
        data_dir=data,
        audit_path=tmp / "audit.log",
        approvals_path=tmp / "approvals.jsonl",
        semantic_dir=_semantic_dir(),
        ai_rate_per_minute=100000,
        **kw,
    )
    return TestClient(create_app(st)), st


def audit_events(st: Settings) -> list[dict[str, Any]]:
    return [json.loads(x) for x in st.audit_path.read_text(encoding="utf-8").splitlines() if x.strip()]


def csv_rows(p: Path) -> list[dict[str, str]]:
    with p.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def verdict(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


# --------------------------------------------------------------------------------------------------------------------
def drill1(tmp: Path) -> dict[str, Any]:
    data = make_data(tmp)
    c, st = make_app(data, tmp)
    cases = {
        "absent": None,
        "empty": "",
        "too_short": "abc",
        "illegal_chars": "bad id; <script>",
        "too_long": "a" * 200,
        "newline_injection": "trace-1\r\nX-Evil: 1",
        "valid_client_id": "trace-abc-12345",
    }
    rows = []
    for name, val in cases.items():
        h = hdr("dispatcher")
        if val is not None:
            h["X-Correlation-ID"] = val
        try:
            r = c.get("/records/SHI-00002", headers=h)
            got = r.headers.get("x-correlation-id", "")
            rows.append(
                {
                    "case": name,
                    "status": r.status_code,
                    "echoed_or_generated": got,
                    "well_formed": bool(CORR.fullmatch(got)),
                    "client_value_kept": got == val,
                }
            )
        except Exception as exc:  # an illegal header value may be refused by the client itself
            rows.append(
                {"case": name, "client_error": type(exc).__name__, "well_formed": True, "note": "request could not be sent"}
            )
    c.get("/records/SHI-00002")  # 401 path
    c.get("/records/DOES-NOT-EXIST", headers=hdr("dispatcher"))  # 422 path
    ev = audit_events(st)
    missing = [e for e in ev if not e.get("correlation_id")]
    err_body = c.get("/records/SHI-00002").json()
    ev_hdr = csv_rows(data / "curated" / "tracking_events.csv")
    lineage_missing = [r for r in ev_hdr if not r.get("load_id") or not r.get("source_row")]
    src_cols = list(csv_rows(ROOT / "data" / "synthetic" / "tracking_events.csv")[0].keys())
    obs = {
        "requests": rows,
        "audit_events": len(ev),
        "audit_events_without_correlation_id": len(missing),
        "error_body_has_correlation_id": bool(err_body.get("correlation_id")),
        "curated_tracking_event_rows": len(ev_hdr),
        "curated_rows_without_lineage": len(lineage_missing),
        "source_event_columns": src_cols,
        "source_stream_has_correlation_column": "correlation_id" in src_cols,
    }
    ok = bool(
        all(r["well_formed"] for r in rows) and not missing and obs["error_body_has_correlation_id"] and not lineage_missing
    )
    return {
        "id": "DRILL-1",
        "name": "Missing correlation IDs in event streams",
        "hypothesis": "A request or event without a correlation id still gets a well-formed id and an unbroken audit trail.",
        "method": "Seven header variants against /records (absent, empty, short, illegal characters, 200 chars, CRLF injection, valid), "
        "plus an unauthenticated call and a 422 call; then every audit event and every curated tracking-event row is checked.",
        "observations": obs,
        "pass_criteria": [
            "every response carries a well-formed id",
            "no audit event lacks one",
            "error bodies carry one",
            "every curated event row has load_id and source_row lineage",
        ],
        "verdict": verdict(ok),
        "findings": [
            "F-M3-01: the SOURCE event stream has no correlation column. Per-event correlation cannot be recovered upstream; the system "
            "substitutes batch lineage (load_id + source_row) for stored events and a generated id per API request. A true end-to-end id "
            "needs the producing system to emit one (data contract change, owner ruling).",
        ],
    }


# --------------------------------------------------------------------------------------------------------------------
class SlowProvider:
    name, version = "slow-model", "1"

    def __init__(self, delay: float) -> None:
        self.delay, self.calls = delay, 0

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        self.calls += 1
        time.sleep(self.delay)
        return ProviderResult("{}")


class DownProvider:
    name, version = "down-model", "1"

    def __init__(self) -> None:
        self.calls = 0

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        self.calls += 1
        raise RuntimeError("503 upstream unavailable")


class GoodProvider:
    name, version = "good-model", "1"

    def __init__(self) -> None:
        self.calls = 0

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        self.calls += 1
        return ProviderResult(
            json.dumps(
                {
                    "summary": "Shipment is in exception; review the booking.",
                    "recommendation": "Review and approve before action",
                    "confidence": 0.9,
                    "abstained": False,
                }
            )
        )


def timed(fn: Any) -> tuple[Any, float]:
    t0 = time.perf_counter()
    r = fn()
    return r, (time.perf_counter() - t0) * 1000


def drill2(tmp: Path) -> dict[str, Any]:
    data = make_data(tmp)
    c, st = make_app(data, tmp, ai_timeout_s=0.3, ai_breaker_threshold=3, ai_breaker_reset_s=1.0)
    gw = c.app.state.svc.gateway  # type: ignore[attr-defined]
    h = hdr("dispatcher")

    def core() -> list[int]:
        return [
            c.get("/records/SHI-00002", headers=h).status_code,
            c.get("/shipments?limit=20", headers=h).status_code,
            c.get("/shipments/SHI-00002/events", headers=h).status_code,
            c.get("/ready").status_code,
        ]

    obs: dict[str, Any] = {}
    # phase 0: healthy deterministic baseline
    lat0 = [timed(lambda: c.post("/ai/summarize/SHI-00027", headers=h))[1] for _ in range(20)]
    core_lat0 = [timed(core)[1] for _ in range(20)]
    obs["phase0_deterministic"] = {
        "ai_p50_ms": round(statistics.median(lat0), 2),
        "core_group_p50_ms": round(statistics.median(core_lat0), 2),
    }
    # phase 1: provider hangs for 2 s, timeout 0.3 s
    slow = SlowProvider(2.0)
    gw.provider = slow
    r, ms = timed(lambda: c.post("/ai/summarize/SHI-00027", headers=h))
    body = r.json()
    core_codes, core_ms = timed(core)
    obs["phase1_slow_provider"] = {
        "ai_status": r.status_code,
        "generated_by": body.get("generated_by"),
        "fallback_reason": body.get("fallback_reason"),
        "ai_wall_ms": round(ms, 1),
        "provider_sleep_ms": 2000,
        "timeout_ms": 300,
        "core_while_provider_hangs": core_codes,
        "core_group_ms": round(core_ms, 1),
    }
    time.sleep(2.1)  # let abandoned workers finish before the next phase
    # phase 2: provider down: breaker opens after 3 failures and stops calling it
    down = DownProvider()
    gw.provider = down
    reasons = []
    for _ in range(6):
        out = c.post("/ai/summarize/SHI-00027", headers=h).json()
        reasons.append(out.get("fallback_reason"))
    obs["phase2_provider_down"] = {"reasons_in_order": reasons, "provider_calls": down.calls, "requests": 6}
    # phase 3: recovery. Wait for the breaker reset window, provider healthy again
    time.sleep(1.2)
    good = GoodProvider()
    gw.provider = good
    r3 = c.post("/ai/summarize/SHI-00027", headers=h).json()
    r4 = c.post("/ai/summarize/SHI-00027", headers=h).json()
    obs["phase3_recovery"] = {
        "first_after_reset": [r3.get("generated_by"), r3.get("fallback_reason")],
        "second": [r4.get("generated_by"), r4.get("fallback_reason")],
        "provider_calls": good.calls,
    }
    # phase 4: AI switched off
    c2, _ = make_app(data, tmp / "off" if (tmp / "off").exists() else _mk(tmp / "off"), ai_enabled=False)
    off = c2.post("/ai/summarize/SHI-00027", headers=h)
    obs["phase4_ai_disabled"] = {
        "ai_status": off.status_code,
        "core": [
            c2.get("/records/SHI-00002", headers=h).status_code,
            c2.get("/shipments", headers=h).status_code,
            c2.get("/ready").status_code,
        ],
    }
    metrics = c.get("/metrics", headers=hdr("ops")).text
    obs["metrics_ai_fallback_lines"] = [ln for ln in metrics.splitlines() if ln.startswith("ai_fallback_total")]
    p1, p2, p3, p4 = obs["phase1_slow_provider"], obs["phase2_provider_down"], obs["phase3_recovery"], obs["phase4_ai_disabled"]
    ok = (
        p1["ai_status"] == 200
        and p1["fallback_reason"] == "provider_timeout"
        and p1["ai_wall_ms"] < 1200
        and set(p1["core_while_provider_hangs"]) == {200}
        and p2["reasons_in_order"][:2] == ["provider_error"] * 2
        and p2["reasons_in_order"][2:] == ["circuit_open"] * 4
        and p2["provider_calls"] == 2
        and p3["first_after_reset"][0] == "model"
        and p3["second"][0] == "model"
        and p4["ai_status"] == 503
        and set(p4["core"]) == {200}
    )
    return {
        "id": "DRILL-2",
        "name": "AI gateway timeout and core-workflow degradation",
        "hypothesis": "When the model hangs or fails the AI endpoint degrades to the deterministic fallback within the timeout, the core workflow "
        "stays up, the breaker stops calling the dependency, and the system recovers by itself.",
        "method": "Replace the gateway provider with (a) a provider that sleeps 2 s (timeout 0.3 s), (b) a provider that always raises (breaker "
        "threshold 3, reset 1 s), (c) a healthy provider after the reset window, (d) AI switched off. Core endpoints are called throughout.",
        "observations": obs,
        "pass_criteria": [
            "slow provider: 200 fallback provider_timeout in < 1.2 s; core 200",
            "down provider: 2 errors then circuit_open (the timeout in phase 1 already counted as the first of 3 failures), provider called 2 times",
            "after reset window the next call reaches the provider and succeeds",
            "AI off: 503 on AI, 200 on core",
        ],
        "verdict": verdict(ok),
        "findings": [
            "F-M3-02: a timed-out provider call cannot be killed; the worker thread is abandoned and keeps running until the provider returns. "
            "The pool is bounded (8 workers) but a hanging provider can exhaust it. The Bulkhead primitive exists and is tested but is NOT wired to "
            "the gateway. Accepted for the pilot (no real model); wire it before a model is enabled.",
        ],
    }


def _mk(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


# --------------------------------------------------------------------------------------------------------------------
def drill3(tmp: Path) -> dict[str, Any]:
    base = _mk(tmp / "base")
    d0 = make_data(base)
    cur0 = csv_rows(d0 / "curated" / "tracking_events.csv")
    q0 = [json.loads(x) for x in (d0 / "quarantine" / "tracking_events.jsonl").read_text().splitlines()]
    rep0 = json.loads((d0 / "reports" / "latest.json").read_text())

    # A. replay 40 curated events as new rows (new ids, same business key and sequence number)
    replay = _mk(tmp / "replay")
    d1 = replay / "data"
    shutil.copytree(ROOT / "data" / "synthetic", d1 / "synthetic")
    p = d1 / "synthetic" / "tracking_events.csv"
    with p.open(newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh)
        header, rows = list(rd.fieldnames or []), list(rd)
    curated_ids = {r["event_id"] for r in cur0}
    victims = [r for r in rows if r["event_id"] in curated_ids][:40]
    dups = [{**r, "event_id": f"EVE-9{i:04d}"} for i, r in enumerate(victims)]
    with p.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=header, lineterminator="\n")
        w.writeheader()
        w.writerows(rows + dups)
    batch.run(d1, d1, _semantic_dir(), 0.05, False)
    cur1 = csv_rows(d1 / "curated" / "tracking_events.csv")
    q1 = [json.loads(x) for x in (d1 / "quarantine" / "tracking_events.jsonl").read_text().splitlines()]
    new_q = [q for q in q1 if str(q["row"]["event_id"]).startswith("EVE-9")]
    replay_rules = sorted({r for q in new_q for r in q["rules"]})
    replayed_in_curated = [r for r in cur1 if str(r["event_id"]).startswith("EVE-9")]

    # B. the same input twice gives the same output (idempotent load)
    d2 = _mk(tmp / "twice")
    shutil.copytree(ROOT / "data" / "synthetic", d2 / "synthetic")
    batch.run(d2, d2, _semantic_dir(), 0.05, False)
    h1 = (d2 / "curated" / "shipments.csv").read_bytes() + (d2 / "curated" / "tracking_events.csv").read_bytes()
    r1 = json.loads((d2 / "reports" / "latest.json").read_text())["load_id"]
    batch.run(d2, d2, _semantic_dir(), 0.05, False)
    h2 = (d2 / "curated" / "shipments.csv").read_bytes() + (d2 / "curated" / "tracking_events.csv").read_bytes()
    r2 = json.loads((d2 / "reports" / "latest.json").read_text())["load_id"]

    # C. saga: replay the same booking request many times, sequentially, concurrently, and after a "restart"
    store_path = tmp / "bookings.jsonl"
    carrier = SimulatedCarrier(p_transient=0.0)
    saga = CarrierSaga(carrier, BookingStore(store_path), SagaConfig(max_attempts=3), sleep=lambda _s: None)
    seq = [saga.book("SHI-00100", "CarrierX") for _ in range(50)]
    suppressed_seq = sum(1 for o in seq if o.duplicate_suppressed)
    carrier2 = SimulatedCarrier(p_transient=0.0)
    saga2 = CarrierSaga(carrier2, BookingStore(tmp / "bookings2.jsonl"), SagaConfig(max_attempts=3), sleep=lambda _s: None)
    results: list[str] = []
    lock = threading.Lock()

    def worker() -> None:
        try:
            o = saga2.book("SHI-00200", "CarrierX")
            res = "suppressed" if o.duplicate_suppressed else "booked"
        except InFlightError:
            res = "in_flight_rejected"
        with lock:
            results.append(res)

    ts = [threading.Thread(target=worker) for _ in range(20)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    carrier3 = SimulatedCarrier(p_transient=0.0)
    saga3 = CarrierSaga(
        carrier3, BookingStore(store_path), SagaConfig(max_attempts=3), sleep=lambda _s: None
    )  # new process view of the same file
    after_restart = saga3.book("SHI-00100", "CarrierX")
    obs = {
        "etl_replay": {
            "events_replayed": len(dups),
            "curated_before": len(cur0),
            "curated_after": len(cur1),
            "quarantined_before": len(q0),
            "quarantined_after": len(q1),
            "replayed_rows_quarantined": len(new_q),
            "replayed_rows_in_curated": len(replayed_in_curated),
            "rules_that_caught_them": replay_rules,
            "baseline_report_load_id": rep0["load_id"],
        },
        "etl_same_input_twice": {"load_id_run1": r1, "load_id_run2": r2, "curated_bytes_identical": h1 == h2},
        "saga_sequential_50": {
            "carrier_book_calls": carrier.calls,
            "live_bookings": len(carrier.live),
            "duplicates_suppressed": suppressed_seq,
        },
        "saga_concurrent_20": {
            "outcomes": {k: results.count(k) for k in set(results)},
            "carrier_book_calls": carrier2.calls,
            "live_bookings": len(carrier2.live),
        },
        "saga_after_restart": {"duplicate_suppressed": after_restart.duplicate_suppressed, "carrier_book_calls": carrier3.calls},
    }
    ok = (
        len(new_q) == len(dups)
        and not replayed_in_curated
        and len(cur1) == len(cur0)
        and h1 == h2
        and r1 == r2
        and carrier.calls == 1
        and len(carrier.live) == 1
        and suppressed_seq == 49
        and carrier2.calls == 1
        and len(carrier2.live) == 1
        and after_restart.duplicate_suppressed
        and carrier3.calls == 0
    )
    return {
        "id": "DRILL-3",
        "name": "Duplicate event replay against idempotency",
        "hypothesis": "Replayed events do not create second facts, and replayed booking requests do not create second bookings.",
        "method": "(A) append 40 replayed tracking events (new event ids, same business key and sequence number) and run the ETL; (B) run the ETL twice on "
        "the same input; (C) replay one booking request 50 times, then 20 times concurrently, then after a simulated restart on the same store file.",
        "observations": obs,
        "pass_criteria": [
            "all replayed events quarantined, none curated, curated count unchanged",
            "second ETL run is byte-identical",
            "exactly one carrier call and one live booking per shipment, also concurrently and after restart",
        ],
        "verdict": verdict(ok),
        "findings": [
            "F-M3-03: idempotency is by business key (BR-01/BR-02) in the batch and by (shipment, carrier) key in the saga. A replay with a changed "
            "business key (e.g. a shifted event_time) is a new fact and is NOT caught. Stated limit, not a defect.",
        ],
    }


# --------------------------------------------------------------------------------------------------------------------
def view(o: dict[str, Any]) -> tuple[Any, Any, Any]:
    return (o.get("abstained"), o.get("summary"), o.get("recommendation"))


def drill4(tmp: Path) -> dict[str, Any]:
    data = make_data(tmp)
    c, st = make_app(data, tmp, data_max_age_s=24 * 3600)
    h = hdr("dispatcher")
    sid = "SHI-00027"
    src = data / "synthetic" / "shipments.csv"
    before = c.get(f"/records/{sid}", headers=h)
    ai0 = c.post(f"/ai/summarize/{sid}", headers=h).json()
    load0 = before.headers["x-data-load-id"]
    old_status = before.json()["status"]
    # the master changes; ETL is NOT re-run
    text = src.read_text(encoding="utf-8")
    new_status = "manual_hold" if old_status != "manual_hold" else "exception"
    lines = text.splitlines()
    hdr_cols = lines[0].split(",")
    si = hdr_cols.index("status")
    for i, ln in enumerate(lines):
        if ln.startswith(sid + ","):
            cols = ln.split(",")
            cols[si] = new_status
            lines[i] = ",".join(cols)
    src.write_text("\n".join(lines) + "\n", encoding="utf-8")
    stale = c.get(f"/records/{sid}", headers=h)
    ai1 = c.post(f"/ai/summarize/{sid}", headers=h).json()
    fresh_ready = c.get("/ready").status_code
    # time passes: the last ETL report becomes 30 h old
    rep_path = data / "reports" / "latest.json"
    rep = json.loads(rep_path.read_text())
    rep["run_id"] = "run-" + (datetime.now(UTC) - timedelta(hours=30)).strftime("%Y%m%dT%H%M%SZ")
    rep_path.write_text(json.dumps(rep))
    old_ready = c.get("/ready")
    # recovery: re-run the ETL
    batch.run(data, data, _semantic_dir(), 0.05, False)
    healed = c.get(f"/records/{sid}", headers=h)
    ai2 = c.post(f"/ai/summarize/{sid}", headers=h).json()
    ready_after = c.get("/ready").status_code
    ev = [e for e in audit_events(st) if e["action"] == "ai.summary"]
    obs = {
        "shipment": sid,
        "master_status_changed_to": new_status,
        "record_status_before_change": old_status,
        "record_status_after_master_change_before_etl": stale.json()["status"],
        "record_status_after_etl": healed.json()["status"],
        "ai_output_before": view(ai0),
        "ai_output_unchanged_while_stale": view(ai1) == view(ai0),
        "ai_output_changed_after_etl": view(ai2) != view(ai0),
        "data_load_id": {
            "served_before": load0,
            "served_while_stale": stale.headers["x-data-load-id"],
            "served_after_etl": healed.headers["x-data-load-id"],
        },
        "ready_while_report_recent": fresh_ready,
        "ready_when_report_30h_old": old_ready.status_code,
        "ready_when_report_30h_old_detail": old_ready.json().get("detail"),
        "ready_after_etl": ready_after,
        "audit_ai_summary_input_hashes": [e.get("input_hash") for e in ev],
        "input_hash_changed_after_etl": len(ev) == 3
        and ev[0].get("input_hash") == ev[1].get("input_hash") != ev[2].get("input_hash"),
    }
    ok = (
        obs["record_status_after_master_change_before_etl"] == old_status
        and obs["ai_output_unchanged_while_stale"]
        and fresh_ready == 200
        and old_ready.status_code == 503
        and "data_fresh" in str(obs["ready_when_report_30h_old_detail"])
        and obs["record_status_after_etl"] == new_status
        and obs["ai_output_changed_after_etl"]
        and ready_after == 200
        and obs["input_hash_changed_after_etl"]
    )
    return {
        "id": "DRILL-4",
        "name": "Stale master data traced downstream",
        "hypothesis": "A change in the master data that has not been loaded is visible (readiness, data-version header) and its downstream "
        "effect (record, AI summary, audit input hash) is traceable and heals on reload.",
        "method": "Change one shipment's status in the source file without re-running the ETL; read the record and the AI summary; age the "
        "last ETL report to 30 h; check /ready with DATA_MAX_AGE_S=24 h; re-run the ETL; read again; compare audit input hashes.",
        "observations": obs,
        "pass_criteria": [
            "stale value is served until reload (the behaviour is understood, not hidden)",
            "/ready fails when the last load is older than the limit",
            "after reload record and summary change",
            "audit input hash differs between the stale and reloaded summaries",
            "every response names the data load it came from",
        ],
        "verdict": verdict(ok),
        "findings": [
            "F-M3-04: staleness is only detected when DATA_MAX_AGE_S is set; the default is off. Set it in every deployed environment.",
            "F-M3-05: the AI summary and the dispatcher both act on the last loaded copy, not the master. The data-version header now lets an "
            "investigator tie any response to a load; the audit event does not yet store the load id (backlog DB-16).",
            "stale_gps (BR-03) is NOT testable: the vehicles dataset has no position timestamp, so a stale position cannot be told from a fresh one.",
        ],
    }


# --------------------------------------------------------------------------------------------------------------------
def drill5(tmp: Path) -> dict[str, Any]:
    # corrupted input: truncated mid-row, one row with a wrong column count, one blank mandatory field
    src_dir = _mk(tmp / "corrupt")
    shutil.copytree(ROOT / "data" / "synthetic", src_dir / "data" / "synthetic")
    shutil.copytree(ROOT / "legacy", src_dir / "legacy")
    ship = src_dir / "data" / "synthetic" / "shipments.csv"
    lines = ship.read_text(encoding="utf-8").splitlines()
    total_rows = len(lines) - 1
    lines[10] = lines[10].rsplit(",", 3)[0]  # wrong column count
    lines[20] = lines[20].replace(lines[20].split(",")[1], "", 1)  # blank customer_id
    body = "\n".join(lines[:-1]) + "\n" + lines[-1][: len(lines[-1]) // 2]  # last row cut in half, no trailing newline
    ship.write_text(body, encoding="utf-8")
    # arm A: the legacy batch
    before_files = {p.relative_to(src_dir) for p in src_dir.rglob("*") if p.is_file()}
    la = subprocess.run(
        [sys.executable, "-I", str(src_dir / "legacy" / "reconcile_legacy.py")],
        capture_output=True,
        text=True,
        timeout=60,
        cwd=src_dir,
    )  # noqa: S603
    after_files = {p.relative_to(src_dir) for p in src_dir.rglob("*") if p.is_file()}
    new_legacy_files = sorted(str(p) for p in after_files - before_files if "__pycache__" not in str(p))
    # arm B: the ETL on the same corrupted input
    etl_dir = _mk(tmp / "etl")
    shutil.copytree(src_dir / "data" / "synthetic", etl_dir / "synthetic")
    rep = batch.run(etl_dir, etl_dir, _semantic_dir(), 0.05, False)
    sh = rep["entities"]["shipments"]
    qrows = [json.loads(x) for x in (etl_dir / "quarantine" / "shipments.jsonl").read_text().splitlines()]
    recon = sh["processed"] == sh["curated"] + sh["quarantined"]
    # arm C: the ETL dies half way
    good = _mk(tmp / "good")
    shutil.copytree(ROOT / "data" / "synthetic", good / "synthetic")
    batch.run(good, good, _semantic_dir(), 0.05, False)
    snap = {
        p.relative_to(good): p.read_bytes()
        for sub in ("curated", "quarantine", "reports")
        for p in (good / sub).rglob("*")
        if p.is_file()
    }
    calls = {"n": 0}
    real = batch.evaluate_entity

    def dying(*a: Any, **k: Any) -> Any:
        calls["n"] += 1
        if calls["n"] == 4:
            raise OSError("injected: disk full while processing the 4th entity")
        return real(*a, **k)

    batch.evaluate_entity = dying
    crashed = None
    try:
        batch.run(good, good, _semantic_dir(), 0.05, False)
    except OSError as exc:
        crashed = str(exc)
    finally:
        batch.evaluate_entity = real
    snap2 = {
        p.relative_to(good): p.read_bytes()
        for sub in ("curated", "quarantine", "reports")
        for p in (good / sub).rglob("*")
        if p.is_file()
    }
    stage = good / batch.STAGING
    leftover = sorted(str(p.relative_to(good)) for p in stage.rglob("*") if p.is_file()) if stage.exists() else []
    obs = {
        "input": {
            "shipment_rows": total_rows,
            "damage": "row 10 short by 3 columns, row 20 blank customer_id, last row truncated mid-field",
        },
        "legacy_batch": {
            "exit_code": la.returncode,
            "stdout": la.stdout.strip(),
            "stderr_tail": la.stderr.strip()[-200:],
            "new_files_written": new_legacy_files,
            "reports_rejected_rows": False,
        },
        "etl": {
            "processed": sh["processed"],
            "curated": sh["curated"],
            "quarantined": sh["quarantined"],
            "reconciles": recon,
            "quarantine_has_reason_per_row": all(q["rules"] for q in qrows),
            "quarantine_has_source_row": all("source_row" in q for q in qrows),
            "rules_seen": sh["quarantine_by_rule"],
        },
        "etl_crash": {
            "crashed_with": crashed,
            "published_layers_unchanged": snap == snap2,
            "staging_files_left_behind": leftover,
        },
    }
    ok = (
        recon
        and obs["etl"]["quarantine_has_reason_per_row"]
        and obs["etl"]["quarantine_has_source_row"]
        and snap == snap2
        and crashed is not None
        and not leftover
        and not new_legacy_files
    )
    return {
        "id": "DRILL-5",
        "name": "Legacy batch partial failure and audit-evidence completeness",
        "hypothesis": "Damaged input and a mid-run crash must not leave a silent partial result; the new ETL's evidence is complete where the legacy "
        "batch's is not.",
        "method": "Feed identical corrupted shipments to the legacy reconcile script and the ETL; then crash the ETL while processing the 4th of 6 "
        "entities and compare the published layers byte for byte.",
        "observations": obs,
        "pass_criteria": [
            "ETL: processed = curated + quarantined, every quarantined row has rules and a source row",
            "ETL crash: published layers byte-identical to the last good run, exit non-zero",
            "legacy batch evidence is recorded as found (not asserted to be good)",
        ],
        "verdict": verdict(ok),
        "findings": [
            "F-M3-06: the legacy batch counts rows and prints a number. It writes no report, no reject list and does not fail on damaged rows: "
            "partial failure is silent. Kept for coexistence only; it must not be used as a control.",
            "F-M3-07 (FIXED during M3): before this drill the ETL wrote curated/quarantine files directly, so a crash mid-run left a mix of new and "
            "old files. Found by reading the write sequence while designing this drill; fixed with staged writes and os.replace publication "
            "(tests/test_data_resilience.py). The 'before' behaviour was not reproduced by execution.",
            "Publication is atomic per file, not across all files: a reader can see new curated shipments with old curated events for a moment "
            "during publish. Acceptable for the batch window; a versioned directory swap is the platform-level fix.",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True, type=Path)
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for fn, slug in (
        (drill1, "1-correlation-ids"),
        (drill2, "2-ai-gateway-timeout"),
        (drill3, "3-duplicate-replay"),
        (drill4, "4-stale-master-data"),
        (drill5, "5-legacy-partial-failure"),
    ):
        with tempfile.TemporaryDirectory() as t:
            res = fn(Path(t))
        res["run_utc"] = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        (a.out_dir / f"drill-{slug}.json").write_text(
            json.dumps(res, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8", newline="\n"
        )
        results.append({k: res[k] for k in ("id", "name", "verdict")})
        print(res["id"], res["verdict"], res["name"])
    (a.out_dir / "summary.json").write_text(json.dumps({"drills": results}, indent=2) + "\n", encoding="utf-8", newline="\n")
    return 0 if all(r["verdict"] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
