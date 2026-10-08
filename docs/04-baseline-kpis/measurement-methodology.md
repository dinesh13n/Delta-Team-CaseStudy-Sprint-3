# Measurement Methodology

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 4 KPI baseline) |
| Runbook step | C1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | evidence/04-baseline-kpis/EVD-C-05-data-profile.json; evidence/04-baseline-kpis/EVD-C-05-profile.py |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- All figures are computed by `evidence/04-baseline-kpis/EVD-C-05-profile.py` (read-only; run with `python -I`, writing outside `data/`).
- Percentiles use the index method `sorted(v)[int(p/100*n)]`. Linear interpolation gives p95 = 13,707 ms; the 2 ms difference is recorded in EVD-A-06.
- Test and coverage figures come from `pytest --cov` in a throwaway venv on a copy of the subtree (EVD-C-03).
- The source files carry the A1 baseline hashes (verified before and after each run).
- The measurement period is unknown because the fixture has no usable time span (impossible timestamps present).
