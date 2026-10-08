# Open questions register, version 2 (decisions recorded)

| Field | Value |
|---|---|
| Stage | T: Open questions and decisions (runbook/04-OPEN-QUESTIONS-REGISTER.md) |
| Runbook step | 04-3 (Doc 04 sections 1 and 6) |
| Version | v2.0 (supersedes the Stage R5 revision) |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5); decisions by the operator, Dinesh |
| Status | All 23 questions have a recorded decision; every decision is by one person under provisional authority |
| Evidence sources | EVD-T-01-operator-decision-record.json; runbook/04-OPEN-QUESTIONS-REGISTER.md; the Stage R5 revision |
| Assumptions | The operator may decide for every role slot because OQ-05 was decided that way; this is not an assignment of ownership to anyone else |
| Unresolved issues | None open; 1 deferred (OQ-07); intent unknown for OQ-15; engagement deadline unknown (OQ-12) |
| Residual risks | Single-person authority: no decision here has independent confirmation (GOV-10) |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Result
Register rule (Document 04 section 1): *a question is closed only when an owner records a decision with a date.* On 2026-10-08 the operator recorded a decision for all 23 questions: **15 decided, 7 ratified (an earlier provisional resolution confirmed), 1 deferred (OQ-07), 0 open.** Before: 13 open, 2 resolved, 3 resolved provisionally, 5 assumed, proposed or conditional.

## What this does and does not change
- **Does:** removes the ambiguity. Every default now has a dated decision behind it, so a reviewer can no longer say the gap was merely assumed. Exit criterion R-X9 is met on the register's own rule. [VF]
- **Does not:** make any gate independent. One person holds every role, so the decisions are as provisional as the approvals. An accepted gap is still a gap: the rubric marks that depend on a model, a platform, a regulatory mapping or named approvers are unchanged. [VF]
- Most answers were the default I recommended. They are the operator's decisions, but they were not independently derived. [VF]

| OQ | Subject | Status | Decision | Source | What it means now | If reversed | Residual |
|---|---|---|---|---|---|---|---|
| OQ-01 | Target platform | **DECIDED** | Stay platform-neutral. No cloud or runtime is named. | Round A, answer 2 | ADR-0009 stands: container image and compose file; IaC stays a non-provisioning stub (M-X2 stays NOT MET, accepted). | Naming a platform reopens F1, H3, M1, N1, N3 and N5; expect new ADRs, real IaC, a secrets provider and an observability backend. | B-4 accepted as a gap: no worked reference implementation on a platform. |
| OQ-02 | Model A and Model B | **DECIDED** | No model is used. The deterministic provider stays the only provider. | Round A, answer 3 | R4 'Working AI capabilities' stays BLOCKED, now accepted by the operator. The Stage Q builder comparison (Sonnet vs Haiku, same vendor) stays the only portability evidence. | A hosted or local model reopens J1, J3, L2 and Q: evaluation run, token and latency measurement, second-vendor comparison. | B-1 and B-2 accepted as gaps; real-model quality, latency and cost remain unmeasured. |
| OQ-03 | Network egress | **DECIDED** | No network egress from the application. Build and demo run offline. | Round A, answer 3 | Matches what was built (offline demo, no model call). | Allowing egress is a precondition for any hosted model and for live vulnerability feeds in CI beyond what CI already uses. | None new. |
| OQ-04 | Regulatory obligations | **DECIDED** | No regime is named. The candidate obligations set stays an unvalidated working assumption. | Round B, answer 2 | `docs/25-governance/compliance-obligations.md` stays labelled candidate; RA-01 remains an unsigned risk acceptance. | Naming a regime means a compliance owner validates and maps controls, owners and approval points (K4). | B-3 accepted as a gap; R3 compliance stays BLOCKED. |
| OQ-05 | Stakeholders and approvers | **DECIDED** | The operator (Dinesh) approves everything as Transformation Lead, under provisional authority. No other named party exists. A CTO review stays recommended. | Round A, answer 1 | Gates stay self-signed and PROVISIONAL. This records the arrangement; it does not make the approvals independent. G9 and GOV-10 stay open. | Naming a sponsor or CTO means they review and countersign the gates and the 12 risk acceptances. | B-8: R3 'Risk controls' stays NOT MET (named owners, signed acceptances). |
| OQ-06 | Operator portal in scope | **RATIFIED** | A thin read-only operations view, not an Angular portal. Previously RESOLVED (provisional). | Round D | B-7 resolved by decision. | A real portal is a new build item (apps/web) with a new end-to-end test. | The end-to-end demo stays lighter. |
| OQ-07 | Identity provider | **DEFERRED** | No provider chosen. HS256 stays an interim scheme, not for production; JWKS stays a fail-closed stub. | Round C, answer 1 | Production identity remains an explicit gap (ADR-0004). | Choosing a provider turns the stub into a verifier and adds negative tests. | Interim identity is a known production blocker. |
| OQ-08 | Proxy KPIs acceptable | **RATIFIED** | The labelled proxy KPIs are accepted as the frozen baseline. No real business data exists. | Round B, answer 4 | Stage O comparison is valid only as proxies; the comparability caveat stays in the narrative. | Rejecting the proxies leaves the value argument unsupported. | B-5 accepted as a gap. |
| OQ-09 | Financial data for ROI | **DECIDED** | No financial data. The benefit model stays in analyst-hours with sensitivity ranges and no money figure. | Round B, answer 4 | NPV -970 h expected, +5,525 h optimistic, -2,466 h downside stays the statement; verified benefit is nil. | Real figures would let the model be rerun in currency. | B-6 accepted as a gap. |
| OQ-10 | Evidence retention | **RATIFIED** | Evidence stays in the repository, hash-manifested and version-controlled. | Round D | Retention classes stay as written; there is no external append-only audit sink for runtime records. | An external sink needs a platform (OQ-01). | The runtime audit file is still locally tamper-evident only. |
| OQ-11 | Authorisation to write | **RATIFIED** | The operator ratifies, in their own name, the write authorisation given as instruction D-009. A CTO ratification stays recommended. | Round A, answer 1 | EVD-G-04 stays unsigned as a document; this decision is recorded in EVD-T-01 and D-016. | A CTO refusal would make Stage H onward inadmissible by the Spine's own rule. | Authorisation is one person's, not independent. |
| OQ-12 | Time budget | **DECIDED** | Demo budget is 10 minutes plus 5 minutes of questions. No engagement deadline was stated. | Round A, answer 4 | The demo script stays at 10+5; the engagement deadline is UNKNOWN [UNK]. | A stated deadline changes how the remaining gaps are prioritised. | Deadline unknown. |
| OQ-13 | Discovery folder collision | **RATIFIED** | The spine path `docs/00-preflight/discovery/` is authoritative. | Round D | D-001 stands. | None. | None. |
| OQ-14 | Data remediation location | **RATIFIED** | A derived curated layer; the fixture in `data/synthetic/` stays immutable. | Round D | ETL, quarantine and the original smoke assertions stand. | Editing the fixture in place would break the manifest contract and the before/after comparison. | None. |
| OQ-15 | REC-0001 collision intent | **DECIDED** | Handling decided: treat as a defect (lookup logic fixed, bad-key rows quarantined). The data owner's intent is UNKNOWN. | Round C, answer 2 | Implemented; 0 REC-0001 rows in the curated layer. | If the owner says it was a seeded test, nothing changes in code; the documentation changes. | Intent unconfirmed [UNK]. |
| OQ-16 | Demo environment | **DECIDED** | Local, offline, deterministic provider. | Round A, answer 4 | Matches the rehearsed script. No recorded fallback video exists. | A hosted demo needs OQ-01. | No fallback recording. |
| OQ-17 | Demo format and budget | **DECIDED** | 10 minutes plus 5 of questions, live and offline. This differs from the register default of 20 plus 10, and the difference is now a recorded decision. | Round A, answer 4 | Q-X5 stays PARTIAL: rehearsal was by the author only, no audience or recording. | 20+10 means extending the script and rehearsing to 18 minutes. | Rehearsal gap stays. |
| OQ-18 | Agentic AI in scope | **DECIDED** | Not in scope. J6 stands as not-applicable. | Round C, answer 3 | B-12 closed by decision; the `ai_agent` persona stays a read-only suggester. | An agent runtime is a new stage of work with its own controls. | None. |
| OQ-19 | Secret history disposition | **DECIDED** | Keep history unrewritten; treat the values as compromised; the repository is private. Nothing real exists to revoke: they are workshop placeholders, and none may be reused anywhere. | Round B, answer 1; repository set private by the operator | GOV-07 decided: private. The 10 history findings stay as recorded. | Rewriting history breaks the baseline tags and every hash that cites them; a full re-verification would follow. | Credentials stay in history and in any earlier clone; the exposure is narrowed, not removed. |
| OQ-20 | Real deployment or readiness | **DECIDED** | Readiness decision only. Nothing is deployed. | Round B, answer 3 | The verdict NO-GO production on real data / CONDITIONAL GO controlled pilot on synthetic data stays the deliverable. | A pilot would produce pre-production measurements and a release record. | No production outcomes exist. |
| OQ-21 | Location data constraints | **DECIDED** | No limits stated. The minimisation default stays: location fields masked and excluded from prompts and from logs above INFO. | Round B, answer 2 | RA-10 (retention and rights undefined) stays an unsigned acceptance. | Stated limits would change masking, retention and the privacy impact assessment. | Retention and rights are undefined. |
| OQ-22 | Clean-repo contract retention | **RATIFIED** | The original sanity_check assertions stay unchanged. | Round D | H-X10 stands. | None. | None. |
| OQ-23 | Team size and skills | **DECIDED** | One operator plus the agent; sequential execution. | Round C, answer 4 | Stage ordering stays sequential; no parallel plan is needed. | A team would allow stages K, M and J to run in parallel. | Single-operator risk. |

## Reading the table
- **DECIDED / RATIFIED / DEFERRED** are recorded by the operator on 2026-10-08. [VF]
- Source "Round A to D" refers to the four question rounds in `EVD-T-01-operator-decision-record.json`.
- Invalidation triggers from Document 04 still apply: a stakeholder statement naming a platform (OQ-01), a model or egress policy (OQ-02/03), a regime (OQ-04), or an approver (OQ-05) reopens the relevant question.
