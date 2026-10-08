# Environment and Access Boundaries

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

## 1. Environments
| Environment | Use | Access |
|---|---|---|
| Cloud sandbox (Ubuntu 22.04; Python 3.10/3.11/3.14; Node v26.11.1) | Analysis, scripts, probes | Agent; network via allowlist (OQ-03 undecided) |
| Operator Windows machine (Python 3.11.9 default, 3.14.7, 3.12; Node v26.8.1 unconfirmed) | Folder host; git commit/push | Operator; agent reaches only the connected folder |
| GitHub `dinesh13n/Delta-Team-CaseStudy-Sprint-3` (public) | Evidence store | Operator pushes; agent reads anonymously |
| Target platform | none chosen | OQ-01 UNRESOLVED |
| Production | none | **Prohibited**: no access, no credentials, no deployment |

## 2. Rules
- The agent holds no credentials for any system and must not request or store any.
- The agent does not run code from the delivered repository in Stage A. Execution starts in Stage C, in a throwaway virtualenv outside the repo, on Python 3.11 (decision-log D-006).
- Installs happen only in venvs under `/tmp` or the sandbox, never in the operator's global Python.
- No outbound call carries repository content to a third-party service other than the operator's own Claude session.
- The repository was public when this was written; it is now private (decision D-016, 2026-10-08). Nothing sensitive may be committed either way.
