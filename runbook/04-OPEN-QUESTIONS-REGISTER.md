# Brownfield → Production-Grade Transformation Runbook

## Document 04 — Open Questions & Decisions Register

| Field | Value |
|---|---|
| **Document** | 04 — Open Questions & Decisions Register |
| **Version** | v1.0 |
| **Date** | 2026-10-08 |
| **Author / Agent** | AI-FDE Transformation Team — Delta-Team |
| **Status** | Live register — to be maintained throughout execution |
| **Evidence sources** | Delivered repository; Challenge Guide; Delivery Spine; Semantic Layer capture; Evaluation Rubric |

---

## 1. Why this register exists

The Delivery Spine is explicit on this point: *"If evidence is insufficient, record it as
**Unknown** rather than inventing an answer"*, and *"Do not invent owners where none have been
assigned; record them as unresolved governance gaps."*

Each question below arose because the delivered artifacts are silent or self-contradictory on
a matter that changes what an executing engineer builds. Each carries a **recommended default**
so that work is never blocked by an unanswered question — but a default adopted is an
assumption recorded, with an invalidation trigger, not a fact.

**Register discipline.** A question is closed only when an owner records a decision with a
date. A question answered by adopting its default is closed as `DEFAULTED`, and the assumption
is carried into `docs/00-preflight/discovery/assumptions-unknowns.md` and reviewed at every
subsequent stage gate.

---

## 2. Blocking questions — must be answered before the named stage

### OQ-01 — What is the target runtime platform?

| | |
|---|---|
| **Question** | Which cloud or runtime is this system destined for? Azure, AWS, GCP, on-premises, or none (readiness exercise only)? |
| **Why it matters** | IaC, identity, secrets management, observability backend, deployment and release design all follow from this. It is the most load-bearing unanswered question in the engagement. |
| **Evidence of absence** | `infra/terraform/main.tf` declares no provider and no backend — it is a `local_file` resource (F-48). No artifact names a cloud anywhere. |
| **Blocks** | F1 (architecture), H3 (secrets provider), M1 (real IaC), N1 (observability backend), N3 (release), N5 (vendor risk) |
| **Recommended default** | Design platform-neutrally; produce one worked reference implementation on a single platform, clearly labelled illustrative. Invalidation trigger: any stakeholder statement naming a platform. |
| **Owner** | Repository Owner / Architecture — **UNRESOLVED** |
| **Needed by** | Step F1 |

### OQ-02 — Which model replaces `local-sim-v1`, and which second model is used for comparison?

| | |
|---|---|
| **Question** | Which LLM provider and model is the production model, and which distinct second model performs the Stage Q regeneration? |
| **Why it matters** | The Challenge Guide (p.6) mandates *Test Semantic Layer with new model* and *Compare and contrast APPs — Both Models*. Without two models, Stage Q cannot be performed. |
| **Evidence of absence** | `MODEL_VERSION = "local-sim-v1"` is an in-process simulator returning the record's first column value (F-29). No provider, model name, endpoint or credential appears anywhere. |
| **Blocks** | J1, J3, L2, N5, **Q1, Q2 entirely** |
| **Recommended default** | Two locally runnable open-weights models of different families, to avoid both credential and network dependency. State the constraint and its effect on the quality figures. |
| **Owner** | AI Governance Owner — **UNRESOLVED** |
| **Needed by** | Step J1 |

### OQ-03 — Is outbound network access permitted from the build and demo environments?

| | |
|---|---|
| **Question** | May the application call an external model API, package registry or telemetry endpoint? |
| **Why it matters** | Determines whether OQ-02 can be answered with a hosted model, and whether SBOM/scan tooling can fetch vulnerability feeds. |
| **Evidence of absence** | `data/README.md` states *"No external services are required"* — a design property of the delivered system, not a policy statement about the engagement. |
| **Blocks** | J1, M1 (scanner feeds), Q1, Q3 |
| **Recommended default** | Assume no egress. Build for air-gapped operation and treat any available egress as a bonus. |
| **Owner** | Security Owner — **UNRESOLVED** |
| **Needed by** | Step J1 |

### OQ-05 — Who are the actual stakeholders, owners and approvers?

| | |
|---|---|
| **Question** | Are there real named parties for the eight role slots in Document 00 §6, or does the engagement run entirely on provisional governance? |
| **Why it matters** | Every gate requires an approver. Step G4 — the authorisation to modify the repository — cannot be satisfied by an unnamed party. |
| **Evidence of absence** | No individual, team or organisation is named in any delivered artifact. |
| **Blocks** | B2, **G4 (hard block)**, H1 (CODEOWNERS), K4, P1, R1 |
| **Recommended default** | The Transformation Lead holds all roles provisionally; every gate is signed by that role with a `PROVISIONAL AUTHORITY` annotation; the aggregate governance gap is carried into the Stage R residual-risk register as an accepted risk. **Do not fabricate names.** |
| **Owner** | Business Sponsor — **UNRESOLVED** |
| **Needed by** | Step B2; hard-blocks Step G4 |

### OQ-11 — Who authorises the first write to the repository, and when?

| | |
|---|---|
| **Question** | This task's scope is runbook preparation only. Who authorises Stage H execution, under what scope? |
| **Why it matters** | Spine 15 permits modification *only within approved Stage 0B boundaries*. Work performed without that authorisation produces evidence that is inadmissible at the Stage R review. |
| **Evidence of absence** | The task brief explicitly prohibits execution; no artifact describes the authorisation path for a subsequent phase. |
| **Blocks** | **All of Stage H onward** |
| **Recommended default** | Treat Step G4 as a formal checkpoint requiring explicit written instruction before Stage H begins. Stages A–G may proceed under the present brief, as they are read-only. |
| **Owner** | CTO / Repository Owner — **UNRESOLVED** |
| **Needed by** | Step G4 |

---

## 3. Scope and design questions

### OQ-04 — Which regulatory and compliance obligations apply?

**Question.** Does this system fall under data-protection law (driver and vehicle location,
`driver_id`, `current_location`), customs and trade compliance (`customs_agent` persona,
`customs_required` field, `border_risk`), transport safety regulation, or an AI-specific
regime with a risk classification?
**Why it matters.** Rubric criterion 3 scores compliance directly; Spine 25 requires obligations
mapped to controls, owners, evidence and approval points.
**Evidence of absence.** The domain is unmistakably regulated in character, but no artifact
names a jurisdiction, a regime or an obligation.
**Blocks.** K4, and the compliance sub-dimension of R3.
**Recommended default.** Produce a *candidate* obligations set driven by the data categories
actually present, marked throughout as an unvalidated working assumption, together with a
validation plan. Record the gap explicitly in the risk-acceptance register. Do not assert
applicability.
**Owner.** Compliance Owner — **UNRESOLVED.** **Needed by.** Step K4.

### OQ-06 — Is the operator portal in scope?

**Question.** Should a real operator UI be built, or is the portal formally descoped?
**Why it matters.** `README.md` claims an Angular portal with components, services, routes,
forms and Playwright tests. `apps/web/` contains two plain TypeScript classes with no
framework (F-05), and the Playwright test passes against nothing (F-52). Rubric criterion 4
requires an end-to-end workflow.
**Blocks.** E3 (MVP scope), J4, Q3 (demo content).
**Recommended default.** Build a minimal but genuine operator interface covering one complete
business flow end to end — including the human approval gate from Step K1, which is far more
persuasive demonstrated than described. Replace the vacuous Playwright test either way.
**Owner.** Business Sponsor / Product — **UNRESOLVED.** **Needed by.** Step E3.

### OQ-07 — Which identity provider replaces the `X-User-Role` header?

**Question.** Entra ID, Keycloak, Auth0, a local OIDC provider, or mTLS for service identity?
**Why it matters.** F-17 is the most exploitable finding in the repository; its remediation
cannot be designed without knowing the mechanism. Service and AI identities matter as much as
human ones — `ai_agent` is a declared persona.
**Blocks.** H4, K2, M1.
**Recommended default.** A local OIDC provider in the development environment with a
provider-agnostic token-validation layer, so the production provider is a configuration change.
**Owner.** Security Owner / Architecture — **UNRESOLVED.** **Needed by.** Step F1.

### OQ-18 — Is agentic AI in scope?

**Question.** Should an agent runtime be engineered (Spine 22), or is the correct answer a
justified `not-applicable.md`?
**Why it matters.** Spine 22 explicitly permits a justified N/A and warns against inventing
agent artifacts. The repository has an `ai_agent` persona and an `ai_invocations` dataset but
no agent runtime anywhere.
**Blocks.** J6.
**Recommended default.** Decide at Step E1 on minimum-necessary-agency grounds. On present
evidence the likely correct answer is **no agent runtime**, with a written justification —
which is a stronger governance position than building one to fill a template.
**Owner.** AI Governance Owner — **UNRESOLVED.** **Needed by.** Step E1.

### OQ-20 — Does "production-grade" mean a real deployment or a defensible readiness decision?

**Question.** Is there a target environment the system will actually be released into, or is
the deliverable a production-*readiness* decision with evidence?
**Why it matters.** Spine 30 and 34–36 assume a real release producing real production KPIs.
Without one, Stages N3, O1, O2 and O3 must be reframed as planned-and-validated rather than
executed-and-measured.
**Blocks.** N3, O1, R1.
**Recommended default.** Treat it as a readiness decision. Execute the release plan against a
production-like environment, label the Stage O measurements as pre-production, and state the
distinction plainly rather than letting a reviewer infer it.
**Owner.** CTO — **UNRESOLVED.** **Needed by.** Step N3.

---

## 4. Data and semantics questions

### OQ-14 — Where does data remediation happen?

**Question.** `scripts/sanity_check.py` asserts exactly 354 rows per CSV and 3,000 JSONL events
against `data/manifest.json`, exiting non-zero on mismatch (F-54). Quarantining the blank and
duplicate rows found in Step C5 therefore breaks `make smoke`. Is the remedy (a) a derived
`curated` layer leaving `data/synthetic/` immutable, (b) a deliberately versioned
`manifest.json` plus in-place correction, or (c) tolerate the defects and document them?
**Why it matters.** It determines the F2 data strategy, the H6 ETL design and the H9 gate
extension. Choosing wrongly means either a broken smoke gate or a data layer whose contract
nobody can trust.
**Blocks.** F2, H6, H9.
**Recommended default.** **(a)** — a derived, versioned curated layer. It satisfies the
manifest contract and the quality requirement simultaneously, preserves `data/synthetic/` as
the declared test fixture, and keeps the before/after data-quality comparison possible, which
(b) would destroy.
**Owner.** Data Owner — **UNRESOLVED.** **Needed by.** Step F2.

### OQ-15 — Is the `REC-0001` cross-entity collision a seeded defect or a generator artifact?

**Question.** `REC-0001` is the first-row primary key of all six datasets simultaneously
(F-30). `data/quality_issues.json` lists "duplicate business key" as a seeded defect class but
does not describe cross-entity collision. Is this intentional?
**Why it matters.** If it is a seeded defect, the fix is in the data. If it is a generator
artifact, the fix is in the lookup logic (F-31) and the data is left as a fixture. The two lead
to materially different Step H5 implementations — and note that `tests/test_api_contract.py`
and `api-examples/http-requests.http` both use `REC-0001`, so whichever way it is ruled, those
references change.
**Blocks.** H5, D1.
**Recommended default.** Treat it as a genuine finding regardless of intent, and fix the
lookup logic (F-31) *first*, since keyed lookup on the declared business key is correct whether
or not the data changes. Namespace identifiers in the curated layer as a second, separable step.
**Owner.** Data Owner — **UNRESOLVED.** **Needed by.** Step D1.

### OQ-08 — Are proxy KPIs acceptable as the frozen Stage 4 baseline?

**Question.** No business KPI data exists (F-57). Is a baseline built from `events.jsonl`
latency, cost units and severity, plus `ai_invocations` token counts, acceptable as the frozen
baseline for the Stage 34–36 comparison?
**Why it matters.** Spine 4 requires a frozen baseline and Spine 35 forbids changing
definitions later. If the proxies are rejected after Stage O, the entire value argument
collapses with no time to rebuild it.
**Blocks.** C1, O1, O2, O3.
**Recommended default.** Yes, with every proxy explicitly labelled, its limitations stated in
`proxy-metrics.md`, and the comparability caveat repeated in the Stage O variance analysis and
in the executive narrative. **Have this ratified at Step C1, not discovered at Step O2.**
**Owner.** Business Sponsor / Data Owner — **UNRESOLVED.** **Needed by.** Step C1.

### OQ-21 — Are there data residency or location-privacy constraints?

**Question.** `vehicles.current_location`, `driver_id`, `routes.origin`/`destination` and
`tracking_events.location` constitute personal location data about identifiable drivers.
`security/threat-model.md` names `location_data_overexposure` as a concern. Are there residency,
minimisation or retention constraints?
**Why it matters.** Drives the D4 access semantics, the K3 privacy impact assessment and the
N1 privacy-safe logging design. Also interacts with F-13 (`LOG_LEVEL=DEBUG` by default).
**Blocks.** D4, K3, N1.
**Recommended default.** Apply minimisation by default: location fields are excluded from
prompts and from logs above `INFO`, and are field-masked for personas without an explicit
operational purpose. Over-protecting is recoverable; under-protecting is not.
**Owner.** Compliance Owner / Data Owner — **UNRESOLVED.** **Needed by.** Step D4.

---

## 5. Process, governance and logistics questions

### OQ-09 — Is any financial data available for the ROI model?

**Question.** Cost per shipment, exception handling cost, headcount, hourly rates,
infrastructure spend, model pricing — any of it?
**Why it matters.** Spine 36 requires ROI, NPV and payback. With no inputs, every figure is
invented, which is precisely what the spine prohibits.
**Recommended default.** Build a parameterised model with assumption inputs clearly exposed, a
sensitivity analysis across optimistic/expected/downside, and a double-counting check. Present
ranges, never a single number presented as a measurement.
**Owner.** Business Sponsor — **UNRESOLVED.** **Needed by.** Step O3.

### OQ-10 — What is the evidence retention policy and where does evidence live?

**Question.** How long is evidence retained, where, under whose control, and is in-repository
storage acceptable for an audit trail?
**Why it matters.** Spine 25 requires an evidence retention policy. F-44 shows the current
audit sink is a tamperable local file — the evidence tree must not repeat that mistake at a
larger scale.
**Recommended default.** Evidence in-repository under `evidence/`, hash-manifested and
version-controlled; runtime audit records in an external append-only store the application
cannot rewrite; retention stated per evidence class in `evidence-retention-policy.md`.
**Owner.** Compliance Owner — **UNRESOLVED.** **Needed by.** Step A2.

### OQ-12 — What is the time budget and submission deadline?

**Question.** How long does the team have, and is there a fixed submission date?
**Why it matters.** It determines MVP scope at Step E3 and the increment plan at Step I2. It
also governs the trade-off identified in Document 03 §4: thirty-one of fifty-seven findings sit
in R3 (20 marks) while only seven sit in R4 (25 marks), so an unbounded remediation effort
scores worse than a bounded one.
**Recommended default.** Time-box Stages A–G to roughly one third of the budget, Stages H–L to
one third, and Stages M–R to one third. Protect Step J4 (working end-to-end workflow) and
Step R4 (requirement disposition) explicitly — they carry disproportionate marks.
**Owner.** Transformation Lead — **UNRESOLVED.** **Needed by.** Step E3.

### OQ-13 — Does `docs/discovery/` or `docs/00-preflight/discovery/` win?

**Question.** The delivered repository reserves `docs/discovery/` for discovery notes; the
Delivery Spine mandates `docs/00-preflight/discovery/`.
**Why it matters.** Two discovery locations means a reviewer finds half the evidence.
**Recommended default.** The spine path is authoritative;
`docs/discovery/README.md` is retained as a pointer, since `scripts/sanity_check.py` does not
require it but removing delivered files without cause is poor practice.
**Owner.** Transformation Lead — **UNRESOLVED.** **Needed by.** Step A2.

### OQ-16 — What demonstration environment is available?

**Question.** Is there a hosted environment for the demo, is it local, and must it run without
network access?
**Blocks.** Q3. **Recommended default.** Fully local via the Step H2 container definition, with
a recorded fallback video in case live execution fails. **Owner.** SRE / Operations —
**UNRESOLVED.** **Needed by.** Step Q3.

### OQ-17 — What is the demonstration format, audience and time budget?

**Question.** How long, to whom, and is it live or recorded?
**Why it matters.** Rubric criterion 5 scores demo quality and the ability to answer evaluator
questions. A six-beat script (Document 02, Step Q3) needs a known time budget to be rehearsed.
**Blocks.** Q3. **Recommended default.** Assume 20 minutes of demonstration plus 10 of
questions; rehearse to 18. **Owner.** Transformation Lead — **UNRESOLVED.** **Needed by.** Step Q3.

### OQ-19 — How is the secret history exposure handled?

**Question.** Step A1 commits the as-delivered tree, which contains `Welcome123`,
`sk-workshop-hardcoded-example` and a shared vendor token (F-09, F-10, F-12). Removing them at
Step H3 does not remove them from the `baseline/v0-as-delivered` commit. Is history rewritten,
or is the baseline preserved with the values treated as compromised and rotated?
**Why it matters.** It is a genuine trade-off between evidential integrity (the baseline tag is
the anchor of every before/after claim) and secret hygiene. A reviewer will notice either choice.
**Recommended default.** **Preserve history, rotate everything.** These are synthetic workshop
credentials, so the actual exposure is nil, while the baseline tag is load-bearing for the
entire evidence argument. Record the decision, the rotation plan and the reasoning explicitly in
`secrets-hardening.md` — the point is that the trade-off was seen and decided, not hidden.
**Owner.** Security Owner — **UNRESOLVED.** **Needed by.** Step H3.

### OQ-22 — Must the `sanity_check.py` clean-repo contract keep passing?

**Question.** `scripts/sanity_check.py` fails if any of `docs/PARTICIPANT_BRIEF.md`,
`docs/discovery/prompt-pack.md`, `docs/challenges/moonshot-tasks.md` or
`docs/workshop-scorecard.md` exists. Must this remain enforced after transformation?
**Why it matters.** It is a workshop-integrity contract rather than an engineering one, but
Step H9 extends this script and must not silently drop its existing assertions (F-55).
**Recommended default.** Preserve all existing assertions unchanged and add new ones alongside.
Document the forbidden-file check as an inherited workshop contract so a future maintainer
understands why it exists.
**Owner.** Transformation Lead — **UNRESOLVED.** **Needed by.** Step H9.

### OQ-23 — What team size and skill mix is available?

**Question.** How many engineers, with what skills — Python, frontend, security, SRE, data?
**Why it matters.** The runbook spans 102 steps across 18 stages. Stage parallelisation
(Stages K and M can run partly in parallel with J; Stage D can start during C) depends entirely
on headcount. A sequential single-engineer execution needs a materially different increment plan.
**Blocks.** I2. **Recommended default.** Plan for sequential execution by a small team; mark
parallelisable stages in the increment plan so capacity can be exploited if it exists.
**Owner.** Transformation Lead — **UNRESOLVED.** **Needed by.** Step I2.

---

## 6. Summary table

| OQ | Subject | Blocks | Severity | Owner role | Needed by |
|---|---|---|---|---|---|
| OQ-01 | Target platform | F1, H3, M1, N1, N3, N5 | **Blocking** | Architecture | F1 |
| OQ-02 | Model A and Model B | J1, J3, L2, N5, Q1, Q2 | **Blocking** | AI Governance | J1 |
| OQ-03 | Network egress permitted | J1, M1, Q1 | **Blocking** | Security | J1 |
| OQ-04 | Regulatory obligations | K4 | High | Compliance | K4 |
| OQ-05 | Stakeholders and approvers | B2, G4, H1, K4, P1, R1 | **Blocking** | Business Sponsor | B2 / G4 |
| OQ-06 | Operator portal in scope | E3, J4, Q3 | High | Product | E3 |
| OQ-07 | Identity provider | H4, K2, M1 | High | Security | F1 |
| OQ-08 | Proxy KPIs acceptable | C1, O1–O3 | High | Business Sponsor | C1 |
| OQ-09 | Financial data for ROI | O3 | Medium | Business Sponsor | O3 |
| OQ-10 | Evidence retention | A2, K4 | Medium | Compliance | A2 |
| OQ-11 | Authorisation to write | **All of Stage H+** | **Blocking** | CTO | G4 |
| OQ-12 | Time budget | E3, I2 | High | Transformation Lead | E3 |
| OQ-13 | Discovery folder collision | A2 | Low | Transformation Lead | A2 |
| OQ-14 | Data remediation location | F2, H6, H9 | High | Data Owner | F2 |
| OQ-15 | `REC-0001` collision intent | D1, H5 | High | Data Owner | D1 |
| OQ-16 | Demo environment | Q3 | Medium | SRE | Q3 |
| OQ-17 | Demo format and budget | Q3 | Medium | Transformation Lead | Q3 |
| OQ-18 | Agentic AI in scope | J6 | Medium | AI Governance | E1 |
| OQ-19 | Secret history disposition | H3, P5 | High | Security | H3 |
| OQ-20 | Real deployment or readiness | N3, O1, R1 | High | CTO | N3 |
| OQ-21 | Location data constraints | D4, K3, N1 | High | Compliance | D4 |
| OQ-22 | Clean-repo contract retention | H9 | Low | Transformation Lead | H9 |
| OQ-23 | Team size and skills | I2 | Medium | Transformation Lead | I2 |

---

## 7. The five decisions needed first

If only a short window of CTO and sponsor attention is available, these five unlock the most
work and have no workable default that fully substitutes for an answer:

1. **OQ-11 — authorisation to modify the repository.** Everything from Stage H onward is
   blocked without it. Stages A–G can proceed under the present brief regardless, so this can
   be answered in parallel with early execution.
2. **OQ-05 — named approvers.** Every gate signature depends on it, and the Delivery Spine
   forbids inventing owners. Even confirming "there are none, proceed provisionally" is an
   answer that unblocks Step G4.
3. **OQ-02 — the two models.** Stage Q is a mandated Challenge Guide deliverable that cannot
   be simulated or substituted. If only one model is available, that must be known early
   enough to declare Stage Q not-performed rather than discovering it at the end.
4. **OQ-01 — target platform.** Four stages of infrastructure, identity, secrets and release
   work are platform-shaped; a late answer invalidates completed design work.
5. **OQ-12 — time budget.** Document 03 §4 shows the findings are concentrated in R3 (20 marks)
   while the marks are concentrated in R4 (25 marks). Without a time budget, the natural
   gravity of 57 findings pulls effort away from the working application, and that trade-off
   should be made deliberately rather than by drift.
