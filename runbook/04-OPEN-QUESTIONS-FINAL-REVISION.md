# Open questions: final revision at Step R5

| Field | Value |
|---|---|
| Stage | R |
| Runbook step | R5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | runbook/04-OPEN-QUESTIONS-REGISTER.md; docs/00-preflight/operating-contract/open-governance-decisions.md |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Final status of every question in `04-OPEN-QUESTIONS-REGISTER.md`. R-X9 asks for each to be resolved or **formally accepted by an owner**. Only RESOLVED rows are closed; "RESOLVED (provisional)" means the engagement chose an answer that its owner has not confirmed. No question is formally accepted by a named person.

| OQ | Subject | Final status | Basis | Owner role |
|---|---|---|---|---|
| OQ-01 | Target platform | OPEN | default: platform-neutral container (ADR-0009); nobody accepted | Architecture (UNRESOLVED) |
| OQ-02 | Model A and Model B | OPEN | no real model; Stage Q not performed | AI governance (UNRESOLVED) |
| OQ-03 | Network egress | OPEN | default: none; no model called | Security (UNRESOLVED) |
| OQ-04 | Regulatory obligations | OPEN | recorded as accepted-unresolved RA-01, unsigned | Compliance (UNRESOLVED) |
| OQ-05 | Stakeholders and approvers | OPEN | operator self-approves PROVISIONAL; G9 FAIL | Business sponsor (UNRESOLVED) |
| OQ-06 | Operator portal in scope | RESOLVED (provisional) | thin read-only view built; Angular portal rejected | Product (UNRESOLVED) |
| OQ-07 | Identity provider | OPEN | HS256 interim (ADR-0004); JWKS stub | Security (UNRESOLVED) |
| OQ-08 | Proxy KPIs acceptable | ASSUMED | used as proxies throughout; sponsor never confirmed | Business sponsor (UNRESOLVED) |
| OQ-09 | Financial data for ROI | OPEN | ROI/NPV parameterised in analyst-hours; no money | Business sponsor (UNRESOLVED) |
| OQ-10 | Evidence retention | OPEN | in-repo, hash-manifested | Compliance (UNRESOLVED) |
| OQ-11 | Authorisation to write | CONDITIONAL | operator instruction D-009; CTO ratification pending; EVD-G-04 unsigned | CTO (not named) |
| OQ-12 | Time budget | ASSUMED | none stated; demo 10 min proposed | Transformation lead |
| OQ-13 | Discovery folder collision | RESOLVED | D-001 | Transformation lead |
| OQ-14 | Data remediation location | RESOLVED (provisional) | derived curated layer; fixture immutable | Data owner (UNRESOLVED) |
| OQ-15 | REC-0001 collision intent | OPEN | treated as an invalid key; owner intent unconfirmed | Data owner (UNRESOLVED) |
| OQ-16 | Demo environment | PROPOSED | local, offline, deterministic provider | SRE (UNRESOLVED) |
| OQ-17 | Demo format and budget | PROPOSED | 10 minutes + 5 questions | Transformation lead |
| OQ-18 | Agentic AI in scope | OPEN | J6 recorded not applicable | AI governance (UNRESOLVED) |
| OQ-19 | Secret history disposition | OPEN | history not rewritten; rotation planned; **nothing revoked**; repo public | Security (UNRESOLVED) |
| OQ-20 | Real deployment or readiness | RESOLVED (provisional) | readiness only; no deployment | CTO (not named) |
| OQ-21 | Location data constraints | OPEN | masking applied; retention/rights undefined (RA-10) | Compliance (UNRESOLVED) |
| OQ-22 | Clean-repo contract retention | RESOLVED | original sanity_check assertions retained (H-X10) | Transformation lead |
| OQ-23 | Team size and skills | OPEN | one operator and one agent | Transformation lead |

Counts: 2 resolved, 3 resolved provisionally, 5 assumed/proposed/conditional, 13 open (total 23). **R-X9 is NOT MET.**
