# Model comparison (Q2)

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT PERFORMED |
| Evidence sources | evidence/40-scale/EVD-Q-02-comparison.csv |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-02 |
| Residual risks | Lock-in and ambiguity risk remain unmeasured |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Result: NOT PERFORMED
Model B does not exist (see `semantic-layer-portability-test.md`). The scorecard in `EVD-Q-02-comparison.csv` holds the **Model A** column from recorded evidence and `NOT RUN` in the Model B column, so the structure and thresholds are fixed in advance. No comparison conclusion is drawn. [VF]

| Dimension | Model A (claude-sonnet-5-5) | Model B |
|---|---|---|
| Repository suite | 176 passed, 1 skipped, 7 expected xfail (Python 3.11, 2026-10-08) | NOT RUN |
| Red-team attacks that succeed | 0 of 12 (baseline: 10 of 12) | NOT RUN |
| Spec conformance, fidelity, code quality, latency, token cost | recorded in earlier stages; deterministic provider only, no real token cost | NOT RUN |

## What this means for the claims
- "The semantic layer is model-independent" is **a design claim**, supported by the absence of model-specific text and by schema validation, **not** by a second implementation. Do not present it as demonstrated. [INF]
- The corrective-action list the runbook expects from this step is empty, because no ambiguity can surface without a second interpreter. It is **not** evidence that the specs are unambiguous.
