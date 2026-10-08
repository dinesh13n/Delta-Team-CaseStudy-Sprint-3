# AI exception summary (I9, suggest-only)

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

**Behaviour.** POST /ai/summarize/{id}: load record and recent events through the repository, filter by policy, reduce by `ai-context-policy.yaml`, build a prompt with untrusted values only in a delimited data block, call the ModelProvider, validate the output against `ai-summary-output.schema.json`. On schema violation, low confidence, or provider error: use the deterministic provider; if that is impossible return an abstention (200) or 503.
**State machine of a suggestion.** `suggested` -> `approved` | `rejected` (terminal). A second decision returns 409. `requires_human_approval` is always true; nothing is executed by the system.
**Agency level.** L0 (suggest only) [VF from E1].

**Requirements.** FR-09, FR-10, FR-11, FR-12, FR-17. **Findings addressed.** F-22, F-23, F-24, F-25, F-26, F-27, F-28, F-29. **Acceptance criteria.** see `../acceptance-criteria.md`.
