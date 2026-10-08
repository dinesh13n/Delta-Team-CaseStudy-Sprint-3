# Evidence Contract (operating-contract copy)

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

This contract adopts `docs/EVIDENCE-CONTRACT.md` unchanged. Summary of the rules that bind this phase:
1. Every artifact begins with the mandatory header (Stage, Runbook step, Version, Date, Author/Agent, Status, Evidence sources, Assumptions, Unresolved issues, Residual risks).
2. Every statement is classified Verified Fact, Inference, Assumption or Unknown, with a file path or evidence ID.
3. Raw evidence is stored as `evidence/<NN-stage>/EVD-<step>-<n>-<slug>.<ext>`, listed in that folder's MANIFEST.md with SHA-256, producing step, command, UTC time, operator and citing artifact.
4. Evidence is append-only; a re-run creates a new numbered file (as done for EVD-A-03b/c/d/e).
5. Baselines are tagged and never moved: `baseline/v0.1-as-delivered-bytes` is the byte-exact reference.
6. A step is complete only when its exit criteria are met and evidence exists; otherwise the gap is recorded, never hidden.
