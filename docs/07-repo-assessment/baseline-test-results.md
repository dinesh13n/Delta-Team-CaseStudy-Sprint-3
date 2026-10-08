# Baseline Test Results (Step C3)

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 5-7) |
| Runbook step | C3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-C-03 |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

`httpx` and `pytest-cov` installed into the throwaway venv only; `requirements.txt` not changed.

| Check | Result | Evidence |
|---|---|---|
| `pytest -q` | **3 passed**, 1 deprecation warning, exit 0 | EVD-C-03-junit.xml |
| Coverage (apps, etl, legacy, scripts) | **45%** (98 statements, 54 missed) | EVD-C-03-coverage.xml |
| `make smoke` | ok, 6 CSV files, 3000 events, exit 0 | EVD-C-03-transcript.txt |
| `make etl` | processed 354, malformed 1, exit 0 | EVD-C-03-transcript.txt |
| Playwright spec | **not executed**: no Playwright runner or browser installed in the subtree; spec tests a page that does not exist (F-05, F-52) | none |

Per-module: apps/api/main.py 74% (role-check branch lines 13-17 not covered), ai_gateway 100%, audit 100%, domain_service 87%, etl 0%, legacy 0%, scripts 0%.

Findings confirmed: F-02, F-51 (the only characterization test asserts `isinstance(row, dict)`), F-52, F-54 (sanity_check passes only for exactly 354/3000).
