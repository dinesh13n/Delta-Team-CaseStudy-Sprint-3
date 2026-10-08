# Cutover checklist

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (not executable) |
| Evidence sources | evidence/30-release/EVD-N-03-backup-restore.json (SHA-256 a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-09 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Each line is a check with its evidence; none has been performed against a real environment. Status column: DONE (repo-level evidence), OPEN.

| # | Check | Evidence | Status |
|---|---|---|---|
| 1 | CI green on the release commit | GitHub Actions run | OPEN (never ran) |
| 2 | Image built from tag; digest recorded; scan and SBOM attached | registry | OPEN |
| 3 | Secrets present in platform secret store; none in image or repo | secret scan; platform | scan DONE, platform OPEN |
| 4 | Production secret ≥ 32 chars, distinct from every earlier value | platform | OPEN |
| 5 | H3 credentials exposed in git history revoked (P-X5) | provider consoles | OPEN: owner action |
| 6 | Data load published; `/ready` 200; `X-Data-Load-Id` present | smoke | OPEN |
| 7 | Backup taken; restore rehearsed in staging | backup-validation.md | repo-level DONE, staging OPEN |
| 8 | Alerts routed to a named recipient | alertmanager | OPEN (OQ-05) |
| 9 | AI kill switch tested on the deployed instance | smoke | OPEN |
| 10 | Rollback tag and previous image digest recorded | release-approvals.md | OPEN |
| 11 | Approvers recorded (go/no-go) | release-approvals.md | OPEN |
| 12 | Risk acceptances RA-01..RA-12 signed or consciously open | risk-acceptance-register.md | OPEN: 0 of 12 signed |
