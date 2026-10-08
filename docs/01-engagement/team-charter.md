# Team Charter

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

## Mission
Take the delivered repository to a production-ready state, proving every claim with evidence stored in `evidence/`.

## Team (PROVISIONAL)
| Role | Holder |
|---|---|
| Transformation Lead and executing engineer | Dinesh |
| Execution agent | Claude Code agent (claude-sonnet-5-5), acts only inside the operating contract |
| All other role slots | UNRESOLVED (docs/00-preflight/operating-contract/provisional-operating-contract.md) |

## Working agreements
- Follow runbook 02 in stage order; close each step with the required final response.
- Corrections to the runbook are logged in `decision-log.md`.
- Commits name the runbook step; the agent pushes to `main` of `dinesh13n/Delta-Team-CaseStudy-Sprint-3` (push scope granted 2026-10-08).
- Stop conditions: docs/00-preflight/operating-contract/stop-conditions.md.
