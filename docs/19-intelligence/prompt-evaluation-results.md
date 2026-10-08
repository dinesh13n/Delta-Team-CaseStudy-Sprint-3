# Prompt / output evaluation results

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Run 1 FAIL; Run 2 PASS after remediation |
| Evidence sources | EVD-J-03-eval-run1, EVD-J-03-eval-run2 |
| Assumptions | See body |
| Unresolved issues | Real-model behaviour unmeasured |
| Residual risks | DR-3 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Predeclared thresholds: `evaluation/thresholds.json`. Runner: `evaluation/run_eval.py`. Provider under test: deterministic (+ scripted fakes for failure cases). **No real model was called.**

| Metric | Threshold | Run 1 (10:38:32Z) | Run 2 (after fix) |
|---|---|---|---|
| schema_valid_rate | >= 1.0 | 1.0 PASS | 1.0 PASS |
| unsupported_claim_rate | <= 0 | 0.0 PASS | 0.0 PASS |
| forbidden_field_leak_rate | <= 0 | **0.1094 FAIL** (21 of 192) | 0.0 PASS |
| injection_marker_leak_rate (adversarial) | <= 0 | **0.4651 FAIL** (20 of 43) | 0.0 PASS |
| abstention_correct_rate | >= 1.0 | 1.0 PASS | 1.0 PASS |
| approval_flag_true_rate | >= 1.0 | 1.0 PASS | 1.0 PASS |
| recommendation_class_correct_rate | >= 1.0 | 1.0 PASS | 1.0 PASS |
| latency_ms_p95 (in-process) | <= 3000 | 1.09 PASS | 1.04 PASS |
| Pass rate by set | | golden 1.00, edge 1.00, adversarial 0.535, failure 0.889 | all 1.00 |

## What run 1 found (defects)
- **DEF-L-01 (S1-class, F-22).** The deterministic provider echoed categorical fields (`service_tier`, `event_type`) into the summary. The injection filter was a regex, so zero-width-split, homoglyph, `</data>`-close, brace-template, newline and JSON-break payloads passed through into the output (20 of 43 adversarial cases).
- **DEF-L-02 (F-22/F-23 class).** No output-side check: a provider that returns a forbidden-field value (customer id) was passed to the caller (1 of 9 failure cases).
## Remediation (kept as separate evidence)
Enum-gated echo (`clean_enum`: a value outside the declared vocabulary is replaced by `[unrecognised]` and never repeated); NFKC normalisation and removal of format characters before injection matching; output-side forbidden-value filter with fallback (`output_policy_violation`). Regression tests: `tests/test_ai_remediation.py` (5). Run 2: `EVD-J-03-eval-run2-after-remediation.json`. Run 1 is retained unedited (append-only).
