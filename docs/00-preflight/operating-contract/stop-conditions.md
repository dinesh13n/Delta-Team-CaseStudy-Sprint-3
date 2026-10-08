# Stop Conditions

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

Work stops and the operator is told immediately when any of these occurs:
1. A step would modify a file inside the delivered subtree before OQ-11 authorisation.
2. `git diff baseline/v0.1-as-delivered-bytes -- 07-logistics-shipment-fleet-routing-ops/` is not empty, or a manifest hash fails.
3. Evidence for a claim cannot be produced; the claim is recorded as Unknown, not asserted.
4. A real credential, personal data or production endpoint is found.
5. A command requires deleting, overwriting or force-pushing existing content.
6. A tool or network call is refused by policy; the agent does not retry by another route.
7. A finding in the runbook is contradicted by measurement (continue after logging; stop if it changes the plan).
8. A blocking open question (OQ-01, 02, 03, 05, 11) is needed by the next step and has no default.
9. The operator asks to stop.
