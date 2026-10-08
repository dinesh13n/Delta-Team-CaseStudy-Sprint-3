# Repository quality gate

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (CONDITIONAL on items in the gate) |
| Evidence sources | EVD-H-* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Criteria come from TG-1..TG-9 (`docs/14-transformation/transformation-gates.md`).

| Gate | Result | Evidence |
|---|---|---|
| TG-1 Characterization green or each difference APPROVED/reverted | PASS: 5 pass, 7 approved-change xfail, 0 unexplained | EVD-H-10 |
| TG-2 Unit and integration tests green | PASS: 86 passed, 7 xfailed (3.14 and 3.11) | EVD-H-11-pytest-coverage |
| TG-3 ruff and mypy clean | PASS | EVD-H-11-static-analysis |
| TG-4 Secret scan clean | PASS (tree 0); history 10 findings with documented disposition | EVD-H-03 |
| TG-5 Semantic-layer tests green | PASS: 16 passed | EVD-H-11-tg5-tg6 |
| TG-6 Fixture untouched | PASS for data files; 20 non-data files differ by design | EVD-H-11-tg5-tg6 |
| TG-7 Coverage >= 80% | PASS: 96% (apps + etl) | EVD-H-11-pytest-coverage |
| TG-8 Evidence produced and registered in MANIFEST.md | PASS after H12 registration (see gate) | MANIFEST.md files |
| TG-9 Contract route diff clean | PASS | EVD-H-09 |
| (extra) CI executed on the hosted platform | NOT RUN, CONDITIONAL | needs push |
