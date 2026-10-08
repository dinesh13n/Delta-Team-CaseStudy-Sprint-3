# Data traceability

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-E-03; EVD-F-04; acceptance-criteria.md |
| Assumptions | See body |
| Unresolved issues | Test files are PLANNED (written in Stage H/J/L); no test result is claimed here |
| Residual risks | See coverage-gap-register.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Data requirement | Finding(s) | Rule | Test | Oracle |
|---|---|---|---|---|
| FR-02 | F-30 | feat-01 | AC-03 | EVD-D-05-rule-baseline.json |
| FR-06 | F-33 | feat-03; DQ-01 | AC-08, AC-10 | EVD-D-05-rule-baseline.json |
| FR-06 | F-34 | DQ-02 | AC-08 | EVD-D-05-rule-baseline.json |
| FR-06 | F-35 | DQ-03 | AC-08 | EVD-D-05-rule-baseline.json |
| FR-06 | F-36 | DQ-05 | AC-08 | EVD-D-05-rule-baseline.json |
| FR-06 | F-37 | semantic-layer | semantic-layer tests (16 pass) | EVD-D-05-rule-baseline.json |
| FR-06, FR-08 | F-38 | DQ-08 | AC-08, AC-11 | EVD-D-05-rule-baseline.json |
| FR-06 | F-39 | DQ-07 | AC-08 (flag) + resilience tests | EVD-D-05-rule-baseline.json |
| FR-06 | F-40 | feat-03 | AC-08 | EVD-D-05-rule-baseline.json |
| FR-07 | F-41 | feat-03 | AC-10 | EVD-D-05-rule-baseline.json |
| FR-07 | F-54 | synthetic-data-strategy | AC-10 | EVD-D-05-rule-baseline.json |
| FR-06 | F-58 | DQ-08 | AC-08 | EVD-D-05-rule-baseline.json |
| FR-06 | F-59 | BR (weights) | AC-08 | EVD-D-05-rule-baseline.json |
| FR-06 | F-61 | DQ-04 | AC-08 | EVD-D-05-rule-baseline.json |
| FR-06 | F-62 | BR-K-* | AC-08 | EVD-D-05-rule-baseline.json |

Baseline counts per rule are frozen in `evidence/11-data-context/EVD-D-05-rule-baseline.json`; ETL tests must reproduce them exactly on the fixture and then show zero in curated.
