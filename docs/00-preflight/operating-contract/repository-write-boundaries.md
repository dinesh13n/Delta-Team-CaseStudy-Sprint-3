# Repository Write Boundaries

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

## 1. Stages A to G (now)
| Location | Write? | Rule |
|---|---|---|
| `07-logistics-shipment-fleet-routing-ops/**` | **No** | Frozen. Check: `git diff baseline/v0.1-as-delivered-bytes -- 07-logistics-shipment-fleet-routing-ops/` must be empty |
| `docs/**`, `evidence/**`, `semantic-layer/**` | Yes, additive | New files and appends only; evidence is never overwritten (new numbered file instead) |
| `runbook/**` | Yes, corrections only | Each change logged in decision-log.md |
| Root `.gitignore`, `.gitattributes`, `README.md` | Yes, minimal | Logged |
| Training PDFs, rubric image, `Prompts-Guidlines/` | **No** | Reference material |

## 2. Stage H onward
Unlocked only when the Repository Owner (UNRESOLVED) or the CTO gives written authorisation (OQ-11, Step G4). Until then no commit may touch the subtree.

## 3. Mechanics
- The agent writes files on the operator's machine; the **operator runs `git commit` and `git push`** (cloud session cannot push, EVD history; decision with operator).
- Commit messages name the runbook step (for example "Stage A step A5: ...").
- Tags are annotated and never moved or deleted.
- Force-push, history rewrite and branch deletion are prohibited without explicit approval (see provisional-human-approval-rules.md).
