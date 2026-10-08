# Operability, contract and reproducibility

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

**Behaviour.** /health, /ready, /metrics; OpenAPI served at /openapi.json must equal the published contract for paths and schemas (contract test). Install and test from a clean checkout with a hashed lock file; README gives one correct run command.
**State.** None.

**Requirements.** FR-15, FR-16, FR-17, FR-20. **Findings addressed.** F-02, F-03, F-04, F-07, F-46, F-50. **Acceptance criteria.** see `../acceptance-criteria.md`.
