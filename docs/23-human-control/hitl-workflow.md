# Human-in-the-loop workflow

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/main.py, apps/api/approvals.py, test_human_control.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Human-in-the-loop applies to **every AI suggestion**.

1. A dispatcher requests a summary: `POST /ai/summarize/{shipment_id}` (token, policy `shipments:read`, rate limit).
2. The gateway returns a suggestion with a `summary_id`, `requires_human_approval: true`, `generated_by` (`deterministic`, `model` or `fallback`) and the reason if it fell back. The request is registered as *pending* with the requester's subject and correlation id.
3. The dispatcher reads it next to the record. Nothing has changed in any system.
4. The dispatcher decides: `POST /ai/summaries/{summary_id}/decision` with `approve` or `reject` and an optional reason (≤ 500 chars).
5. The system records `approval_id`, `decided_by` (from the token), `decided_at` (server clock) and appends an `ai.decision` audit event (`ai.decision.denied` for refused attempts).
6. A second decision on the same suggestion returns 409.

States: `pending` → `approved` | `rejected` (final). There is no expiry state yet (HC-R-03).

[VF] Steps 1-6 are implemented and covered by `tests/test_human_control.py`. Operations view: `/ops` shows the suggestion with an "approval required" label.
[UNK] What an approval *triggers* in the real business (reassignment, customer notice) is outside the pilot; it is carried by the dispatcher in existing tools.
