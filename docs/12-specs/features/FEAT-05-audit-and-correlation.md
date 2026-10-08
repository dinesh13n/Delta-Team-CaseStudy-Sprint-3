# Audit trail and correlation

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/09-initial-prd/functional-requirements.md; openapi.yaml |
| Assumptions | See body |
| Unresolved issues | See spec-readiness.md |
| Residual risks | Provisional |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Behaviour.** Middleware assigns the correlation id. Every protected request, every denial and every AI call writes an audit event conforming to `audit-event.schema.json`, chained by SHA-256. GET /audit/verify recomputes the chain and reports the first bad index. Audit write failure fails the request (fail-closed) for write-type actions and logs for read-type [ASM].
**State.** Append-only file; rotation by size is a deployment concern.

**Requirements.** FR-13, FR-14. **Findings addressed.** F-42, F-43, F-44, F-45. **Acceptance criteria.** see `../acceptance-criteria.md`.
