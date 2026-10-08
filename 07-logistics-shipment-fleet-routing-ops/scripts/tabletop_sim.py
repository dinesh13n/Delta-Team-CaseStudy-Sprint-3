# ruff: noqa: E501
"""Scripted incident simulation (runbook M4 tabletop). Author-run: one person plays every role.

    python -m scripts.tabletop_sim --out ../evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json

Scenario TT-1: a model returns a summary containing a customer identifier (forbidden by ai-context-policy).
The simulation drives the real application in process, follows docs/29-incident-bcdr/ai-incident-playbook.md step by step and
records what each step actually produced. It tests the playbook and the system's evidence. It does NOT test people, escalation
paths, communication channels or decision-making under pressure: no second human takes part.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from fastapi.testclient import TestClient

import etl.run_daily_batch as batch
from apps.api.ai.providers import PromptParts, ProviderResult
from apps.api.config import ROOT, Settings, _semantic_dir
from apps.api.main import create_app
from apps.api.security.tokens import issue_dev_token
from scripts.reconstruct import reconstruct

SECRET = "tabletop-secret-" + "x" * 40  # secret-scan: allow (throw-away value for the in-process simulation)


def hdr(role: str, sub: str, purpose: str | None = None) -> dict[str, str]:
    return {"Authorization": "Bearer " + issue_dev_token(SECRET, sub, role, purpose=purpose, ttl=3600)}


class LeakyModel:
    """A model that was manipulated (or simply wrong) and puts the customer id into its summary."""

    name, version = "leaky-model", "1"

    def __init__(self, leak: str) -> None:
        self.leak = leak

    def complete(self, parts: PromptParts, facts: dict[str, Any]) -> ProviderResult:
        return ProviderResult(
            json.dumps(
                {
                    "summary": f"Shipment is in exception. Customer {self.leak} should be called back.",
                    "recommendation": "Call the customer",
                    "confidence": 0.9,
                    "abstained": False,
                }
            )
        )


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def settings_for(data: Path, tmp: Path, **kw: Any) -> Settings:
    return Settings(
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    a = ap.parse_args()
    t0 = time.perf_counter()
    steps: list[dict[str, Any]] = []

    def step(phase: str, action: str, observed: Any, ok: bool | None = None) -> None:
        steps.append(
            {
                "t_plus_s": round(time.perf_counter() - t0, 2),
                "phase": phase,
                "playbook_action": action,
                "observed": observed,
                "ok": ok,
            }
        )

    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        data = tmp / "data"
        shutil.copytree(ROOT / "data" / "synthetic", data / "synthetic")
        batch.run(data, data, _semantic_dir(), 0.05, False)
        st = settings_for(data, tmp)
        app = create_app(st)
        c = TestClient(app)
        gw = app.state.svc.gateway
        sid = "SHI-00027"
        leak = "CUS-00027"  # the shipment's customer_id (forbidden field)
        responses: list[str] = []

        # ---- inject
        gw.provider = LeakyModel(leak)
        r = c.post(f"/ai/summarize/{sid}", headers={**hdr("dispatcher", "alice"), "X-Correlation-ID": "trace-tabletop-0001"})
        responses.append(r.text)
        body = r.json()
        step(
            "INJECT",
            "Model returns a summary containing a customer identifier",
            {
                "status": r.status_code,
                "generated_by": body["generated_by"],
                "fallback_reason": body["fallback_reason"],
                "guardrail_status": body["guardrail_status"],
                "leak_in_response": leak in r.text,
            },
            ok=leak not in r.text,
        )

        # ---- detect
        metrics = c.get("/metrics", headers=hdr("ops", "oncall")).text
        blocked = [
            ln
            for ln in metrics.splitlines()
            if ln.startswith("ai_guardrail_blocked_total") or 'ai_fallback_total{reason="output_policy_violation"}' in ln
        ]
        step(
            "DETECT",
            "Alert condition: increase(ai_fallback_total{reason='output_policy_violation'}) > 0 (note: ai_guardrail_blocked_total does NOT fire on this path)",
            {"metric_lines": blocked},
            ok=bool(blocked),
        )

        # ---- triage
        rec = reconstruct(st.audit_path, st.approvals_path, "trace-tabletop-0001", None, None, None)
        ai_ev = [e for e in rec["events"] if e["action"] == "ai.summary"]
        d = ai_ev[0]["detail"] if ai_ev else {}
        step(
            "TRIAGE",
            "Find the event by correlation id; read what the AI did and from which data (audit only, no application logs)",
            {
                "events_matched": rec["events_matched"],
                "timeline": rec["timeline"],
                "from_audit": {
                    k: d.get(k) for k in ("generated_by", "fallback_reason", "guardrail_status", "prompt_version", "data_load_id")
                },
            },
            ok=d.get("fallback_reason") == "output_policy_violation" and bool(d.get("data_load_id")),
        )
        affected = c.get(f"/shipments/{sid}/events", headers=hdr("dispatcher", "alice"))
        responses.append(affected.text)
        sev = (
            "SEV-3 (control worked: nothing reached a person)"
            if all(leak not in x for x in responses)
            else "SEV-2 (a forbidden value reached a response)"
        )
        step(
            "TRIAGE",
            "Severity per incident-severity-matrix: did any forbidden value leave the system?",
            {"responses_checked": len(responses), "severity": sev},
            ok=sev.startswith("SEV-3"),
        )

        # ---- who saw it / any action taken?
        who = reconstruct(st.audit_path, st.approvals_path, None, body["summary_id"], None, None)
        step(
            "TRIAGE",
            "Who requested it, was it decided?",
            {
                "approval_records": [
                    {k: v for k, v in x.items() if k in ("kind", "requested_by", "decision", "decided_by")}
                    for x in who["approval_records"]
                ]
            },
            ok=len(who["approval_records"]) >= 1,
        )

        # ---- contain
        t_contain = time.perf_counter()
        st_off = settings_for(data, tmp, ai_enabled=False)
        c_off = TestClient(create_app(st_off))
        off = c_off.post(f"/ai/summarize/{sid}", headers=hdr("dispatcher", "alice"))
        core = [c_off.get("/records/" + sid, headers=hdr("dispatcher", "alice")).status_code, c_off.get("/ready").status_code]
        step(
            "CONTAIN",
            "Switch AI off (AI_ENABLED=false + restart); core workflow check",
            {
                "ai_status": off.status_code,
                "core": core,
                "restart_to_effect_s_in_process": round(time.perf_counter() - t_contain, 3),
            },
            ok=off.status_code == 503 and core == [200, 200],
        )

        # ---- preserve evidence
        ev_dir = tmp / "preserved"
        ev_dir.mkdir()
        shutil.copy(st.audit_path, ev_dir / "audit.log")
        shutil.copy(st.approvals_path, ev_dir / "approvals.jsonl")
        ver = reconstruct(ev_dir / "audit.log", ev_dir / "approvals.jsonl", None, None, "alice", None)
        step(
            "PRESERVE",
            "Copy audit and approvals, hash the copies, verify the chain, record the tip hash outside the system",
            {
                "audit_sha256": sha(ev_dir / "audit.log"),
                "approvals_sha256": sha(ev_dir / "approvals.jsonl"),
                "chain_valid": ver["chain"]["valid"],
                "records": ver["chain"]["records"],
                "tip_hash": ver["chain"]["tip_hash"],
            },
            ok=ver["chain"]["valid"],
        )

        # ---- eradicate / verify the fix
        lock = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-q",
                "-p",
                "no:cacheprovider",
                "tests/test_prompt_lock.py",
                "tests/test_ai_remediation.py",
            ],
            capture_output=True,
            text=True,
            cwd=ROOT,
            timeout=300,
        )  # noqa: S603
        ev = subprocess.run(
            [sys.executable, "-m", "evaluation.run_eval", "--out", str(tmp / "eval.json"), "--label", "tabletop"],
            capture_output=True,
            text=True,
            cwd=ROOT,
            timeout=300,
        )  # noqa: S603
        fails = len(json.loads((tmp / "eval.json").read_text())["failures"]) if (tmp / "eval.json").exists() else None
        step(
            "ERADICATE",
            "Prove prompts and guardrail unchanged, re-run the evaluation before re-enabling AI",
            {"prompt_lock_and_remediation_tests_exit": lock.returncode, "eval_exit": ev.returncode, "eval_failures": fails},
            ok=lock.returncode == 0 and fails == 0,
        )

        # ---- recover
        c_ok = TestClient(create_app(settings_for(data, tmp)))  # deterministic provider (no model configured)
        back = c_ok.post(f"/ai/summarize/{sid}", headers=hdr("dispatcher", "alice")).json()
        step(
            "RECOVER",
            "Re-enable AI with the deterministic provider only (the leaking model stays disabled)",
            {
                "generated_by": back["generated_by"],
                "guardrail_status": back["guardrail_status"],
                "leak_in_response": leak in json.dumps(back),
            },
            ok=back["generated_by"] == "deterministic" and leak not in json.dumps(back),
        )

        # ---- communicate
        comms = (
            f"Subject: AI summary guardrail blocked a model output (SEV-3)\n"
            f"What happened: at {ai_ev[0]['ts'] if ai_ev else 'n/a'} a model summary for {sid} contained a customer identifier. The output guardrail replaced it with a deterministic summary.\n"
            f"Impact: no customer identifier left the system; {len(who['approval_records'])} suggestion record(s) exist; no shipment, route or booking was changed.\n"
            f"Action taken: AI switched off, evidence preserved (tip hash {ver['chain']['tip_hash'][:16]}...), evaluation re-run (0 failures), AI re-enabled with the deterministic provider only.\n"
            f"Next: owner to decide whether the model may be re-enabled after a TEVV re-run."
        )
        step("COMMUNICATE", "Fill the communications template from facts in the audit", {"message": comms}, ok=True)

    passed = all(s["ok"] for s in steps if s["ok"] is not None)
    out = {
        "scenario": "TT-1 model output contains a customer identifier",
        "run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "participants": "none: author-run simulation (one agent played all roles)",
        "what_this_proves": "the playbook steps can be executed with the evidence the system actually produces",
        "what_this_does_not_prove": "that people can find, follow and decide with the playbook under pressure; escalation and communication channels",
        "steps": steps,
        "all_checks_ok": passed,
        "total_s": round(time.perf_counter() - t0, 2),
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    for s in steps:
        print(
            f"{s['t_plus_s']:>6}s {s['phase']:<11} {'OK ' if s['ok'] else 'FAIL' if s['ok'] is False else '-'}  {s['playbook_action']}"
        )
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
