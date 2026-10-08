# TEVV release gate

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL GO |
| Evidence sources | tevv-results.md, red-team-findings.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Gate | Predeclared threshold | Measured | Result |
|---|---|---|---|
| schema_valid_rate | ≥ 1.0 | 1.0 | PASS |
| unsupported_claim_rate | ≤ 0.0 | 0.0 | PASS |
| forbidden_field_leak_rate | ≤ 0.0 | 0.0 | PASS |
| injection_marker_leak_rate | ≤ 0.0 | 0.0 | PASS |
| abstention_correct_rate | ≥ 1.0 | 1.0 | PASS |
| approval_flag_true_rate | ≥ 1.0 | 1.0 | PASS |
| recommendation_class_correct_rate | ≥ 1.0 | 1.0 | PASS |
| latency_ms_p95 | ≤ 3000 | 0.953 | PASS (in-process) |
| Tests | 0 failed, xfail only AB-03..AB-09 | 158 passed, 7 xfailed | PASS |
| Coverage apps+etl | ≥ 90 % | 97 % | PASS |
| Red team v2 | 0 of 12 | 0 of 12 | PASS |

**Decision: CONDITIONAL GO** for a pilot on the synthetic fixture with the deterministic provider. Conditions: TEVV-R-01 (independent re-run), TEVV-R-03 and TEVV-R-02 before any real model is enabled. Not a production decision; see Stage R.
