# Provisional Tool and Agent Permissions

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

| Capability | Permission now | Notes |
|---|---|---|
| Read repository files | Allowed | all stages |
| Write new files under docs/, evidence/, semantic-layer/ | Allowed | additive |
| Edit the delivered subtree | **Denied** | until OQ-11 |
| Run shell commands in sandbox | Allowed | outside the repo tree for probes |
| Run shell on operator machine | Allowed within connected folder | deletes denied by default; operator approval for deletion |
| `git commit`, `git push`, tags | **Operator only** | agent prepares commands |
| Install packages | Allowed in throwaway venv / user-level uv | not global |
| Web search/fetch | Allowed for public documentation | no repository content sent |
| Create or modify cloud resources | **Denied** | no platform chosen (OQ-01) |
| Call external AI models with repository data | **Denied** | models not chosen (OQ-02) |
| Scheduled tasks or background agents | Denied | not needed in Stage A to G |
| Memory writes | Only on explicit user request | privacy rules apply |

Agent identity for evidence: "Claude agent for Dinesh". Permissions re-confirmed at every stage gate.
