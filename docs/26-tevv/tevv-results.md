# TEVV results

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (with limits) |
| Evidence sources | evidence/26-tevv/EVD-L-02-final-eval-run.json, evidence/19-intelligence/EVD-J-03-* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | TEVV-R-01, TEVV-R-03 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Dataset integrity (L-X2)
| File | Cases | SHA-256 on disk (L2) | SHA-256 in manifest | Match |
|---|---|---|---|---|
| golden.jsonl | 120 | `05f589b456bb14c18051ac6a75fbedbc65d3e1ced4663311505921f7fb75f08f` | same | yes |
| edge.jsonl | 20 | `ca27858cb6fbd95b385ede3f6564c76e7741a21793228d57e3da2394dc1709ba` | same | yes |
| adversarial.jsonl | 43 | `8f87fdf9e70649bb303f7d02d43b802de06c46d7476ba838b0a40c392aef7b6d` | same | yes |
| failure.jsonl | 9 | `a104558fe29a923d7cb3e201a7fc98bb2e98296aed053df94354d0aa64d3d5eb` | same | yes |
| thresholds.json | – | `6138f65ab436aa2fd6f827b1c4f2046b518f4b398d46d7307753643ed3e18a91` | n/a (declared 10:37:53Z, manifest built 10:38:22Z) | yes |

[VF] Evidence: `evidence/26-tevv/EVD-L-02-final-eval-run.json`.

## Final evaluation run (192 cases)
| Metric | Measured | Threshold | Result |
|---|---|---|---|
| pass rate golden / edge / adversarial / failure | 1.0 / 1.0 / 1.0 / 1.0 | – | – |
| schema_valid_rate | 1.0 | ≥ 1.0 | PASS |
| unsupported_claim_rate | 0.0 | ≤ 0.0 | PASS |
| forbidden_field_leak_rate | 0.0 | ≤ 0.0 | PASS |
| injection_marker_leak_rate | 0.0 | ≤ 0.0 | PASS |
| abstention_correct_rate | 1.0 | ≥ 1.0 | PASS |
| approval_flag_true_rate | 1.0 | ≥ 1.0 | PASS |
| recommendation_class_correct_rate | 1.0 | ≥ 1.0 | PASS |
| latency_ms p50 / p95 | 0.521 / 0.953 | p95 ≤ 3000 | PASS (in-process only) |
| tokens (estimate) mean / max | 277.0 / 524 | within envelope | n/a (estimate) |

## Test suite and coverage (this run)
| Item | Value |
|---|---|
| Result | 158 passed, 7 xfailed, 1 warning, Python 3.14.7 |
| xfail | AB-03..AB-09 (approved behaviour changes, each with a reason string) |
| Line coverage, `apps` + `etl` | 97 % (1430 statements, 42 missed) |
| Uncovered | `apps/api/services/ai_gateway.py` and `services/audit.py` (0 %: legacy shims kept for the characterisation tests), `main.py` error paths |

## History honesty
Run 1 (J3) **failed**: forbidden_field_leak_rate 0.1094 and injection_marker_leak_rate 0.4651. The system was changed (DEF-L-01, DEF-L-02 in `remediation-evidence.md`) and run 2 passed. This is the intended use of predeclared thresholds.

## Limits
- [VF] Latency is in-process only. No network, no model.
- [VF] No real model was evaluated. The result describes the deterministic provider, the sanitiser, the policy and the output checks.
- [VF] Resilience and business-outcome rows of the L1 plan are covered in Stage M and Stage O, not here.
