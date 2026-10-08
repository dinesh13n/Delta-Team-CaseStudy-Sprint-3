# Provisional Human Approval Rules

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0B provisional operating contract |
| Runbook step | A5 (runbook/02-TRANSFORMATION-RUNBOOK.md, Stage A) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | **PROVISIONAL**, Draft pending named approvers (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/ (A4 pack); runbook/00-RUNBOOK-OVERVIEW.md section 6; runbook/04-OPEN-QUESTIONS-REGISTER.md; docs/00-preflight/operating-contract/decision-log.md |
| Assumptions | The operator acts for every role slot only to keep work moving; this is not an assignment of ownership |
| Unresolved issues | OQ-01, OQ-02, OQ-03, OQ-05, OQ-11 (blocking) |
| Residual risks | Every approval below is self-issued until named approvers exist |

Every owner, approver and decision right in this contract is **PROVISIONAL**. No owner has been invented. Where the table says UNRESOLVED, nobody has been assigned.

The operator is the only human available. Where an approval below needs a named owner, the operator records a PROVISIONAL self-approval and the item is queued for the real owner.

| Trigger | Approval needed | Approver now |
|---|---|---|
| First write inside `07-logistics-shipment-fleet-routing-ops/` | Written authorisation (OQ-11) | CTO / Repository Owner, UNRESOLVED; **hard stop** |
| Any `git push --force`, tag move, history rewrite (OQ-19) | Explicit approval | operator + Repository Owner UNRESOLVED |
| Changing repository visibility | Explicit approval | operator (owner of the account) |
| Choosing the platform, models, egress policy | Decision (OQ-01/02/03) | UNRESOLVED |
| Accepting a residual security risk | Security Owner | UNRESOLVED |
| Any call to an external AI model with repository content | AI Governance Owner | UNRESOLVED |
| Declaring a stage gate passed | Transformation Lead | operator, PROVISIONAL |
| Correcting the runbook | Operator approval, logged | operator (done for D-007/D-008) |
| Deleting a file on the operator machine | Operator prompt | operator |

Self-approval is flagged in every gate record so reviewers can see it was not independent.
