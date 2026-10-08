# Data Use Constraints

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

## 1. Data classification [VF]
- All data in `data/synthetic/` is declared synthetic (`data/README.md`, `data/quality_issues.json`). Treated as non-personal but **not** publishable beyond the repository without owner view, because location and driver identifiers resemble personal data (OQ-21).

## 2. Constraints
- No real operational, customer or personal data may enter the repository or any prompt.
- The planted credential-shaped values (`Welcome123`, `sk-workshop-hardcoded-example`, `replace-me-but-currently-shared`, `legacy-batch-password`) are fictitious; they must never be reused anywhere else.
- Data is read in place; no copy of fixtures is made outside the subtree except aggregate statistics in `evidence/`.
- Defects in the data (duplicate keys, blanks, `REC-0001` collision) are preserved as-found until Stage H and the owner decision (OQ-14, OQ-15).
- Retention: evidence retained in repository history; period set by Compliance Owner (OQ-10 defaulted, D-002).
- AI invocations in Stage A to G: none made with repository records beyond the agent's own reading.
