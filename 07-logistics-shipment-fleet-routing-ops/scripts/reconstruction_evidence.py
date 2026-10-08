# ruff: noqa: E501
"""Reconstruction evidence (runbook N2): drive one realistic request chain, then rebuild it from the audit and approval record only.

    python -m scripts.reconstruction_evidence --out ../evidence/31-observability/EVD-N-02-reconstruction.json

The chain: actor -> request -> policy decision -> data load -> AI producer/prompt -> recommendation -> human decision -> audit -> trace id.
Also measures how many audit events carry the correlation fields (the baseline source stream carried a usable id on 33.6% of events).
Author-run, in process, deterministic provider: it shows the evidence exists and joins, not that a real model's reasoning can be replayed.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from fastapi.testclient import TestClient

import etl.run_daily_batch as batch
from apps.api.config import ROOT, Settings, _semantic_dir
from apps.api.main import create_app
from apps.api.security.tokens import issue_dev_token
from scripts.reconstruct import load, reconstruct

SECRET = "recon-evidence-secret-" + "x" * 40  # secret-scan: allow (throw-away value for an in-process run)
CID = "trace-n2-0001"


def hdr(role: str, sub: str, cid: str | None = None) -> dict[str, str]:
    h = {"Authorization": "Bearer " + issue_dev_token(SECRET, sub, role, ttl=3600)}
    if cid:
        h["X-Correlation-ID"] = cid
    return h


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
            ai_rate_per_minute=1000,
        )
        c = TestClient(create_app(st))
        sid = "SHI-00027"
        # background traffic so the reconstruction has to pick the right events out of others
        for i in range(5):
            c.get(f"/records/SHI-0000{i + 1}", headers=hdr("dispatcher", "bob", f"noise-{i}"))
        c.get("/records/SHI-00002", headers=hdr("clinician", "mallory", "noise-denied"))
        c.get("/records/SHI-00002", headers={"X-Correlation-ID": "noise-anon"})

        r1 = c.get(f"/records/{sid}", headers=hdr("dispatcher", "alice", CID))
        r2 = c.post(f"/ai/summarize/{sid}", headers=hdr("dispatcher", "alice", CID))
        s = r2.json()
        r3 = c.post(
            f"/ai/summaries/{s['summary_id']}/decision",
            headers=hdr("dispatcher", "alice", CID),
            json={"decision": "approve", "reason": "checked against the booking"},
        )

        rec = reconstruct(st.audit_path, st.approvals_path, CID, None, None, None)
        ev = rec["events"]
        ai = next((e for e in ev if e["action"] == "ai.summary"), None)
        dec = next((e for e in ev if e["action"] == "ai.decision"), None)
        d = (ai or {}).get("detail") or {}
        link = {
            "actor": (ai or {}).get("actor"),
            "request": {
                "correlation_id": CID,
                "action": (ai or {}).get("action"),
                "resource": (ai or {}).get("resource"),
                "http_echo": r2.headers.get("X-Correlation-ID"),
            },
            "policy_decision": (ai or {}).get("policy_decision"),
            "data_load_id": d.get("data_load_id"),
            "data_load_id_response_header": r2.headers.get("X-Data-Load-Id"),
            "producer": {
                k: d.get(k) for k in ("generated_by", "fallback_reason", "guardrail_status", "prompt_version", "latency_ms")
            },
            "recommendation_ref": {"summary_id": s["summary_id"], "requires_human_approval": s["requires_human_approval"]},
            "human_approval": [
                {
                    k: x.get(k)
                    for k in ("kind", "summary_id", "requested_by", "decision", "decided_by", "decided_at", "correlation_id")
                }
                for x in rec["approval_records"]
            ],
            "decision_event": {
                "action": (dec or {}).get("action"),
                "outcome": (dec or {}).get("outcome"),
                "actor": (dec or {}).get("actor"),
            },
            "audit_chain": {k: rec["chain"][k] for k in ("valid", "records", "tip_hash", "trusted")},
            "trace_id": CID,
        }
        complete = all(
            [
                link["actor"] and link["actor"].get("subject") == "alice",
                link["policy_decision"] and link["policy_decision"].get("decision") == "allow",
                link["data_load_id"] and link["data_load_id"] == link["data_load_id_response_header"],
                link["producer"]["generated_by"] and link["producer"]["prompt_version"],
                any(x.get("kind") == "decision" and x.get("decided_by") == "alice" for x in link["human_approval"]),
                link["decision_event"]["action"] == "ai.decision",
                link["audit_chain"]["valid"],
                r1.status_code == r2.status_code == r3.status_code == 200,
            ]
        )
        events = load(st.audit_path)
        fields = {
            "correlation_id": lambda e: bool(e.get("correlation_id")),
            "actor_subject": lambda e: bool((e.get("actor") or {}).get("subject")),
            "policy_decision": lambda e: bool(e.get("policy_decision")),
            "resource_id": lambda e: bool((e.get("resource") or {}).get("id")),
        }
        cover = {k: {"present": sum(f(e) for e in events), "of": len(events)} for k, f in fields.items()}
        # tamper test: the reconstruction must say UNTRUSTED when a past event is edited
        tampered = tmp / "tampered.log"
        lines = st.audit_path.read_text(encoding="utf-8").splitlines()
        j = json.loads(lines[1])
        j["actor"]["subject"] = "someone-else"
        lines[1] = json.dumps(j)
        tampered.write_text("\n".join(lines) + "\n", encoding="utf-8")
        bad = reconstruct(tampered, st.approvals_path, CID, None, None, None)
        out: dict[str, Any] = {
            "run_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "scenario": "dispatcher alice reads a shipment, requests an AI summary, approves it; noise traffic from 3 other callers",
            "participants": "none: author-run, in process, deterministic provider",
            "reconstruction": {
                "query": rec["query"],
                "events_matched": rec["events_matched"],
                "timeline": rec["timeline"],
                "chain_of_evidence": link,
            },
            "chain_complete": bool(complete),
            "audit_field_coverage": cover,
            "baseline_comparison": {
                "baseline_source_stream": "docs/04-baseline-kpis/baseline-data-quality.md: correlation usable on 1,008 of 3,000 events (33.6%); no actor, tenant or approval in the baseline audit (F-43)",
                "after_audit_events": f"{cover['correlation_id']['present']} of {cover['correlation_id']['of']} audit events carry a correlation id and actor",
                "not_improved": "the SOURCE event stream still has no correlation column (F-M3-01); lineage for stored events is load_id + source_row",
            },
            "tamper_test": {
                "edited": "actor.subject of audit record 1",
                "chain_valid": bad["chain"]["valid"],
                "trusted": bad["chain"]["trusted"],
                "note": bad["trust_note"],
            },
            "observations": [
                "the decision record in the approval store carries no correlation id of its own (null); it is joined to the request through summary_id and through the ai.decision audit event, which does carry it",
                "requester and decider are the same subject (alice): the system permits self-approval (HC-R-01, four-eyes not implemented)",
            ],
            "not_shown": [
                "the exact model text (not stored in audit by design)",
                "reconstruction by a person other than the author",
                "behaviour with a real model or IdP",
            ],
        }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        "chain_complete",
        out["chain_complete"],
        "| events",
        rec["events_matched"],
        "| coverage",
        {k: f"{v['present']}/{v['of']}" for k, v in cover.items()},
        "| tamper trusted:",
        out["tamper_test"]["trusted"],
    )
    print(*rec["timeline"], sep="\n")
    return 0 if complete and not bad["chain"]["trusted"] else 1


if __name__ == "__main__":
    sys.exit(main())
