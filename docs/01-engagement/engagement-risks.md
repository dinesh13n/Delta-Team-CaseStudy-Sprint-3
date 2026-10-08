# Engagement Risks

| Field | Value |
|---|---|
| Stage | B: Qualification, Stakeholders and Problem Framing (Spine 1) |
| Runbook step | B1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/ (A4, A5, A6 packs); runbook/04-OPEN-QUESTIONS-REGISTER.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Risk | Likelihood | Impact | Mitigation owner |
|---|---|---|---|---|
| ER-1 | Self-approved gates lack independence | High | Med | CTO (GOV-10) |
| ER-2 | Cannot run a real second-model comparison without model access | High | High (rubric 2) | AI Governance Owner UNRESOLVED |
| ER-3 | Effort pulled to governance findings at the expense of the working app (rubric 4) | Med | High | Transformation Lead |
| ER-4 | Public repo exposes training material and planted credentials | Med | Med | Operator (GOV-07) |
| ER-5 | Python 3.14 target breaks pinned dependencies | High | Med | Transformation Lead |
| ER-6 | Runbook contains other wrong figures | Med | Med | Transformation Lead |
| ER-7 | No deployment platform means no real release evidence | High | High | Architecture UNRESOLVED |
