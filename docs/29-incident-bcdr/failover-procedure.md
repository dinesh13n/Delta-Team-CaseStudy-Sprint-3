# Failover procedure

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT APPLICABLE (justified) / CONDITIONAL |
| Evidence sources | apps/api/audit_chain.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

There is one process with file-based state; there is no second instance to fail over to. Honest statement: **no failover capability exists.** The substitute is fast restart (seconds) and rebuild-and-restore (DR plan). Introducing a second instance requires moving audit/approvals to a shared store (otherwise two chains diverge) and moving the rate limit and breaker state to shared or per-instance semantics. That design belongs to the platform decision (OQ-01).
