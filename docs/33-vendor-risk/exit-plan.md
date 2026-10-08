# Exit plan

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (plan for each critical vendor) / CONDITIONAL (vendors not yet chosen) |
| Evidence sources | docs/30-release/backup-validation.md; evidence/30-release/EVD-N-03-backup-restore.json |
| Assumptions | See body |
| Unresolved issues | vendor choices |
| Residual risks | N-R-18 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

N-X7: an exit plan for every critical vendor. The critical vendors do not exist yet; the plans below are conditions for adopting them.

| Vendor class | Exit trigger | Exit steps | Data to retrieve | Time estimate |
|---|---|---|---|---|
| Model provider | price rise, quality drop, policy/contract breach, outage pattern | set `AI_ENABLED=false` or `AI_PROVIDER=deterministic` (minutes); evaluate replacement; re-issue prompt lock | none stored at provider by contract (must be a contract term) | minutes to disable; weeks to replace |
| Platform | cost, availability, regulation | redeploy image elsewhere; restore from backup (EVD-N-03 pattern); re-point identity | audit, approvals, curated layers via backup archive | days [ASM] |
| IdP | outage, cost | AUTH_MODE fallback is **not** allowed in production (`legacy_header` refused); keep a second verified issuer | users/roles live at IdP | weeks [ASM] |
| GitHub | policy/outage | repository mirror and local clone; CI translation | full git history | days |

**Condition for adopting any critical vendor:** the contract must allow export of all customer data and deletion on exit; this repository cannot check that.
