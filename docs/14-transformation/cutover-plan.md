# Cutover plan

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

There is no live production system [VF]; "cutover" means making the modern path the default in the repository. Per increment: (1) merge behind its flag with the default on the new path; (2) run TG-1..TG-9; (3) record the difference report entry; (4) tag `v2-incN` after the user's review. Legacy modes stay available through flags until their retirement trigger (coexistence-strategy.md). Real production cutover is out of scope until a platform and owners exist (OQ-01, OQ-05).
