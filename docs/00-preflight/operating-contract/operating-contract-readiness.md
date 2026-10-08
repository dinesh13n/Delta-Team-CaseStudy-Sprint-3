# Operating Contract Readiness

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

## 1. Checklist
| Check | Result |
|---|---|
| Twelve artifacts present | Yes |
| Mandatory header on each | Yes |
| Every owner marked PROVISIONAL or UNRESOLVED | Yes; none invented |
| Write boundaries stated and checkable | Yes (git diff against v0.1 tag) |
| Stop conditions stated | Yes |
| Items flagged for confirmation at later Spine stages | Listed below and in EVD-A-05 |

## 2. Items flagged for confirmation
| Spine stage | Folder | Item to confirm |
|---|---|---|
| 2 | docs/02-stakeholders | Named holders for all eight role slots (GOV-01) |
| 23 | docs/23-human-control | Human-approval triggers and autonomy limits (provisional-human-approval-rules.md) |
| 25 | docs/25-governance | Change control, evidence retention, independent review (change-control-rules.md, GOV-08, GOV-10) |
| 37 | docs/37-operating-model | Environment and access boundaries, platform (environment-access-boundaries.md, GOV-03) |

## 3. Verdict
Ready to govern **read-only Stages A to G**. **Not** ready to govern Stage H onward: write authorisation (OQ-11) and named approvers (OQ-05) are missing. Status stays PROVISIONAL.
