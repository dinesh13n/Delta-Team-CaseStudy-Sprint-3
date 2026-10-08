# TEVV plan

| Field | Value |
|---|---|
| Stage | L |
| Runbook step | L1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evaluation/thresholds.json, dataset_manifest.json, EVD-J-03, EVD-L-02 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | TEVV-R-01 (self-graded) |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Scope
Test, evaluation, verification and validation of the v2 system: deterministic behaviour (policy, ETL, KPIs, saga, audit), the one probabilistic surface (the AI summary gateway), security, privacy, resilience.

## Order of work (the order is the control)
| Step | Done at (UTC) | Artifact |
|---|---|---|
| Thresholds declared | 2026-10-08T10:37:53Z | `07-logistics-shipment-fleet-routing-ops/evaluation/thresholds.json` (sha `6138f65ab436aa2fd6f827b1c4f2046b518f4b398d46d7307753643ed3e18a91`) |
| Datasets built and manifest written | 2026-10-08T10:38:22Z | `evaluation/datasets/*.jsonl`, `dataset_manifest.json` |
| First evaluation run (J3) | after both of the above | `evidence/19-intelligence/EVD-J-03-eval-run1.json` (FAIL) |
| Remediation | after run 1 | sanitiser, enum allow-list, output leak check |
| Second run (J3) | after remediation | `EVD-J-03-eval-run2-after-remediation.json` (PASS) |
| Final TEVV run (L2) | 2026-10-08 (this stage) | `evidence/26-tevv/EVD-L-02-final-eval-run.json` |
| Red team (L3) | 2026-10-08 (this stage) | `evidence/26-tevv/EVD-L-03-redteam-baseline.json`, `…-v2.json` |

[VF] Thresholds were adopted **unchanged** from J2. They were not edited after run 1 failed; the system was changed instead.
[VF] The L1 stage did not create a second threshold file. One source of truth avoids the question "which one was predeclared".

## What is evaluated, and how
| Surface | Method | Pass rule |
|---|---|---|
| AI summary quality, groundedness, leakage, abstention, approval flag | `evaluation/run_eval.py` over 192 cases | `thresholds.json` |
| Deterministic behaviour | pytest, 158 passed + 7 xfailed (approved change) | all pass; xfail only for AB-03..AB-09 |
| Security | `tests/test_security_suite.py` (repeatable) and `scripts/red_team.py` (campaign) | 0 successful attacks against v2 |
| Resilience | `tests/test_resilience.py`, M3 drills | see Stage M |
| Business outcome | O1 | NOT demonstrable on the fixture (see Stage O) |

## Independence
[VF] The same agent wrote the system, the datasets and the runner. This is not independent verification. A human reviewer must re-run `python -m evaluation.run_eval` and spot-check cases. Recorded as TEVV-R-01.
