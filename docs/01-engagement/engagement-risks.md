# Engagement Risks

| Field | Value |
|---|---|
| Stage | B: Qualification (Spine 1) |
| Runbook step | B1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-01, OQ-02, OQ-03, OQ-05, OQ-11 (see open-qualification-questions.md) |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Risk | Likelihood / impact | Mitigation in runbook |
|---|---|---|---|
| ER-1 | Write authorisation is operator-only, not CTO | High / High | Recorded as PROVISIONAL at G4; CTO review of final gate (GOV-10) |
| ER-2 | No real model, so AI capability cannot be demonstrated against a real LLM | High / High | Local open-weights model default (OQ-02); state limits |
| ER-3 | Findings concentrate in governance while marks concentrate in a working application (R3 vs R4) | Medium / High | Protect J4 and R4 per runbook 03 section 4 |
| ER-4 | Public repo holds training material and planted credentials | Medium / Medium | GOV-07 |
| ER-5 | Runbook contains unverified numbers | Medium / Medium | Re-verify in Stage C; D-007 precedent |
| ER-6 | Python 3.14 target breaks pinned dependencies | Medium / Low | Baseline on 3.11; upgrade pins in Stage H |
| ER-7 | Scope (102 steps) exceeds available time | Medium / High | OQ-12 default time-boxing |
