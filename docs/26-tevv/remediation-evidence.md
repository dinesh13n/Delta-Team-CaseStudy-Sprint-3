# Remediation evidence

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-J-03 run1/run2, EVD-L-02, EVD-L-03, EVD-M-02 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Defect | Found by | Fix | Verification |
|---|---|---|---|
| DEF-L-01 forbidden values appeared in summaries (rate 0.1094) | J3 run 1 | gateway `_forbidden_values` + `_leaks`: any output containing a forbidden value becomes a fallback with reason `output_policy_violation` | run 2: 0.0; `tests/test_ai_remediation.py` |
| DEF-L-02 injected text reached output (rate 0.4651) | J3 run 1 | sanitiser: NFKC normalisation, Cf/zero-width stripping, `<`/`>` escaping; categorical fields only via `clean_enum` allow-list, anything else becomes `[unrecognised]` | run 2: 0.0; RT-08 live on v2 |
| DEF-L-03 model dependency could hang the request | M2 design | `resilience.py` timeout + circuit breaker wired in the gateway (`provider_timeout`, `circuit_open`) | `tests/test_resilience.py` (9 tests) |
| DEF-L-04 prompt could change without notice | K2 | `prompts.lock.json` + `PromptIntegrityError` at load | `tests/test_prompt_lock.py` |

Re-test after remediation: L2 final run (all thresholds pass) and L3 v2 campaign (0 of 12). Evidence: `evidence/26-tevv/EVD-L-02-final-eval-run.json`, `evidence/26-tevv/EVD-L-03-redteam-v2.json`.

[VF] No threshold or dataset was changed to obtain a pass (checksums in `tevv-results.md`).
