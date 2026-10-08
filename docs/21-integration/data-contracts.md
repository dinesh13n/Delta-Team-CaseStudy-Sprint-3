# Data contracts

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-H-06 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Entities, keys and patterns come from `semantic-layer/entities.yaml`; curated layer adds `load_id` and `source_row`; quarantine rows carry rule ids. Schemas for AI output and audit events are v1.1 in `data/contracts/schemas/`. Fixture is immutable.
