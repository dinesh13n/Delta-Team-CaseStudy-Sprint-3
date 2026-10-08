# Go / no-go criteria

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | docs/26-tevv/tevv-release-gate.md; docs/25-governance/risk-acceptance-register.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-11 criteria could be bent after the fact; they are fixed here and committed before R1 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Criteria are fixed here **before** the R-stage decision. Current state is the repo-level state on 2026-10-08. A "GO" needs every mandatory row PASS.

| # | Criterion | Mandatory | Current state |
|---|---|---|---|
| G1 | All automated tests pass; coverage ≥ floor | yes | PASS: 170 passed, 7 xfailed (approved changes), 97% |
| G2 | Evaluation at or above J2 thresholds, no safety-class failures | yes | PASS for deterministic provider; model not tested (no model) |
| G3 | Red team: no original defect re-exploitable | yes | PASS: 10 of 12 attacks succeeded on baseline, 0 of 12 on v2 |
| G4 | No known critical/high vulnerability in runtime dependencies | yes | PASS: pip-audit 0 findings (runtime locks); 12 bandit findings triaged in M1 |
| G5 | Audit tamper-evident, reconstruction demonstrated | yes | PASS (author-run) |
| G6 | Backup restore demonstrated | yes | PASS at repo level; platform OPEN |
| G7 | Rollback defined and rehearsed | yes | PARTIAL: defined; rehearsed only as backup restore and `git revert` reasoning |
| G8 | Alerts routed to named humans | yes | **FAIL**: no recipients (OQ-05) |
| G9 | Named approver for go and named owner for each accepted risk | yes | **FAIL**: 0 of 12 risk acceptances signed |
| G10 | Target platform and identity provider exist | yes for production | **FAIL**: OQ-01, OQ-07 |
| G11 | Independent review of the evidence | yes | **FAIL**: none done (TEVV-R-01); author graded own work |
| G12 | Compliance obligations resolved | yes for real data | **FAIL/UNRESOLVED**: RA-01 |

## Reading
For a **pilot on synthetic data in a controlled environment**, G1 to G7 are the relevant set and are met at repo level. For **production on real data**, G8 to G12 are open and the decision cannot be GO. Detailed decision in R1.
