# Model benchmark

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | BLOCKED for model comparison; baseline recorded |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | OQ-02, OQ-03 |
| Residual risks | DR-3 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Candidate models require OQ-02 (selection), OQ-03 (egress) and credentials; none exist. What was benchmarked: Model A = `deterministic 1.0`. Model B = none available. The harness (`evaluation/run_eval.py`) takes any `ModelProvider`, and the datasets are fixed, so Stage Q can compare fairly once a model exists.
No benchmark number for a language model is claimed.
