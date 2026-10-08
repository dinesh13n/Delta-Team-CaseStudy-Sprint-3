# Rollback strategy

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/14-transformation; characterization tests EVD-C-08 |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Level | Trigger | Action |
|---|---|---|
| R1 flag | behaviour doubt in a single feature | flip the flag in feature-flag-plan.md (not available for FF-05) |
| R2 revert | any unexplained characterization failure (the change was not the planned change) or failing gate | `git revert` the increment commit group |
| R3 tag | multiple increments suspect | check out the previous `v2-incN` tag |
| R4 baseline | total loss of confidence | check out `baseline/v0.1-as-delivered-bytes`; `sha256sum -c` proves byte identity |
Each H step ends with a verified rollback statement in the transformation log. Data rollback is trivial because the fixture is never modified (schema-migration-plan.md).
