# Known limitations

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/42-executive/residual-risks.md |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. One agent built, tested and graded the system; no independent review. 2. No real model; AI quality, latency and cost with a model are unknown; portability untested. 3. All data is a synthetic fixture; datasets for evaluation are constructed. 4. No deployment: availability, capacity, restore on a platform, alert delivery are unmeasured. 5. Every owner is a role; no person approved anything. 6. Credentials removed from the tree remain in history of a public repository and are not revoked. 7. No business KPI exists; benefit is unproven. 8. Single-commit import means pre-registration of thresholds is shown by timestamps, not by git order.
