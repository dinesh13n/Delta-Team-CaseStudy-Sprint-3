"""Incident reconstruction from the audit chain and the approval record (runbook N2).

    python -m scripts.reconstruct --audit logs/audit-v2.log --approvals logs/approvals.jsonl --summary-id sum-... --out out.json
    python -m scripts.reconstruct --audit ... --correlation-id corr-... | --subject alice | --resource SHI-00027

Answers: who did what, to which record, under which policy decision, what the AI produced and from which data load, and who
decided. The chain is verified first; a broken chain is reported prominently and the timeline is marked UNTRUSTED.
Read-only: it never writes to the audit file.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from apps.api.audit_chain import GENESIS, JsonlAuditSink


def load(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def select(
    events: list[dict[str, Any]], *, corr: str | None, summary: str | None, subject: str | None, resource: str | None
) -> list[dict[str, Any]]:
    summary_corrs = {e["correlation_id"] for e in events if summary and (e.get("detail") or {}).get("summary_id") == summary}
    summary_corrs |= {e["correlation_id"] for e in events if summary and e["resource"]["id"] == summary}
    out = []
    for e in events:
        d = e.get("detail") or {}
        if (
            (corr and e["correlation_id"] == corr)
            or (
                summary
                and (e["correlation_id"] in summary_corrs or d.get("summary_id") == summary or e["resource"]["id"] == summary)
            )
            or (subject and e["actor"]["subject"] == subject)
            or (resource and e["resource"]["id"] == resource)
        ):
            out.append(e)
    return out


def line(e: dict[str, Any]) -> str:
    d = e.get("detail") or {}
    bits = [
        f"{e['ts']}",
        f"{e['action']}",
        f"by {e['actor']['subject']} ({e['actor']['role']})",
        f"on {e['resource']['type']} {e['resource']['id']}",
    ]
    bits.append(f"policy={e['policy_decision']['decision']} rule={e['policy_decision']['rule']}")
    bits.append(f"outcome={e['outcome']}")
    if d.get("generated_by"):
        bits.append(f"ai={d['generated_by']}" + (f"({d['fallback_reason']})" if d.get("fallback_reason") else ""))
    if d.get("guardrail_status"):
        bits.append(f"guardrail={d['guardrail_status']}")
    if d.get("data_load_id"):
        bits.append(f"data={d['data_load_id']}")
    if e.get("approval_id"):
        bits.append(f"approval={e['approval_id']}")
    bits.append(f"corr={e['correlation_id']}")
    return " | ".join(bits)


def reconstruct(
    audit: Path, approvals: Path | None, corr: str | None, summary: str | None, subject: str | None, resource: str | None
) -> dict[str, Any]:
    ver = JsonlAuditSink(audit).verify() if audit.exists() else {"valid": True, "records": 0, "first_bad_index": None}
    events = load(audit)
    tip = events[-1]["hash"] if events else GENESIS
    picked = select(events, corr=corr, summary=summary, subject=subject, resource=resource)
    appr = []
    # approval records are joined through the suggestions the matched audit events point at, so a decision record that carries
    # no correlation id of its own (it is written by a later request) is still found
    linked = {(e.get("detail") or {}).get("summary_id") for e in picked}
    linked |= {e["resource"]["id"] for e in picked if e["resource"]["type"] == "ai_summary"}
    linked.discard(None)
    approval_ids = {e["approval_id"] for e in picked if e.get("approval_id")}
    if approvals and approvals.exists():
        for rec in (json.loads(x) for x in approvals.read_text(encoding="utf-8").splitlines() if x.strip()):
            sid = rec.get("summary_id")
            by_query = (
                (summary and sid == summary)
                or (corr and rec.get("correlation_id") == corr)
                or (resource and rec.get("shipment_id") == resource)
                or (subject and subject in (rec.get("requested_by"), rec.get("decided_by")))
            )
            if by_query or sid in linked or rec.get("approval_id") in approval_ids:
                appr.append(rec)
    return {
        "query": {"correlation_id": corr, "summary_id": summary, "subject": subject, "resource": resource},
        "chain": {**ver, "tip_hash": tip, "trusted": bool(ver["valid"])},
        "trust_note": "chain valid: edits to past events would have been detected"
        if ver["valid"]
        else "CHAIN BROKEN: treat the timeline as untrusted and preserve the file",
        "events_matched": len(picked),
        "timeline": [line(e) for e in picked],
        "events": picked,
        "approval_records": appr,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", required=True, type=Path)
    ap.add_argument("--approvals", type=Path, default=None)
    ap.add_argument("--correlation-id", default=None)
    ap.add_argument("--summary-id", default=None)
    ap.add_argument("--subject", default=None)
    ap.add_argument("--resource", default=None)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    res = reconstruct(a.audit, a.approvals, a.correlation_id, a.summary_id, a.subject, a.resource)
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(json.dumps(res, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(res["trust_note"])
    print(*res["timeline"], sep="\n")


if __name__ == "__main__":
    main()
