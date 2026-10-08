# Event contracts

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | docs/12-specs/event-contracts.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Audit events (v1.1 schema) are the only emitted events. Saga state transitions are emitted through the same callback shape (`action: carrier.booking`, state, key, attempts); wiring the saga emitter to the audit sink is left to deployment composition [ASM]. No message broker exists.
