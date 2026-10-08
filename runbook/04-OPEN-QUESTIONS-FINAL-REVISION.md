# Open questions: final revision (decisions recorded 2026-10-08)

| Field | Value |
|---|---|
| Stage | T (Runbook 04 execution; supersedes the Stage R5 revision) |
| Version | v2.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5); decisions by the operator, Dinesh |
| Status | All 23 questions decided, ratified or deferred by the operator; not independently confirmed |
| Evidence sources | evidence/44-decisions/EVD-T-01-operator-decision-record.json; docs/44-decisions/open-questions-register-v2.md |
| Unresolved issues | OQ-07 deferred; OQ-15 intent unknown; engagement deadline unknown; independent review absent (GOV-10) |
| Residual risks | One person holds every role |

Final status of every question in `04-OPEN-QUESTIONS-REGISTER.md`. The register's rule: a question is closed when an owner records a decision with a date. The operator recorded all of them on 2026-10-08 under the provisional authority decided in OQ-05. Counts: 15 decided, 7 ratified, 1 deferred, 0 open. **R-X9 is met on that rule, and the limit is stated: nothing is confirmed by anyone independent.**

| OQ | Subject | Status | Decision | Source |
|---|---|---|---|---|
| OQ-01 | Target platform | DECIDED | Stay platform-neutral. No cloud or runtime is named. | Round A, answer 2 |
| OQ-02 | Model A and Model B | DECIDED | No model is used. The deterministic provider stays the only provider. | Round A, answer 3 |
| OQ-03 | Network egress | DECIDED | No network egress from the application. Build and demo run offline. | Round A, answer 3 |
| OQ-04 | Regulatory obligations | DECIDED | No regime is named. The candidate obligations set stays an unvalidated working assumption. | Round B, answer 2 |
| OQ-05 | Stakeholders and approvers | DECIDED | The operator (Dinesh) approves everything as Transformation Lead, under provisional authority. No other named party exists. A CTO review stays recommended. | Round A, answer 1 |
| OQ-06 | Operator portal in scope | RATIFIED | A thin read-only operations view, not an Angular portal. Previously RESOLVED (provisional). | Round D |
| OQ-07 | Identity provider | DEFERRED | No provider chosen. HS256 stays an interim scheme, not for production; JWKS stays a fail-closed stub. | Round C, answer 1 |
| OQ-08 | Proxy KPIs acceptable | RATIFIED | The labelled proxy KPIs are accepted as the frozen baseline. No real business data exists. | Round B, answer 4 |
| OQ-09 | Financial data for ROI | DECIDED | No financial data. The benefit model stays in analyst-hours with sensitivity ranges and no money figure. | Round B, answer 4 |
| OQ-10 | Evidence retention | RATIFIED | Evidence stays in the repository, hash-manifested and version-controlled. | Round D |
| OQ-11 | Authorisation to write | RATIFIED | The operator ratifies, in their own name, the write authorisation given as instruction D-009. A CTO ratification stays recommended. | Round A, answer 1 |
| OQ-12 | Time budget | DECIDED | Demo budget is 10 minutes plus 5 minutes of questions. No engagement deadline was stated. | Round A, answer 4 |
| OQ-13 | Discovery folder collision | RATIFIED | The spine path `docs/00-preflight/discovery/` is authoritative. | Round D |
| OQ-14 | Data remediation location | RATIFIED | A derived curated layer; the fixture in `data/synthetic/` stays immutable. | Round D |
| OQ-15 | REC-0001 collision intent | DECIDED | Handling decided: treat as a defect (lookup logic fixed, bad-key rows quarantined). The data owner's intent is UNKNOWN. | Round C, answer 2 |
| OQ-16 | Demo environment | DECIDED | Local, offline, deterministic provider. | Round A, answer 4 |
| OQ-17 | Demo format and budget | DECIDED | 10 minutes plus 5 of questions, live and offline. This differs from the register default of 20 plus 10, and the difference is now a recorded decision. | Round A, answer 4 |
| OQ-18 | Agentic AI in scope | DECIDED | Not in scope. J6 stands as not-applicable. | Round C, answer 3 |
| OQ-19 | Secret history disposition | DECIDED | Keep history unrewritten; treat the values as compromised; the repository is private. Nothing real exists to revoke: they are workshop placeholders, and none may be reused anywhere. | Round B, answer 1; repository set private by the operator |
| OQ-20 | Real deployment or readiness | DECIDED | Readiness decision only. Nothing is deployed. | Round B, answer 3 |
| OQ-21 | Location data constraints | DECIDED | No limits stated. The minimisation default stays: location fields masked and excluded from prompts and from logs above INFO. | Round B, answer 2 |
| OQ-22 | Clean-repo contract retention | RATIFIED | The original sanity_check assertions stay unchanged. | Round D |
| OQ-23 | Team size and skills | DECIDED | One operator plus the agent; sequential execution. | Round C, answer 4 |

Meaning of each decision, what changes if it is reversed, and the residual gap: `docs/44-decisions/open-questions-register-v2.md`. What an independent signer can add: `docs/44-decisions/cto-signoff-pack.md`.
