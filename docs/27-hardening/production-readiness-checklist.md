# Production readiness checklist (hardening)

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | hardening-plan.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | Item | State |
|---|---|---|
| 1 | Identity provider with asymmetric keys | NOT DONE (OQ-07) |
| 2 | Secrets from a secret store, rotated | plan only; no store (OQ-01) |
| 3 | TLS and HSTS at the edge | NOT DONE (platform) |
| 4 | Image built, scanned, signed | NOT DONE |
| 5 | IaC for a real platform | **BLOCKED** (OQ-01) |
| 6 | CI executed on GitHub, branch protection on | NOT DONE |
| 7 | SBOM and dependency scan | DONE |
| 8 | Security tests automated | DONE (27 tests) |
| 9 | Independent security review | NOT DONE |
| 10 | Rate limits at the edge, WAF | NOT DONE |
| 11 | Backup and restore verified | see N3 |
| 12 | Monitoring and alerting live | code only (N1) |
| 13 | Rotation of the exposed baseline secrets | NOT DONE (owner unknown) |

Items 1-6, 9, 10, 13 are required before real data. They are the content of the "CONDITIONAL" in the Stage R decision.
