# Operating contract updates (A5 reconciliation)

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | docs/00-preflight/operating-contract*, autonomy-matrix.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Reconciliation of the A5 provisional controls with what was built.

| A5 provisional control | Status after K1 | Note |
|---|---|---|
| Human approval for every AI output | CONFIRMED, enforced (D-08) | |
| AI may not act on systems | CONFIRMED, enforced by absence of write endpoints | |
| AI sees only allow-listed fields | CONFIRMED, tested (eval) | |
| Named approver per decision | PARTLY: approver is the authenticated subject; no named-approver registry | OQ-05 |
| Four-eyes for high-impact actions | NOT IMPLEMENTED | HC-R-01, needed when actions exist |
| Override must be recorded | NOT IMPLEMENTED for deterministic rules | DB-12 |
| Kill switch | CONFIRMED | `AI_ENABLED` |
| Approval expires | NOT IMPLEMENTED | HC-R-03 |

[VF] Three provisional controls are not met; they are listed as accepted gaps in `risk-acceptance-register.md`, not removed from the contract.
