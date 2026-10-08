# Grounding results

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (deterministic provider) |
| Evidence sources | EVD-J-03 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Method: for every non-abstained summary, extract shipment ids, event counts, booking counts and the highest retry_count and compare with the case facts. Result: **0 unsupported claims in 192 cases** (both runs). Every non-abstained output lists its sources (`source_count >= 1`).
Limit [INF]: the deterministic provider can only state what it computes, so zero hallucination is by construction, not evidence about a language model. Groundedness of a real model must be re-measured with the same harness.
