# Regression results

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-H-10, EVD-H-11-pytest-coverage |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Baseline (Stage C): 2 original tests + 12 characterization tests, coverage 45%.
After: those 14 tests all accounted for (5 pass, 7 approved-change xfail, 2 adapted pass); 79 new tests added (93 collected in total: 86 pass + 7 xfail). Zero regressions as defined in H10: no difference without an approved-change ID. Data fixtures are byte-identical to the baseline (hash manifest). Details: `behavior-difference-report.md`.
