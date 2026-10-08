# Confidence handling

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/ai/gateway.py, tests/test_human_control.py, EVD-J-03 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Situation | Behaviour | Where |
|---|---|---|
| Deterministic provider | confidence fixed by rule; always valid | provider |
| Model confidence < 0.5 | `abstained: true`, `abstain_reason: low_confidence`, `recommendation: null`, still `requires_human_approval: true` | gateway; `test_low_confidence_model_output_becomes_an_abstention` |
| Confidence missing or outside 0..1 | schema invalid, fallback `schema_invalid` (BR-08) | gateway |
| Context too thin to summarise (no events, missing status) | abstain `insufficient_context` | eval abstention cases, rate 1.0 |
| Provider timeout / error / breaker open | fallback to deterministic output with the reason in `fallback_reason` | `resilience.py`, gateway |

[ASM] The 0.5 floor is a starting value (model-configuration). It must be re-set from a measured calibration curve once a real model exists; none can be measured now.
