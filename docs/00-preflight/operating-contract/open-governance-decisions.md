# Open Governance Decisions

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

| ID | Decision needed | Who | Blocks | Default in use | Linked |
|---|---|---|---|---|---|
| GOV-01 | Named approvers for all role slots | Business Sponsor | gates from B2 | operator self-approves PROVISIONAL | OQ-05 |
| GOV-02 | Authorisation to modify the repository | CTO | Stage H onward | none; hard stop | OQ-11 |
| GOV-03 | Target platform | Architecture | F1, H3, M1, N1 | sandbox only | OQ-01 |
| GOV-04 | The two models for the comparison | AI Governance | J1, J3 | none | OQ-02 |
| GOV-05 | Network egress policy | Security | J1, M1, Q1 | allowlist as found | OQ-03 |
| GOV-06 | Regulatory obligations and location-data limits | Compliance | K4, D4 | none | OQ-04, OQ-21 |
| GOV-07 | Repository visibility (currently public, holds training PDFs and planted credential-shaped values) | Operator | none | public | new, from risk R-12 |
| GOV-08 | Evidence retention | Compliance | A2, K4 | in-repo, hash-manifested | OQ-10 |
| GOV-09 | Time budget and team size | Transformation Lead | E3, I2 | none stated | OQ-12, OQ-23 |
| GOV-10 | Independent review of self-approved gates | CTO | final gate | none | new |

## Update 2026-10-08 (Runbook 04)
The operator recorded decisions for the linked questions (`docs/44-decisions/open-questions-register-v2.md`, evidence `EVD-T-01`). Status of the governance items:

| ID | Status now | Note |
|---|---|---|
| GOV-01 | Decided (OQ-05): the operator approves all roles, provisionally | still not independent |
| GOV-02 | Ratified by the operator (OQ-11) | CTO ratification still recommended |
| GOV-03 | Decided: platform-neutral (OQ-01) | |
| GOV-04 | Decided: no model (OQ-02) | |
| GOV-05 | Decided: no egress (OQ-03) | |
| GOV-06 | Decided: no regime named, no location limits stated (OQ-04, OQ-21) | candidate set unvalidated |
| GOV-07 | **Decided: repository private** | was public; history still holds the values |
| GOV-08 | Ratified: evidence in the repository, hash-manifested (OQ-10) | |
| GOV-09 | Decided: demo budget 10+5; team is one operator plus the agent; engagement deadline unknown (OQ-12, OQ-23) | |
| GOV-10 | Open | independent review still absent |
