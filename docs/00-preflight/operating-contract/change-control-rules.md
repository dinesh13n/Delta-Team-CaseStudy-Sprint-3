# Change Control Rules

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

1. **Unit of change:** one runbook step per commit where practical; commit message begins "Stage <X> step <Y>:".
2. **Logging:** every decision, deviation or correction is added to `decision-log.md` with ID, basis and status (DECIDED, DEFAULTED, PROPOSED, RECORDED, APPLIED).
3. **Runbook edits:** allowed only to correct errors found during execution; each edit lists the changed files and is approved by the operator (precedent: D-007, D-008).
4. **Baseline protection:** the subtree diff against the v0.1 tag must be empty at every gate until Stage H.
5. **Contract amendments:** edit this folder, bump the version in the header, add a decision-log line; do not delete earlier text.
6. **Branching:** until Step H1 (CODEOWNERS, branch protection) work is on `main`; this is a known gap (F-08).
7. **Rollback:** by `git revert` on the operator machine; no history rewrite without approval.
