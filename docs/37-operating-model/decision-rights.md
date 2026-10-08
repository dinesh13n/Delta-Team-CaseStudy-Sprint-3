# Decision rights

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Decision | Decides | Needs |
|---|---|---|
| Go-live | Sponsor | go-no-go criteria; Release Manager recommendation |
| Enable a model | AI Governance Owner | TEVV on that model, red team, cost view |
| Accept a security risk | Security Owner | register entry; time-boxed |
| Accept a regulatory risk | Sponsor (A), Compliance (R) | RA-01 resolved or accepted |
| Disable AI | any on-call (kill switch) | no approval needed to disable; approval needed to re-enable |
| Change thresholds | AI Governance Owner | written reason; not after seeing a result (J-X2) |
| Revoke a credential | Security Owner or on-call on suspicion | immediately |
