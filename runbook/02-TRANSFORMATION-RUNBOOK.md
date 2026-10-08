# Brownfield → Production-Grade Transformation Runbook

## Document 02 — The Runbook

| Field | Value |
|---|---|
| **Document** | 02 — The Runbook (18 stages, 102 steps) |
| **Version** | v1.0 |
| **Date** | 2026-10-08 |
| **Author / Agent** | AI-FDE Transformation Team — Delta-Team |
| **Status** | Draft for CTO review |
| **Prerequisite reading** | Document 00 (evidence contract, directory spine, roles); Document 01 (findings register) |
| **Evidence sources** | Delivered repository; Challenge Guide; End-to-End Production Delivery Spine; Prompt Template; Semantic Layer capture; Evaluation Rubric |

---

## How to read a step

Every step is written in the same shape:

- **Action** — what the engineer does.
- **Inputs** — what must be in hand before starting.
- **Depends on** — the earlier step(s) that produce those inputs, **and why** that
  dependency exists. A dependency with no stated reason is not a dependency.
- **Outputs** — the artifact(s) the step produces, at their mandated paths.
- **Evidence** — the proof of completion, and where it is stored.
- **Addresses** — finding IDs from Document 01 and/or Challenge Guide challenges.
- **Rubric** — the rubric criteria the step's evidence contributes to.

Close every step with the **Required Final Response**: status (PASS / CONDITIONAL PASS /
BLOCKED), key findings, major risks, assumptions and unknowns, artifacts created, blocking
issues, recommended next action.

**Read-only discipline:** Stages A–G are read-only with two named exceptions (Steps A1–A2
create version control and the evidence tree; Step C8 adds characterization tests additively).
No application behaviour changes before Stage H, and Stage H does not begin until Step G4
records written authorisation.

---

# STAGE A — Engagement Mobilisation & Read-Only Orientation

**Spine stages:** 0A (Pre-Flight Orientation), 0B (Provisional Operating Contract),
0C (Provisional AI Economics Envelope)
**Mode:** Read-only, except Steps A1–A2 which establish the evidence infrastructure itself.
**Purpose:** Make the engagement recordable before making it better.

---

### Step A1 — Establish version control and freeze the pre-transformation baseline

**Action.** Initialise a Git repository at the root of
`07-logistics-shipment-fleet-routing-ops/`. Author a `.gitignore` that excludes at minimum
`logs/`, `generated-env.txt`, `.env`, `.venv/`, `__pycache__/`, `.pytest_cache/`,
`node_modules/`. Commit the delivered tree **exactly as received**, with no edits, as the
first commit. Tag it `baseline/v0.1-as-delivered-bytes` and record the commit SHA. Compute a SHA-256 manifest of every delivered file. Execution note (2026-10-08): a first tag, `baseline/v0-as-delivered`, was found to differ from the received bytes in 6 CSV files because of Windows CRLF conversion; `.gitattributes` was added and `baseline/v0.1-as-delivered-bytes` is the byte-exact reference used by every check below (decision-log D-003).

**Inputs.** The delivered repository tree.

**Depends on.** Nothing — this is the first action of the engagement.

**Why this must be first.** The Delivery Spine requires that every artifact "be
version-controlled", "not overwrite prior evidence silently" and "preserve earlier baselines
so before/after comparison remains possible". Finding **F-01** establishes that none of these
is currently possible. Until an immutable as-delivered commit exists, no later claim of the
form *"this changed and that did not"* — which is the substance of rubric criterion 1 and of
the entire Stage O value argument — can be verified. The `.gitignore` is authored in the same
step because **F-14** and **F-44** mean that without it, a real `.env` and the in-process
audit log become committable on the very first developer action.

**Outputs.** Initialised repository; `.gitignore`; tag `baseline/v0.1-as-delivered-bytes`;
`evidence/00-preflight/EVD-A-01-baseline-file-manifest.sha256`.

**Evidence.** Commit SHA and tag; the SHA-256 manifest; terminal transcript of the init and
tag commands. → `evidence/00-preflight/`

**Addresses.** F-01, F-14, F-44. **Rubric.** 1, 3.

---

### Step A2 — Create the evidence spine

**Action.** Create the full `docs/` tree exactly as specified in the Delivery Spine
(`00-preflight/{discovery,operating-contract,ai-economics}`, `01-engagement` … `42-executive`,
`final-prd`), the mirrored `evidence/` tree, and `semantic-layer/`. Place a `MANIFEST.md`
stub in each `evidence/` subdirectory. Author `docs/EVIDENCE-CONTRACT.md` carrying the
mandatory artifact header block and the Verified Fact / Inference / Assumption / Unknown
classification from Document 00 §3. Resolve **OQ-13** (the `docs/discovery/` versus
`docs/00-preflight/discovery/` collision) and record the ruling.

**Inputs.** Delivery Spine directory specification; Document 00 §3–§4; delivered
`docs/discovery/README.md`.

**Depends on.** **A1** — the tree must be created inside a version-controlled repository,
otherwise the artifacts it will hold inherit the same unprovability the baseline assessment
identified in F-01.

**Why.** Every subsequent step writes to a path defined here. Creating paths on demand leads
to drift from the mandated spine, and the spine is the index a reviewer navigates. The
evidence contract is authored now because artifacts written before it exists will not carry
the mandatory header and will have to be reworked.

**Outputs.** Complete `docs/` and `evidence/` trees; `docs/EVIDENCE-CONTRACT.md`;
`MANIFEST.md` stubs; OQ-13 ruling recorded in `docs/00-preflight/operating-contract/`.

**Evidence.** Directory listing of both trees; commit SHA. → `evidence/00-preflight/EVD-A-02-spine-tree.txt`

**Addresses.** Spine Global Execution Contract. **Rubric.** 1, 3, 5.

---

### Step A3 — Capture an immutable environment and toolchain snapshot

**Action.** Record OS and kernel, Python version, `pip freeze`, Node and npm versions,
Git version, and the presence or absence of `terraform`, `opa`, `docker`, `syft`/`trivy`.
Record which of these are **missing**, because the absence is itself the Stage 5 (IaC)
finding. Do not install anything in this step.

**Inputs.** The execution host.

**Depends on.** **A2** — the snapshot is an evidence artifact and needs its storage path.

**Why.** **F-07** establishes there is no container or environment definition, so the
behaviour observed in Stage C is a function of an undocumented local environment. Without a
recorded snapshot, the Stage C baseline is not reproducible and the Stage H behaviour-
difference analysis (Step H10) cannot distinguish a genuine behaviour change from an
environment change.

**Outputs.** `docs/00-preflight/discovery/environment-snapshot.md`.

**Evidence.** Raw command outputs. → `evidence/00-preflight/EVD-A-03-toolchain-snapshot.txt`

**Addresses.** F-07, F-48. **Rubric.** 1, 2.

---

### Step A4 — Produce the read-only pre-flight discovery pack (Spine 0A)

**Action.** Inspect repository structure, technologies, applications, services, APIs, data
stores, integrations, ETL, tests, security mechanisms, observability, runtime/deployment
clues and business workflows. Produce the twelve mandated artifacts. Classify every statement
as Verified Fact, Inference, Assumption or Unknown and cite file paths. **Do not perform deep
refactoring analysis** — that is Stage C (Spine 7). **Do not make transformation
recommendations** — Spine 0A forbids it.

**Inputs.** The repository; A3 environment snapshot; Document 01 as a cross-check (the
executing engineer should reproduce the findings independently, not copy them).

**Depends on.** **A2** (artifact paths), **A3** (technology inventory needs the toolchain
snapshot to distinguish "the repository requires X" from "X is installed here").

**Why.** Spine 0A is explicitly the orientation that qualification (Stage B) depends on:
an engagement cannot be qualified against a system nobody has characterised. The read-only
constraint exists so that the behavioural baseline captured in Stage C describes the system
as delivered, not as partially repaired.

**Outputs** (all in `docs/00-preflight/discovery/`): `repository-overview.md`,
`system-landscape.md`, `technology-inventory.md`, `high-level-architecture.md`,
`integration-overview.md`, `data-flow-overview.md`, `workflow-overview.md`,
`test-overview.md`, `security-observability-overview.md`, `assumptions-unknowns.md`,
`initial-risk-register.md`, `discovery-summary.md`.

**Evidence.** The twelve artifacts, each with the mandatory header; the file-path citations
they contain; `evidence/00-preflight/EVD-A-04-repo-tree-annotated.txt`.

**Addresses.** Challenge 1; F-05, F-53 (both are documentation-versus-reality drift that
discovery must surface). **Rubric.** 1.

---

### Step A5 — Produce the provisional operating contract (Spine 0B)

**Action.** Define current scope, exclusions, repositories, environments, data boundaries,
permitted and prohibited actions, repository write restrictions, production-access
restrictions, security and privacy constraints, provisional tool and agent permissions,
evidence requirements, change control, human-approval triggers, stop conditions and
escalation. Mark every unresolved ownership or decision right **`PROVISIONAL`**.
**Do not invent owners.**

**Inputs.** A4 discovery pack; Document 00 §6 (role slots, all UNRESOLVED); Document 04.

**Depends on.** **A4** — boundaries can only be drawn around a system whose components,
data stores and integrations have been enumerated. Drawing them first produces a contract
that does not match the estate.

**Why.** This contract is what authorises — and limits — every write action from Stage H
onward. **F-01** and **F-08** establish that the repository has no change-control surface at
all, so the contract is the only governance that will exist until Step H1 creates CODEOWNERS
and branch protection.

**Outputs** (all in `docs/00-preflight/operating-contract/`):
`provisional-operating-contract.md`, `scope-boundaries.md`, `repository-write-boundaries.md`,
`environment-access-boundaries.md`, `data-use-constraints.md`,
`provisional-tool-agent-permissions.md`, `provisional-human-approval-rules.md`,
`evidence-contract.md`, `change-control-rules.md`, `stop-conditions.md`,
`open-governance-decisions.md`, `operating-contract-readiness.md`.

**Evidence.** The twelve artifacts; the explicit list of items flagged for confirmation at
Spine Stages 2, 23, 25 and 37. → `evidence/00-preflight/`

**Addresses.** F-08; Document 04 OQ-05, OQ-11. **Rubric.** 3.

---

### Step A6 — Produce the provisional AI economics envelope (Spine 0C)

**Action.** Build scenarios for deterministic software, conventional automation, GenAI and
agentic AI. Estimate workload volume, context size, model calls, token flows, loop overhead,
retries and latency **only where evidence exists**, and separate measured data from
assumptions. Use the measured figures available: 354 AI invocations carrying 904,432 declared
tokens; 3,000 events carrying 6,735.29 cost units with p50 latency 1,667 ms and p95 13,709 ms.
Declare the maximum acceptable cost per request, cost per case, latency ceiling, context size
and agent-loop limit as provisional design constraints. **Do not assume AI is justified** —
that decision is Stage E.

**Inputs.** `data/synthetic/ai_invocations.csv`; `data/synthetic/events.jsonl`;
A4 discovery pack.

**Depends on.** **A4** — the AI touchpoints must be located before their economics can be
scoped; **A3** — latency figures are environment-dependent.

**Why.** **F-28** establishes that the existing token figure is fabricated
(`len(prompt.split()) * 2`), so the only defensible economic baseline is the dataset's own
declared values, clearly labelled as synthetic. Setting cost ceilings now, before any model
is chosen, prevents the common failure where the model is selected first and the economics
are reverse-justified. Stage E Step E2 reconciles against this envelope.

**Outputs** (all in `docs/00-preflight/ai-economics/`): `workload-assumptions.md`,
`solution-scenarios.md`, `provisional-model-call-inventory.md`, `token-flow-scenarios.md`,
`provisional-token-budget.md`, `provisional-context-budget.md`, `provisional-loop-budget.md`,
`volume-assumptions.md`, `cost-scenarios.md`, `quality-latency-cost-envelope.md`,
`preliminary-finops-baseline.md`, `preliminary-tco.md`, `economics-readiness.md`.

**Evidence.** Profiling output supporting every quoted figure.
→ `evidence/00-preflight/EVD-A-06-ai-economics-profile.json`

**Addresses.** F-28, F-57; Challenge 12. **Rubric.** 2.

---

### Step A7 — Stage A gate review

**Action.** Verify Stage A exit criteria. Record the stage status and the Required Final
Response. Raise any new unknowns into Document 04.

**Inputs.** All Stage A outputs.
**Depends on.** A1–A6.
**Why.** Spine stages 1–3 consume the 0A/0B/0C pack; proceeding with an incomplete
orientation produces qualification decisions built on unexamined assumptions.
**Outputs.** `docs/00-preflight/stage-a-gate.md`.
**Evidence.** Completed exit-criteria table, signed by the Transformation Lead.

### Stage A exit criteria

| # | Criterion | Verification method |
|---|---|---|
| A-X1 | Repository is version-controlled and `baseline/v0.1-as-delivered-bytes` resolves to a commit | `git show baseline/v0.1-as-delivered-bytes` |
| A-X2 | The as-delivered commit is byte-identical to what was received | SHA-256 manifest comparison |
| A-X3 | All 44 top-level spine directories (plus 5 nested) and the `evidence/` mirror exist | Directory listing diff against the spine specification |
| A-X4 | All 37 Stage-A artifacts exist and each carries the complete mandatory header | Automated header-presence check across `docs/00-preflight/**` |
| A-X5 | Every statement is classified Verified Fact / Inference / Assumption / Unknown | Reviewer sample of ≥10 statements per artifact |
| A-X6 | No transformation recommendation appears in any 0A artifact | Reviewer read-through (Spine 0A prohibits it) |
| A-X7 | Every unresolved owner is marked `PROVISIONAL` and appears in `open-governance-decisions.md`; none are invented | Cross-check against Document 00 §6 |
| A-X8 | No application file has been modified since the baseline tag | `git diff baseline/v0.1-as-delivered-bytes -- apps etl legacy data scripts` returns empty |

---

# STAGE B — Qualification, Stakeholders & Problem Framing

**Spine stages:** 1, 2, 3. **Mode:** Read-only.

---

### Step B1 — Qualify the engagement and issue a go / conditional-go / no-go

**Action.** Using Stage A evidence, identify client context, business problem, sponsor,
business owner, technical owner, urgency, expected outcomes, dependencies, delivery
constraints and the reasons the initiative could be premature or non-viable. Separate
stakeholder claims from validated evidence. Classify the engagement **Go**, **Conditional
Go** or **No-Go**.

**Inputs.** A4 discovery pack; A5 operating contract; Document 04.
**Depends on.** **A4, A5** — qualification without an orientation is opinion, and the
decision depends on the write boundaries and stop conditions A5 defines.
**Why.** Spine 1 is the first point at which the engagement can be declined. Given 23 S1
findings and the unresolved platform, model and regulatory questions (OQ-01, OQ-02, OQ-04),
the realistic outcome is **Conditional Go**, with the conditions named and dated.
**Outputs** (`docs/01-engagement/`): `engagement-canvas.md`, `team-charter.md`,
`qualification-checklist.md`, `use-case-hypothesis.md`, `engagement-risks.md`,
`open-qualification-questions.md`, `engagement-go-no-go.md`.
**Evidence.** The decision artifact with its evidence citations. → `evidence/01-engagement/`
**Addresses.** Document 04 OQ-01, OQ-02, OQ-04, OQ-12. **Rubric.** 1.

---

### Step B2 — Map stakeholders, decision rights and approval authority

**Action.** Identify stakeholders across business, users, product, architecture, engineering,
data, security, privacy, compliance, risk, operations and leadership. Capture needs,
incentives, concerns, responsibilities, conflicts, approval authority and decision rights.
Reconcile with the A5 provisional contract. **Where no owner has been assigned, record an
unresolved governance gap — do not invent one.**

**Inputs.** A5 operating contract; Document 00 §6 role slots; B1 qualification.
**Depends on.** **A5** — this step confirms or overturns the provisional positions A5
recorded, so it needs them stated first; **B1** — the sponsor and owners identified in
qualification seed the map.
**Why.** Every later approval gate — the Stage G authorisation to write, the Stage K autonomy
matrix, the Stage R go/no-go — requires a named approver. **OQ-05** records that the delivered
artifacts name none. This step either resolves that or formally accepts that the engagement
runs with provisional governance, which must then appear in the Stage R residual-risk register.
**Outputs** (`docs/02-stakeholders/`): `stakeholder-map.md`, `stakeholder-needs-matrix.md`,
`decision-rights-map.md`, `approval-authority-map.md`, `stakeholder-conflicts.md`,
`escalation-map.md`, `operating-contract-confirmations.md`.
**Evidence.** Approval-authority map; the list of still-unresolved governance gaps.
**Addresses.** F-08; OQ-05. **Rubric.** 3.

---

### Step B3 — Frame the problem and define NFRs and success criteria

**Action.** Translate the evidence into a precise, **technology-neutral** business problem.
Separate symptom, root problem, proposed solution and assumed AI need. Define personas (the
eight in `docs/domain-specific-spec.md`), jobs-to-be-done, user journeys, scope, exclusions,
business requirements, NFRs and measurable success and failure criteria.

**Inputs.** `docs/domain-specific-spec.md`; A4 workflow overview; B1; B2.
**Depends on.** **B1** (the problem must be the one that was qualified), **B2** (success
criteria without an owner cannot be accepted).
**Why.** Spine 3 completion explicitly requires a technology-neutral problem definition. This
matters here because the repository already contains an *assumed* AI solution
(`ai_gateway.py`) whose declared capabilities are unimplemented (**F-29**). Framing the
problem independently of that assumption is what makes the Stage E AI-vs-no-AI decision
honest rather than ceremonial.
**Outputs** (`docs/03-problem-value/`): `problem-framing-canvas.md`, `problem-statement.md`,
`personas.md`, `jobs-to-be-done.md`, `user-journeys.md`, `scope-exclusions.md`,
`business-requirements.md`, `nfrs.md`, `success-criteria.md`, `value-hypothesis.md`,
`assumptions-register.md`.
**Evidence.** NFR set with measurable thresholds; success criteria with owners.
**Addresses.** F-29; Challenge 1. **Rubric.** 1, 4.

---

### Step B4 — Stage B gate review

**Outputs.** `docs/03-problem-value/stage-b-gate.md`.

### Stage B exit criteria

| # | Criterion | Verification method |
|---|---|---|
| B-X1 | A Go / Conditional Go / No-Go decision exists with cited evidence | Read `engagement-go-no-go.md`; every condition has an owner and a date |
| B-X2 | No stakeholder, owner or approval authority has been invented | Cross-check every named party against a source document or an `UNRESOLVED` marker |
| B-X3 | The problem statement names no technology and no AI | Keyword scan of `problem-statement.md` |
| B-X4 | Every NFR is measurable (has a metric, a threshold and a measurement method) | Reviewer check of each NFR row |
| B-X5 | Success criteria are traceable to a business requirement | `success-criteria.md` cross-reference column is complete |
| B-X6 | Repository application code still matches `baseline/v0.1-as-delivered-bytes` | `git diff` empty for `apps`, `etl`, `legacy`, `data`, `scripts` |

---

# STAGE C — Baseline: KPIs, Current State, Root Cause, Behaviour

**Spine stages:** 4, 5, 6, 7. **Mode:** Read-only, except Step C8 (additive tests only).
**Purpose:** Capture what the system does today, precisely enough that any later change can
be proven to be intentional.

---

### Step C1 — Define and freeze the KPI baseline

**Action.** Define each KPI's name, meaning, formula, unit, owner, source, measurement
period, segmentation and current value. **Declare explicitly that no business KPI data exists
in the repository (F-57)** and that the following are *proxies*, with their limitations
stated: event latency p50/p95 and max from `events.jsonl`; cost units per event and per
business entity; severity distribution (`error` + `critical` = 1,188 of 3,000 events);
correlation-ID completeness (33.6%); declared AI token volume (904,432 across 354
invocations); carrier retry distribution (51–4,995). **Freeze these definitions.**

**Inputs.** `data/synthetic/events.jsonl`; `ai_invocations.csv`; `carrier_bookings.csv`;
B3 success criteria.
**Depends on.** **B3** — a KPI that is not tied to a success criterion measures effort rather
than value.
**Why.** Spine 34 and 35 compare after-state against this baseline *using the frozen
definitions*, and the spine forbids changing KPI definitions to improve results. Freezing
them before any change is the only way the Stage O variance claim is defensible. Declaring
proxy status now is what prevents a reviewer in Stage R from discovering that a "business
outcome" was always a latency histogram.
**Outputs** (`docs/04-baseline-kpis/`): `kpi-dictionary.md`, `baseline-kpi-sheet.md`,
`measurement-methodology.md`, `data-source-map.md`, `baseline-data-quality.md`,
`proxy-metrics.md`, `baseline-evidence.md`, `kpi-baseline-signoff.md`.
**Evidence.** The computed baseline values with the exact script that produced them.
→ `evidence/04-baseline-kpis/EVD-C-01-kpi-baseline.json` + the profiling script
**Addresses.** F-57; Challenge 12. **Rubric.** 1, 4.

---

### Step C2 — Reproduce the documented quick-start and record it failing

**Action.** On a clean virtual environment, execute the `README.md` Quick Start verbatim:
`python -m venv .venv`, activate, `pip install -r requirements.txt`, `pytest -q`,
`python etl/run_daily_batch.py --sample`, `uvicorn apps/api.main:app --reload`.
**Capture the full transcript including the failures.** Expected: `pytest -q` fails at
collection with `ModuleNotFoundError`/`RuntimeError` on `httpx` (**F-02**), and the
`uvicorn` invocation fails because the module path uses a slash (**F-03**).

**Inputs.** `README.md`; `requirements.txt`; A3 environment snapshot.
**Depends on.** **A3** — the transcript is only meaningful alongside the recorded toolchain;
**A1** — the transcript must describe the as-delivered tag, not a partially repaired tree.
**Why.** This is the single highest-value piece of Stage C evidence. The Challenge Guide's
Stage 2 acceptance standard is that the team can *distinguish intended legacy behaviour from
defects that must be fixed*. A recorded failure of the project's own documented entry point
proves the distinction empirically rather than asserting it, and it is the before-half of the
Step H10 behaviour-difference comparison. **Do not fix anything in this step** — the failure
is the evidence.

**Outputs.** `docs/07-repo-assessment/baseline-behaviour.md` (quick-start section).
**Evidence.** Full terminal transcript with exit codes.
→ `evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt`
**Addresses.** F-02, F-03, F-07. **Rubric.** 1.

---

### Step C3 — Execute the existing test suite and smoke gate; capture raw results

**Action.** Install the minimum additional dependency required to make the suite *execute*
(`httpx`) **into the virtual environment only — do not amend `requirements.txt`**, which is
a Stage H change. Run `pytest -q --junitxml=... --cov`, then `make smoke`
(`scripts/sanity_check.py`), then `make etl`. Record pass/fail, counts, coverage and exit
codes for each.

**Inputs.** C2 environment; `tests/`; `Makefile`; `scripts/sanity_check.py`.
**Depends on.** **C2** — the suite cannot run until the C2 failure is understood and
deliberately worked around; separating "worked around in the venv" from "fixed in the repo"
is what keeps Stage C read-only.
**Why.** This is the behavioural baseline every later regression claim compares against.
Capturing coverage now quantifies **F-51** and **F-52**: three assertions, one of which
asserts a defect, and one of which runs against an application that does not exist.
**Outputs.** `docs/07-repo-assessment/baseline-test-results.md`.
**Evidence.** JUnit XML, coverage XML, `make smoke` and `make etl` transcripts.
→ `evidence/07-repo-assessment/EVD-C-03-*`
**Addresses.** F-02, F-51, F-52, F-54. **Rubric.** 1.

---

### Step C4 — Map the current process and system landscape

**Action.** Map the end-to-end business process and system landscape: actors, steps,
decisions, queues, handoffs, systems, APIs, events, data stores, ETL, batch jobs, manual
workarounds, integrations, controls and operational dependencies. Reconstruct the four
declared business flows (booking→pickup; hub scan→route assignment; carrier booking saga;
exception investigation→delivery evidence) against the code and data that actually implement
them, and record where a declared flow has **no implementation**.

**Inputs.** `docs/domain-specific-spec.md`; A4 discovery pack; the repository.
**Depends on.** **A4** — the component inventory is the input to the landscape map.
**Why.** Challenge 1 requires business-flow reconstruction from evidence. The reconstruction
is where the declared-versus-implemented gaps become undeniable: three AI capabilities with
no implementation (**F-29**), an Angular portal that is two TypeScript classes (**F-05**),
and a carrier booking saga whose compensation path exists only as a CSV column (**F-38**).
**Outputs** (`docs/05-current-state/`): `current-process-map.md`, `business-workflow-map.md`,
`system-landscape.md`, `integration-landscape.md`, `brownfield-inventory.md`,
`manual-handoffs.md`, `process-bottlenecks.md`, `control-points.md`,
`dependency-hotspots.md`, `current-state-summary.md`.
**Evidence.** Flow-to-code trace table mapping each declared flow to implementing files or
to `NOT IMPLEMENTED`. → `evidence/05-current-state/`
**Addresses.** F-05, F-29, F-38, F-53; Challenge 1. **Rubric.** 1.

---

### Step C5 — Produce the data quality baseline

**Action.** Profile all seven datasets read-only, writing all output outside `data/`.
Measure per dataset: row count, duplicate primary keys (with the duplicated values), rows
with blank mandatory fields, out-of-domain timestamps, out-of-range numerics, categorical
value distributions, and referential integrity against `shipments.csv`. For `events.jsonl`
measure correlation-ID completeness, severity distribution, latency percentiles and cost
totals. Compare results against `data/manifest.json` and `data/quality_issues.json`.

**Expected results** (measured 2026-10-08; a deviation is itself a finding): 354 rows per CSV;
3 duplicate keys per CSV at the `*-00004`/`*-00013`/`*-00019` pattern; 1 fully-blank row per
CSV; `1900-01-01T00:00:00` in each timestamp column; `confidence` max 1.42; `REC-0001` as the
first-row key of all six CSVs; 1 orphan FK each in `tracking_events` and `carrier_bookings`;
3 shipments with duplicate carrier bookings; 983 of 3,000 events (32.8%) with null `correlation_id`.

**Inputs.** `data/synthetic/*`; `data/manifest.json`; `data/quality_issues.json`.
**Depends on.** **A1** — profiling must run against the tagged baseline so the figures are
attributable to a known commit.
**Why.** Challenge 2 requires a data-quality baseline, and Stage D's semantic layer cannot
define enum domains (**F-37**) without first measuring the actual value distributions. This
step also establishes the oracle for the Stage H data-quality regression tests, and surfaces
**F-54**: because `sanity_check.py` asserts exactly 354 rows, remediation cannot delete rows
in place.
**Outputs.** `docs/04-baseline-kpis/baseline-data-quality.md`;
`docs/07-repo-assessment/` data section.
**Evidence.** Profiling script + full JSON/CSV output + the comparison against the declared
manifest. → `evidence/04-baseline-kpis/EVD-C-05-data-profile.json`
**Addresses.** F-30, F-33–F-38, F-42, F-54. **Rubric.** 1, 2.

---

### Step C6 — Perform root-cause analysis

**Action.** For the material findings, perform evidence-based causal analysis across process,
people, policy, data, technology, organisation and architecture using 5-Whys, Fishbone or
causal trees. For every proposed cause record supporting evidence, contradictory evidence,
confidence and validation method. **Never label correlation as causation without evidence.**
At minimum, trace the causal chain behind the three structural problems in Document 01 §6.

**Inputs.** Document 01; C2–C5 outputs; `docs/ADR/0001-partial-modernization.md`.
**Depends on.** **C2, C3, C4, C5** — causal analysis requires the observed behaviour, the
measured data and the landscape; performing it earlier produces plausible narrative rather
than evidence.
**Why.** Without it, Stage G sequences a backlog of symptoms. `ADR-0001` already states the
root cause of an entire class of findings — *"Accepted, but never revisited… business rules
and audit behavior now differ across code paths"* — which is why Step F1 must supersede that
ADR rather than merely add to it.
**Outputs** (`docs/06-root-cause/`): `root-cause-tree.md`, `five-whys.md`,
`fishbone-analysis.md`, `causal-hypotheses.md`, `evidence-confidence-matrix.md`,
`validation-plan.md`, `confirmed-root-causes.md`, `root-cause-readiness.md`.
**Evidence.** Evidence-confidence matrix with a confidence level per cause.
**Addresses.** F-53; Challenge 1. **Rubric.** 1.

---

### Step C7 — Perform the deep brownfield repository assessment

**Action.** Analyse architecture drift, module boundaries, dependencies, duplication,
complexity, obsolete libraries, legacy patterns, partial migrations, configuration, data
handling, security, testability, observability and maintainability. Identify the critical
workflows whose behaviour must be preserved. Produce the characterization test plan.
**Do not refactor.**

**Inputs.** C2–C6; Document 01 findings register.
**Depends on.** **C3** (test and coverage baseline), **C4** (landscape), **C6** (root causes)
— the assessment must explain *why* debt exists, not just that it does.
**Why.** This is the artifact Stage G sequences from and Stage H executes against. The
critical-workflow inventory is the contract that Step H10's behaviour-difference report is
judged against.
**Outputs** (`docs/07-repo-assessment/`): `repo-assessment.md`, `architecture-drift.md`,
`dependency-map.md`, `technical-debt-register.md`, `legacy-pattern-register.md`,
`partial-migration-register.md`, `critical-workflow-inventory.md`,
`characterization-test-plan.md`, `security-code-quality-findings.md`,
`maintainability-assessment.md`, `repo-transformation-readiness.md`.
**Evidence.** Technical-debt register cross-referenced to all 57 finding IDs.
**Addresses.** All of Document 01; Challenges 1 and 2. **Rubric.** 1.

---

### Step C8 — Author and commit characterization tests pinning current behaviour

**Action.** Implement the C7 characterization plan as **additive tests only**. No application
file may be modified. At minimum, pin:

1. `load_record('DOES-NOT-EXIST')` returns the **first row of `shipments.csv`**, asserted by
   its actual field values — not merely `isinstance(dict)` as the delivered test does (F-51).
2. `load_record('REC-0001')` is ambiguous across all six entity types (F-30).
3. `load_record` matches on non-key columns because it scans `row.values()` (F-31).
4. `GET /records/{id}` with **no** `X-User-Role` header succeeds (default `operator`) (F-17).
5. `GET /records/{id}` with `X-User-Role: clinician` succeeds (F-19).
6. `POST /ai/summarize/{id}` succeeds with no role header at all (F-20).
7. The AI response always carries `guardrail_status == "not_enforced"` (F-24).
8. The AI `summary` echoes the record's first column value (F-29).
9. The audit event contains no actor and no correlation ID (F-43).
10. `/health` returns `ok` regardless of data-layer availability (F-46).
11. `run_daily_batch` reports malformed rows and exits `0` (F-40).

Mark each test `@pytest.mark.characterization` and document in its docstring whether the
pinned behaviour is **intended legacy behaviour** or a **defect scheduled for approved
change**.

**Inputs.** C7 characterization test plan; C3 baseline; A5 write boundaries.
**Depends on.** **C7** (the plan), **A5** (this is the one Stage C write action and must be
inside the agreed write boundary), **C3** (the suite must be executable first).
**Why.** Spine 7 requires characterization tests *before* refactoring. These tests are what
make Stage H safe: when Step H5 changes `load_record` to return 404, test 1 will fail, and
that failure is the **proof of an intentional, approved behaviour change** rather than a
regression. Without them, Step H10 cannot distinguish the two, and the Challenge 15
acceptance standard cannot be met. The explicit intended-versus-defect labelling is what the
Challenge 2 acceptance standard asks for.
**Outputs.** `tests/characterization/` (new); updated `docs/07-repo-assessment/characterization-test-plan.md`.
**Evidence.** JUnit XML showing all characterization tests green against
`baseline/v0.1-as-delivered-bytes` behaviour; commit SHA; tag `baseline/v1-characterized`.
→ `evidence/07-repo-assessment/EVD-C-08-characterization-junit.xml`
**Addresses.** F-17, F-19, F-20, F-24, F-29, F-30, F-31, F-32, F-40, F-43, F-46, F-51.
**Rubric.** 1, 4.

---

### Step C9 — Stage C gate review

**Outputs.** `docs/07-repo-assessment/stage-c-gate.md`.

### Stage C exit criteria

| # | Criterion | Verification method |
|---|---|---|
| C-X1 | KPI definitions are frozen, signed off, and every proxy is labelled as such | `kpi-baseline-signoff.md` is signed; `proxy-metrics.md` lists limitations per proxy |
| C-X2 | The documented quick-start failure is recorded with a full transcript and exit codes | `EVD-C-02` exists and shows the `httpx` and module-path failures |
| C-X3 | Baseline test results, coverage and smoke results are captured as machine-readable artifacts | JUnit XML and coverage XML present in `evidence/07-repo-assessment/` |
| C-X4 | The data profile reproduces the expected figures in Step C5, or every deviation is logged as a new finding | Compare `EVD-C-05` against Step C5 expected results |
| C-X5 | Every declared business flow is mapped to implementing code or explicitly marked `NOT IMPLEMENTED` | Flow-to-code trace table is complete |
| C-X6 | Each confirmed root cause carries supporting evidence, contradictory evidence and a confidence level | `evidence-confidence-matrix.md` has no blank cells |
| C-X7 | Characterization tests exist for all 11 behaviours in Step C8 and all pass | `EVD-C-08` JUnit XML |
| C-X8 | Each characterization test is labelled intended-legacy or defect-scheduled-for-change | Docstring review of every test |
| C-X9 | No application file changed: `git diff baseline/v0.1-as-delivered-bytes -- apps etl legacy data scripts infra policy` is empty | Git diff |
| C-X10 | Tag `baseline/v1-characterized` exists | `git show` |

---

# STAGE D — Semantic Layer Extraction

**Source of requirement:** Challenge Guide page 6 (*Develop & Extract Semantic Layer → Develop
PRD → Develop APP → Demo → Test Semantic Layer with new model → Compare and contrast APPs*)
and `Semantic_Layer_capture.pdf`. **Mode:** Read-only with respect to application code;
creates the new `semantic-layer/` tree.

**Why this stage sits here.** The Challenge Guide places semantic-layer extraction *before*
PRD development. The layer is the model-independent definition of the business domain; Stage Q
regenerates the application from it using a second model and compares the results. If the
semantic layer were derived from the PRD instead, the Stage Q comparison would be testing the
PRD, not the layer.

---

### Step D1 — Extract the glossary and entity definitions

**Action.** Author `semantic-layer/glossary.md` (human explanation) and
`semantic-layer/entities.yaml` (source of truth) covering the six entities and every field in
`docs/domain-specific-spec.md`. For each field record: name, type, unit, nullability, whether
it is a business key, an example value, and the **observed** value domain from Step C5.

**Inputs.** `docs/domain-specific-spec.md`; C5 data profile; CSV headers.
**Depends on.** **C5** — field *declarations* come from the spec but field *domains* can only
come from measurement; defining enums from the spec alone would reproduce **F-37** in the very
artifact meant to fix it.
**Why.** `Semantic_Layer_capture.pdf` is explicit: *Markdown explains it. YAML defines it.*
The glossary serves human reviewers and auditors; the YAML is what the application, tests and
Stage Q model generation consume.
**Outputs.** `semantic-layer/README.md`, `glossary.md`, `entities.yaml`.
**Evidence.** Field-coverage table proving every column of all six datasets is defined.
→ `evidence/11-data-context/EVD-D-01-field-coverage.csv`
**Addresses.** F-37; Challenge 1. **Rubric.** 1, 2.

---

### Step D2 — Derive the status taxonomy and enum domains

**Action.** Author `semantic-layer/status-taxonomy.yaml`. Define legal values for every
categorical field. Then explicitly record the **observed violations** from C5: the fourteen
status-like tokens (`not_enforced`, `approved`, `rejected`, `pending`, `legacy`, `internal`,
`standard`, `degraded`, `manual`, `normal`, `vendor`, `high_risk`, `requires_review`,
`ai_assisted`) that appear interchangeably across `service_tier`, `model`, `timezone`,
`weather_risk`, `human_override` and others, and for each state whether the correct remedy is
a data fix, a schema fix or a declared legacy-tolerance rule.

**Inputs.** D1 entity definitions; C5 categorical distributions.
**Depends on.** **D1** (fields must exist before their domains do), **C5** (the violation
list is a measurement).
**Why.** **F-37** is the root data finding: there is no semantic layer, so a `timezone` can
be `rejected` and a `model` can be `approved`. Every downstream control depends on fixing
this — policy cannot evaluate `purpose` if `service_tier` is not a closed set, and AI output
cannot be schema-validated against an undefined enum.
**Outputs.** `semantic-layer/status-taxonomy.yaml`; `semantic-layer/enum-violations.md`.
**Evidence.** Violation table: field → illegal values observed → count → proposed remedy.
→ `evidence/11-data-context/EVD-D-02-enum-violations.csv`
**Addresses.** F-37, F-36. **Rubric.** 1, 2.

---

### Step D3 — Define relationships, business rules and metrics

**Action.** Author `relationships.yaml` (cardinality, foreign keys, ordering semantics for
`tracking_events.sequence_no`, saga relationships between `shipments` and
`carrier_bookings`), `business-rules.yaml` (invariants — e.g. *a route flagged
`restricted_zone_flag: true` must not be assigned without an explicit override*;
*`confidence` ∈ [0,1]*; *a shipment has at most one active carrier booking*), and
`metrics.yaml` (the frozen C1 KPI definitions, expressed as computable definitions).

**Inputs.** D1, D2; C1 frozen KPIs; C5 referential-integrity findings;
`docs/architecture/known-gaps.md`.
**Depends on.** **D1, D2** (rules reference entities and closed value sets), **C1** (metrics
must be the frozen definitions, not new ones — the spine forbids redefining KPIs later).
**Why.** The six declared brownfield gaps (`duplicate_tracking_events`, `stale_gps`,
`timezone_mismatch`, `duplicate_carrier_booking`, `route_ignores_restrictions`,
`location_data_overexposure`) are all expressible as violated invariants. Writing them as
machine-readable rules here is what makes Stage F policy-as-code and Stage L adversarial
testing possible without re-deriving them.
**Outputs.** `semantic-layer/relationships.yaml`, `business-rules.yaml`, `metrics.yaml`.
**Evidence.** Rule-to-gap trace table covering all six declared gaps.
**Addresses.** F-36, F-38, F-39; `docs/architecture/known-gaps.md`. **Rubric.** 2.

---

### Step D4 — Define access semantics and AI context policy

**Action.** Author `access-semantics.yaml`: for each of the eight personas, the entities and
fields they may read or write, under which purpose, scope and risk conditions — including
field-level treatment of `current_location`, `driver_id` and route data
(`location_data_overexposure`). Author `ai-context-policy.yaml`: which fields may enter a
prompt, which must be redacted or tokenised, maximum context size, what provenance must
accompany retrieved content, and which outputs require human approval.

**Inputs.** D1–D3; `docs/domain-specific-spec.md` personas; `security/threat-model.md`;
B2 decision rights.
**Depends on.** **D1** (field-level rules need field definitions), **B2** (persona authority
must reflect confirmed or explicitly provisional decision rights).
**Why.** **F-18** and **F-21** show authorisation is role-only with no resource, purpose or
context input, and **F-22** shows the whole record enters the prompt. Those two defects share
a single root cause: no declarative statement of who may see what, for what purpose. This file
becomes the direct input to the Stage F policy model and the Stage J prompt construction, so
the same semantics govern both the API and the model — which is what closes the gap that
`ADR-0001` describes.
**Outputs.** `semantic-layer/access-semantics.yaml`, `semantic-layer/ai-context-policy.yaml`.
**Evidence.** Persona × entity × field × purpose matrix.
→ `evidence/11-data-context/EVD-D-04-access-semantics-matrix.csv`
**Addresses.** F-16, F-18, F-21, F-22. **Rubric.** 2, 3.

---

### Step D5 — Add schema validation, conformance tests and generated JSON

**Action.** Author `semantic-layer/schemas/semantic-layer.schema.json` validating every YAML
file. Author `semantic-layer/tests/test_semantic_layer.py` asserting: the YAML validates
against the schema; every entity field in `entities.yaml` exists in the corresponding CSV
header and vice versa; every categorical field has a declared domain; every business rule is
machine-evaluable; every KPI in `metrics.yaml` matches a frozen C1 definition. Generate
`semantic-layer/generated/semantic-layer.json` from the YAML as the machine-consumable form,
with generation automated and the output treated as a build artifact.

**Inputs.** D1–D4; CSV headers; C1 KPI definitions.
**Depends on.** **D1–D4** — there must be something to validate.
**Why.** `Semantic_Layer_capture.pdf`: *JSON Schema validates it. Tests protect it. Generated
JSON serves it.* Without the tests the layer drifts from the data within one sprint, which is
exactly how **F-37** and **F-50** arose. Generating the JSON rather than hand-writing it
guarantees the application and the model consume the same definitions the auditors read.
**Outputs.** `semantic-layer/schemas/`, `semantic-layer/tests/`, `semantic-layer/generated/`.
**Evidence.** Test run JUnit XML; schema validation output; generated JSON.
→ `evidence/11-data-context/EVD-D-05-*`
**Addresses.** F-37, F-50. **Rubric.** 2, 4.

---

### Step D6 — Stage D gate review

**Outputs.** `docs/11-data-context/stage-d-gate.md` (summarising the layer and linking to it).

### Stage D exit criteria

| # | Criterion | Verification method |
|---|---|---|
| D-X1 | All nine files from `Semantic_Layer_capture.pdf` exist | Directory listing of `semantic-layer/` |
| D-X2 | Every column of all six datasets is defined in `entities.yaml` | `EVD-D-01` field-coverage table shows 100% |
| D-X3 | Every categorical field has a declared domain, and all observed violations are listed with a remedy | `EVD-D-02`; no blank remedy cells |
| D-X4 | All six declared brownfield gaps are expressed as machine-readable rules | Rule-to-gap trace table |
| D-X5 | `metrics.yaml` matches the frozen C1 definitions exactly | Automated diff against `kpi-dictionary.md` |
| D-X6 | Semantic-layer tests pass and the JSON is generated, not hand-written | JUnit XML; generation command in `MANIFEST.md` |
| D-X7 | The layer contains no model-specific, framework-specific or vendor-specific content | Reviewer read-through — required for the Stage Q comparison to be valid |

---

# STAGE E — Intervention Qualification & Initial PRD

**Spine stages:** 8, 9. **Mode:** Read-only.

---

### Step E1 — Decide AI versus no-AI for each intervention

**Action.** Evaluate every candidate intervention against process redesign, policy change,
deterministic software, rules engines, workflow automation, analytics, classical ML, GenAI and
agentic AI. Apply **minimum necessary intelligence** and **minimum necessary agency**. For each
proposed AI use, state explicitly what uncertainty, language, reasoning, generation or adaptive
decision requirement justifies it. **Reject AI where a conventional approach is safer, cheaper
or more reliable.** Assess the three declared AI capabilities (ETA Prediction, Route
Optimization, Exception Copilot) individually.

**Inputs.** B3 problem framing; C6 root causes; C7 assessment; D3 business rules.
**Depends on.** **B3** (technology-neutral problem), **C6** (causes — AI applied to a process
defect is waste), **D3** (a requirement expressible as a deterministic invariant does not need
a model).
**Why.** **F-29** shows the current AI output is not derived from the record's meaning and the
three declared capabilities are unimplemented, so there is no incumbent to defend. Several
findings — restricted-zone enforcement (**F-39** adjacent), duplicate booking detection
(**F-38**), confidence bounds (**F-36**) — are deterministic rules, and the honest outcome is
likely that route-constraint enforcement is *not* an AI problem while exception triage may be.
Saying so in writing is what Challenge 9's acceptance standard protects.
**Outputs** (`docs/08-ai-qualification/`): `intervention-options.md`, `ai-vs-no-ai-matrix.md`,
`deterministic-vs-ai-boundaries.md`, `minimum-intelligence-assessment.md`,
`minimum-agency-assessment.md`, `intervention-hypothesis.md`, `qualification-decision.md`.
**Evidence.** The matrix, with a justification and a rejected-alternative column per row.
**Addresses.** F-29; Challenge 9; OQ-02. **Rubric.** 2.

---

### Step E2 — Reconcile economics with the Stage 0C envelope

**Action.** Compare the E1 decision against the A6 provisional envelope. **Retire AI cost
assumptions for every intervention where AI was rejected.** Where AI was retained, confirm the
cost-per-request, cost-per-case, latency and context ceilings still hold, and record any that
must change and why.

**Inputs.** A6 envelope; E1 decision.
**Depends on.** **A6** (the envelope to reconcile against), **E1** (what survived).
**Why.** Spine 0C states plainly that Stage 8 determines whether the AI-specific portions
remain applicable. Carrying retired assumptions forward is how FinOps baselines become
fiction — and Stage N Step N4 measures actuals against exactly these numbers.
**Outputs.** `docs/08-ai-qualification/economics-baseline-reconciliation.md`.
**Evidence.** Before/after envelope comparison with retired assumptions struck through, not
deleted.
**Addresses.** F-28; OQ-02, OQ-03. **Rubric.** 2.

---

### Step E3 — Produce the Initial PRD

**Action.** Create the Initial PRD from validated discovery and qualification: problem,
personas, journeys, capabilities, functional requirements, NFRs, exclusions, constraints,
dependencies, success metrics, risks, MVP scope, future scope and unresolved questions.
**Trace every requirement to a business problem and to evidence.** Resolve **OQ-06** (whether
the operator portal is in scope) here, because MVP scope depends on it.

**Inputs.** B3; C1 frozen KPIs; C7 critical workflows; D1–D4 semantic layer; E1, E2.
**Depends on.** **E1** (a PRD must not specify AI that was not justified), **D1–D4** (the PRD
uses the semantic layer's vocabulary so that requirements, specs and the Stage Q regeneration
all speak one language), **C1** (success metrics must be the frozen KPIs).
**Why.** Rubric criterion 4 (25 marks) scores PRD quality and requirement traceability
directly. Tracing to evidence rather than to opinion is what makes it defensible, and the
Stage R requirement-disposition matrix classifies each of these requirements as Delivered /
Changed / Deferred / Rejected / Superseded.
**Outputs** (`docs/09-initial-prd/`): `initial-prd.md`, `capability-map.md`,
`functional-requirements.md`, `nfrs.md`, `mvp-scope.md`, `non-goals.md`,
`release-hypothesis.md`, `product-risks.md`, `open-product-decisions.md`,
`initial-prd-traceability.md`.
**Evidence.** Traceability table: requirement → business problem → evidence source.
**Addresses.** Challenges 1, 9; OQ-06, OQ-12. **Rubric.** 4.

---

### Step E4 — Stage E gate review

**Outputs.** `docs/09-initial-prd/stage-e-gate.md`.

### Stage E exit criteria

| # | Criterion | Verification method |
|---|---|---|
| E-X1 | Every intervention has an explicit AI / no-AI decision with a written justification | `ai-vs-no-ai-matrix.md` has no blank justification cells |
| E-X2 | At least one candidate AI use has been **rejected** in favour of a deterministic approach, or the absence of any rejection is itself justified | Reviewer read of `deterministic-vs-ai-boundaries.md` |
| E-X3 | Economics are reconciled and retired assumptions are struck through, not deleted | `economics-baseline-reconciliation.md` |
| E-X4 | Every PRD requirement traces to a business problem and an evidence source | `initial-prd-traceability.md` has no orphan rows |
| E-X5 | PRD success metrics are identical to the frozen C1 KPI definitions | Automated diff |
| E-X6 | MVP scope decision on the operator portal (OQ-06) is recorded with an owner | `mvp-scope.md` |

---

# STAGE F — Target Architecture, Data & Context Strategy, Specs, Traceability

**Spine stages:** 10, 11, 12, 13. **Mode:** Read-only.

---

### Step F1 — Develop the target architecture and ADRs

**Action.** Develop and compare architecture options across application, frontend/backend,
APIs, AI/model, data, knowledge, integration, security, identity, observability, human control
and deployment. Evaluate against functional requirements, NFRs, security, portability, cost,
latency, scalability, resilience and maintainability. Write one ADR per material decision.
**Explicitly supersede `ADR-0001`** with a decision that resolves the legacy/modern divergence
it records. Resolve **OQ-01** (target platform) and **OQ-07** (identity provider) here.

**Inputs.** E3 Initial PRD; C7 assessment; C6 root causes; D4 access semantics;
`docs/architecture/target-state-principles.md`; `docs/ADR/0001-partial-modernization.md`.
**Depends on.** **E3** (architecture serves requirements), **C6** (it must address root
causes, not symptoms), **C7** (it must account for what exists).
**Why.** **F-53** records an accepted-but-never-revisited decision whose stated consequence is
that business rules and audit behaviour differ across code paths. Leaving it standing means
every later control has two implementations and the Stage R audit chain has two answers.
Superseding it with a dated, owned ADR is the single highest-leverage architectural act in this
runbook.
**Outputs** (`docs/10-architecture/`): `architecture-options.md`, `target-architecture.md`,
`component-model.md`, `integration-architecture.md`, `deployment-architecture.md`,
`security-architecture.md`, `model-service-scorecard.md`, `architecture-risk-register.md`,
`architecture-decision-summary.md`; plus `docs/10-architecture/adrs/` with one ADR per
decision including `ADR-00XX-supersede-0001-partial-modernization.md`.
**Evidence.** Options-comparison matrix; ADR set; supersession record.
**Addresses.** F-53; OQ-01, OQ-07; Challenge 5. **Rubric.** 2.

---

### Step F2 — Define the data, knowledge and context strategy

**Action.** Define sources, ownership, schemas, contracts, quality rules, lineage, provenance,
freshness, retention, metadata, PII and access controls. Define ingestion, indexing, retrieval,
grounding, context assembly, compaction and provenance/citation requirements. Define the
synthetic-data strategy. Promote the D2/D3 rules into executable **data-quality rules** with
thresholds and quarantine semantics, and resolve **OQ-14** (whether remediation occurs in a
derived layer or by versioning `data/manifest.json`).

**Inputs.** D1–D5 semantic layer; C5 data profile; F1 architecture; `data/manifest.json`.
**Depends on.** **D1–D5** (the semantic layer *is* the schema and rule source; defining
contracts separately would create a second source of truth and re-create F-37), **C5** (quality
thresholds must be set against measured defect rates), **F1** (storage and retrieval choices
follow the platform decision from OQ-01).
**Why.** **F-54** means a naive fix breaks `scripts/sanity_check.py`. The strategy must state
where remediation happens — the runbook's recommendation is a derived, versioned `curated`
layer leaving `data/synthetic/` immutable as the declared fixture, which satisfies both the
manifest contract and the quality requirement. The provenance policy is also what makes the
Stage R audit chain reconstructable, addressing **F-42**.
**Outputs** (`docs/11-data-context/`): `data-source-inventory.md`, `data-contracts.md`,
`data-quality-rules.md`, `lineage-map.md`, `knowledge-model.md`, `metadata-model.md`,
`retrieval-strategy.md`, `context-engineering-strategy.md`, `context-compaction-policy.md`,
`provenance-policy.md`, `synthetic-data-strategy.md`, `data-context-risks.md`.
**Evidence.** Data-quality rule set with thresholds; lineage map; OQ-14 ruling.
**Addresses.** F-37, F-38, F-40, F-41, F-42, F-54; Challenge 11. **Rubric.** 2.

---

### Step F3 — Produce implementation-ready specifications

**Action.** Convert approved product intent and architecture into specifications: feature and
system behaviour, APIs, events, schemas, state transitions, business rules, errors,
constraints, security, observability, NFRs and acceptance criteria. **Specify the complete
OpenAPI contract for all endpoints**, closing **F-50**. Specify the audit event schema with
actor, correlation ID, tenant, resource, policy decision, model and prompt version, input hash
and approval ID, closing **F-43**. Specify the AI output schema and the refusal/abstention
path, closing **F-25**. **Do not implement material ambiguity** — unresolved items go to
Document 04.

**Inputs.** F1 architecture; F2 data strategy; D1–D5; E3 PRD; `observability/otel-notes.md`.
**Depends on.** **F1** (specs realise the architecture), **F2** (API and event contracts must
use the agreed data contracts), **D5** (schemas derive from the validated semantic layer so
there is exactly one definition of an entity).
**Why.** Stage H is judged against these specs, and Stage L's TEVV thresholds are derived from
their acceptance criteria. `observability/otel-notes.md` has already written the required AI
telemetry fields — token count, latency, model version, fallback reason, guardrail result —
and this is where they become binding.
**Outputs** (`docs/12-specs/` and `docs/12-specs/features/`): `system-spec.md`, per-feature
specs, `api-contracts.md`, `event-contracts.md`, `schema-specifications.md`,
`interface-contracts.md`, `business-rules.md`, `error-handling-spec.md`, `security-spec.md`,
`observability-spec.md`, `nfr-spec.md`, `acceptance-criteria.md`, `spec-readiness.md`.
**Evidence.** Complete OpenAPI document covering every endpoint; audit and AI output schemas.
→ `evidence/12-specs/`
**Addresses.** F-25, F-27, F-42, F-43, F-45, F-46, F-50. **Rubric.** 2, 4.

---

### Step F4 — Build the requirements → specs → tests → evidence traceability matrix

**Action.** Build bidirectional traceability for functional, data, AI-quality, security,
privacy, resilience, performance, observability and cost requirements:
requirement → spec → planned implementation → test/evaluation → evidence. Detect orphan
requirements, untested specs, unjustified implementation and unverifiable criteria.
**Critical unexplained gaps block progression.**

**Inputs.** E3 requirements; F1–F3; C8 characterization tests; Document 01 findings register.
**Depends on.** **E3, F3** (both ends of the chain must exist), **C8** (characterization tests
are the existing-behaviour anchor of the test column).
**Why.** Rubric criterion 4 names traceability explicitly, and the spine blocks progression on
unexplained gaps. Including the 57 finding IDs as a traceability dimension means a reviewer can
ask *"what happened to F-22?"* and follow a single row to its remediation, its test and its
evidence file. That question is the likeliest one a CTO asks, and it should have a one-line
answer.
**Outputs** (`docs/13-traceability/`): `requirements-traceability-matrix.md`,
`spec-to-test-map.md`, `test-to-evidence-map.md`, `security-traceability.md`,
`data-traceability.md`, `ai-quality-traceability.md`, `resilience-traceability.md`,
`cost-traceability.md`, `coverage-gap-register.md`, `traceability-summary.md`.
**Evidence.** The matrices, plus a finding-ID → remediation → test → evidence index.
→ `evidence/13-traceability/EVD-F-04-finding-coverage-matrix.csv`
**Addresses.** All findings; Challenge 14. **Rubric.** 1, 4.

---

### Step F5 — Stage F gate review

**Outputs.** `docs/13-traceability/stage-f-gate.md`.

### Stage F exit criteria

| # | Criterion | Verification method |
|---|---|---|
| F-X1 | Every material architecture decision has an ADR, and `ADR-0001` is formally superseded | ADR index; supersession note in `0001` |
| F-X2 | OQ-01 (platform) and OQ-07 (identity provider) are resolved with named owners | `architecture-decision-summary.md` |
| F-X3 | Data-quality rules have thresholds, and OQ-14 (remediation location) is ruled on | `data-quality-rules.md`; `synthetic-data-strategy.md` |
| F-X4 | The OpenAPI contract covers **every** endpoint, not just `/health` | Automated route-coverage diff against `apps/api/main.py` |
| F-X5 | The audit event schema includes actor, correlation ID, policy decision, model version, input hash and approval ID | Schema review |
| F-X6 | The AI output schema includes a refusal/abstention path | Schema review |
| F-X7 | Every requirement traces forward to a test and backward to a business problem | `coverage-gap-register.md` contains no unexplained gaps |
| F-X8 | All 57 findings appear in the finding-coverage matrix with a disposition | `EVD-F-04` row count = 57 |
| F-X9 | No material ambiguity has been passed to implementation | Every ambiguity is an open question with an owner |

---

# STAGE G — Transformation & Migration Planning

**Spine stage:** 14. **Mode:** Read-only. **This is the last read-only stage.**

---

### Step G1 — Build and sequence the transformation backlog

**Action.** Convert the findings register and the Stage F specs into a sequenced backlog.
Sequence by: (1) controls that make later work provable; (2) S1 security and identity
findings; (3) data and semantic correctness; (4) AI boundary; (5) resilience and observability;
(6) feature work. Explicitly identify **components that should remain unchanged**.

**Inputs.** Document 01; C7 technical-debt register; F3 specs; F4 traceability.
**Depends on.** **F4** — sequencing without traceability optimises for visible change rather
than risk reduction; **C7** — the critical-workflow inventory determines what must not move.
**Why.** Spine 14 requires explicit identification of what stays unchanged. Document 01 §7
lists eight assets that are genuinely sound — `sanity_check.py`, `manifest.json`,
`domain-specific-spec.md`, `known-gaps.md`, the failure-injection drills,
`otel-notes.md`, the evidence-pack template, the target-state principles. A transformation that
discards these loses its own oracle, and **F-55** means deleting two of them breaks the smoke
gate outright.
**Outputs** (`docs/14-transformation/`): `transformation-backlog.md`, `migration-roadmap.md`,
`dependency-sequence.md`.
**Evidence.** Backlog with a finding-ID column and a do-not-change register.
**Addresses.** F-54, F-55; Document 01 §7. **Rubric.** 2.

---

### Step G2 — Design coexistence, adapters, flags and schema migration

**Action.** Define coexistence between the legacy path (`legacy/`, `etl/`) and the modern
path (`apps/api/`), adapter strategy, backward compatibility, feature flags, and schema and
data migration. Specify how the derived data layer from F2 coexists with the immutable
`data/synthetic/` fixture that `sanity_check.py` asserts against.

**Inputs.** G1 backlog; F1 architecture; F2 data strategy; `docs/ADR/0001`.
**Depends on.** **G1** (sequence determines how long coexistence must last), **F2** (the
migration target is the agreed data contract).
**Why.** `ADR-0001` created the divergence; this step retires it safely rather than by
deletion. Feature flags matter specifically for Step H5 (record-identity semantics) and
Step H7 (AI guardrails), where the change is a deliberate behaviour change that must be
reversible in production.
**Outputs** (`docs/14-transformation/`): `coexistence-strategy.md`, `adapter-strategy.md`,
`schema-migration-plan.md`, `feature-flag-plan.md`.
**Evidence.** Coexistence design with the retirement trigger for each legacy path.
**Addresses.** F-53, F-54; Challenge 14. **Rubric.** 2.

---

### Step G3 — Define cutover, rollback and transformation gates

**Action.** Define cutover, rollback and verification for each increment, and the gates each
increment must pass before merge. Minimum gate set: characterization tests green or
difference explained and approved; lint, type and security scans clean or waived with an
owner; semantic-layer tests green; evidence artifacts produced.

**Inputs.** G1, G2; F3 acceptance criteria; C8 characterization tests.
**Depends on.** **C8** (the characterization suite *is* the primary rollback trigger — an
unexplained characterization failure means the change was not the change that was planned),
**G2** (rollback must account for coexistence state).
**Why.** Spine 14 requires transformation gates, and Challenge 15's acceptance standard is
that readiness states what is ready, what is not and what risk is accepted. Defining the gate
before Stage H begins prevents the gate from being negotiated downward once work is in flight.
**Outputs** (`docs/14-transformation/`): `cutover-plan.md`, `rollback-strategy.md`,
`transformation-risks.md`, `transformation-gates.md`.
**Evidence.** Gate definition table.
**Addresses.** Challenges 14, 15. **Rubric.** 2.

---

### Step G4 — Obtain written authorisation to modify the repository

**Action.** Present the backlog, the do-not-change register, the gate definitions and the
rollback strategy to the Repository Owner and the Business Sponsor. Obtain and record written
authorisation to begin Stage H, naming the permitted scope. Update the A5 operating contract
from `PROVISIONAL` to authorised for the components covered.

**Inputs.** G1, G2, G3; A5 operating contract; B2 approval-authority map.
**Depends on.** **G1–G3** (there must be a plan to authorise), **B2** (there must be an
identified approver — this is where **OQ-05** becomes blocking rather than deferred).
**Why.** Every stage to this point has been read-only by design. Spine 0B states that
discovery stages are read-only *unless the prompt explicitly authorises modification*, and
Spine 15 states that implementation may be modified *only within approved Stage 0B boundaries*.
This step is that authorisation. Without it, Stage H work is out of contract and its evidence
is inadmissible at the Stage R review. See **OQ-11**.
**Outputs.** `docs/14-transformation/transformation-authorisation.md`;
updated `docs/00-preflight/operating-contract/provisional-operating-contract.md`.
**Evidence.** Signed authorisation record with scope, date and approver.
→ `evidence/14-transformation/EVD-G-04-authorisation.pdf`
**Addresses.** F-08; OQ-05, OQ-11. **Rubric.** 3.

---

### Step G5 — Stage G gate review

**Outputs.** `docs/14-transformation/stage-g-gate.md`.

### Stage G exit criteria

| # | Criterion | Verification method |
|---|---|---|
| G-X1 | Every backlog item references at least one finding ID or specification | Backlog column completeness |
| G-X2 | The do-not-change register includes all eight assets from Document 01 §7 | Cross-check |
| G-X3 | Sequencing places evidence and control work before feature work | Reviewer read of `dependency-sequence.md` |
| G-X4 | Every deliberate behaviour change has a feature flag and a rollback path | `feature-flag-plan.md` vs `rollback-strategy.md` |
| G-X5 | Transformation gates are defined and are not negotiable per-increment | `transformation-gates.md` |
| G-X6 | **Written authorisation to modify the repository exists, naming scope and approver** | `EVD-G-04` |
| G-X7 | Repository application code still matches `baseline/v0.1-as-delivered-bytes` | `git diff` empty |

---

# STAGE H — Repo 2.0: Modernization & Validation

**Spine stages:** 15, 16. **Mode:** Write — the first stage that changes application
behaviour. **Precondition: Step G4 authorisation must exist.**

**Working method for every step in this stage:** small reviewable increment → run the full
suite including characterization tests → explain every characterization difference as either
*approved behaviour change* (citing the spec) or *regression* (revert) → commit with the
finding IDs in the message → append to `docs/15-modernization/transformation-log.md`.

---

### Step H1 — Establish repository structure, tooling and quality gates

**Action.** Add `CODEOWNERS`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE` and a PR template.
Introduce `ruff`/`black`, `mypy`, `pytest-cov` and `pre-commit` with secret scanning. Replace
the no-op `"lint": "echo scaffold"` frontend script. Configure branch protection requiring the
transformation gates from G3.

**Inputs.** G3 gate definitions; G4 authorisation; B2 ownership.
**Depends on.** **G4** (authorisation), **G3** (the gates being enforced must already be
defined), **B2** (CODEOWNERS requires named owners — provisional owners must be recorded as
such, not fabricated).
**Why.** **F-08** (no change control) and **F-06** (a lint gate that always passes) mean every
later change is unreviewed and unchecked. Doing this first means Steps H2–H9 are themselves
produced under the controls they are meant to establish.
**Outputs.** Repository governance files; tool configuration; updated CI.
**Evidence.** First pipeline run showing lint, type and secret scan executing.
→ `evidence/15-modernization/EVD-H-01-pipeline-run.txt`
**Addresses.** F-06, F-08, F-14, F-47. **Rubric.** 2, 3.

---

### Step H2 — Fix reproducibility defects

**Action.** Add `httpx` to `requirements.txt` (**F-02**). Correct the `README.md` run command
to `apps.api.main:app` (**F-03**). Introduce hash-pinned lockfiles for both stacks (**F-04**).
Add a `Dockerfile` and a compose/devcontainer definition giving a one-command environment
(**F-07**). Re-run the Step C2 quick-start verbatim and capture the transcript.

**Inputs.** C2 failing transcript; A3 toolchain snapshot; H1 tooling.
**Depends on.** **C2** — the before-transcript must exist for the after-transcript to prove
anything; **H1** — the fix should flow through the new pipeline.
**Why.** This is the cleanest before/after evidence pair in the engagement: the project's own
documented entry point moves from failing to passing, with both transcripts retained. It
satisfies Challenge 5's acceptance standard that *a new team can reproduce the intended
environment with documented steps*.
**Outputs.** Updated `requirements.txt`, `README.md`, lockfiles, `Dockerfile`.
**Evidence.** After-transcript alongside `EVD-C-02`.
→ `evidence/15-modernization/EVD-H-02-quickstart-after.txt`
**Addresses.** F-02, F-03, F-04, F-07. **Rubric.** 1, 2.

---

### Step H3 — Remove hardcoded secrets and sanitise configuration

**Action.** Remove `SHARED_DB_PASSWORD = "Welcome123"` from `legacy/reconcile_legacy.py`
(**F-09**). Replace `.env.example` with placeholder-only values carrying no credential-shaped
literals (**F-10**, **F-11**, **F-12**) and change `LOG_LEVEL` to `INFO` (**F-13**). Remove the
credential-emitting `local_file` from `infra/terraform/main.tf` (**F-15**). Introduce a secrets
provider per the F1 platform decision, document the rotation plan, and run a full-history
secret scan — treating every value found as compromised and requiring rotation. Produce the
secrets inventory and the sensitive-field handling checklist, including location-data treatment
(**F-16**).

**Inputs.** Document 01 §4.2; F1 security architecture; D4 access semantics; H1 secret scanner.
**Depends on.** **H1** (the scanner must be in place to prove the absence afterwards),
**F1** (the replacement secrets mechanism depends on the platform decision, OQ-01).
**Why.** Challenge 4's acceptance standard is that **no sensitive value should be required in
committed code or unsafe example configuration**. Note that removing a secret from the working
tree does not remove it from history: because Step A1 committed the as-delivered tree, these
values exist in the `baseline/v0.1-as-delivered-bytes` commit. The rotation plan and the history
disposition must both be recorded — this is a real operational consequence of the A1 decision
and must be stated, not quietly handled.
**Outputs.** Sanitised files; `docs/27-hardening/secrets-hardening.md` (seeded here, completed
in Stage M).
**Evidence.** Secret-scan report showing zero findings in the working tree; the history
disposition note; the rotation plan.
→ `evidence/15-modernization/EVD-H-03-secret-scan.json`
**Addresses.** F-09–F-16. **Rubric.** 3.

---

### Step H4 — Replace identity and authorisation; wire the policy engine

**Action.** Remove the `X-User-Role` header trust (**F-17**). Implement authentication per the
OQ-07 decision. Replace the five-role allow-list with contextual RBAC + ABAC evaluating role,
resource, purpose, scope and risk, sourced from `semantic-layer/access-semantics.yaml`
(**F-18**). Remove `clinician` (**F-19**). **Apply authorisation to `/ai/summarize`**
(**F-20**). Extend `policy/opa/access.rego` with resource, purpose and context inputs, add
positive and negative policy tests, and **wire the policy engine into the request path** so it
is enforced rather than decorative (**F-21**). Write negative access tests and a
privilege-reduction backlog.

**Inputs.** D4 access semantics; F1 security architecture; F3 security spec; C8
characterization tests 4, 5, 6.
**Depends on.** **D4** (the policy input model is the semantic layer's access semantics — if
policy is written separately it will drift from the data definitions exactly as **F-37**
happened), **F1/OQ-07** (authentication mechanism), **C8** (tests 4–6 pin the current
permissive behaviour; their failure here is the proof of the approved change).
**Why.** Challenge 3's acceptance standard is that *access decisions must consider role,
resource, purpose, scope and risk context*. Five of the twenty-three S1 findings sit in this
step, and **F-20** — an AI endpoint with no authorisation at all — is the single most
exploitable defect in the repository.
**Outputs.** Rewritten authorisation layer; extended `policy/opa/`; policy tests;
`docs/20-application/access-control-implementation.md`.
**Evidence.** Negative access test results; policy allow/deny matrix; C8 tests 4–6 now failing
with a written approved-change justification.
→ `evidence/15-modernization/EVD-H-04-*`
**Addresses.** F-17–F-21. **Rubric.** 3.

---

### Step H5 — Fix record identity and lookup semantics

**Action.** Replace `record_id in row.values()` with a keyed lookup on the declared business
key from `entities.yaml` (**F-31**). Replace the silent `return rows[0]` fallback with proper
404 semantics (**F-32**). Resolve the `REC-0001` cross-entity collision per the **OQ-15**
ruling — either namespacing identifiers by entity type or correcting the data in the derived
layer (**F-30**). Add bounds validation for `confidence` and the other numeric domains
(**F-36**).

**Inputs.** D1 entity definitions; F2 data contracts; F3 error-handling spec; C8
characterization tests 1, 2, 3; OQ-15 ruling.
**Depends on.** **D1** (the business key must be declared before it can be enforced),
**F3** (404 semantics must be specified before they are implemented), **C8** (tests 1–3 pin the
current behaviour), **OQ-15** (whether the collision is data or design determines the fix).
**Why.** This is the clearest example in the engagement of a **deliberate, approved behaviour
change**. The delivered `test_characterization.py` asserts that a missing record returns a row;
after this step it must not. Document 01 §6.2 explains the compounding risk: an unauthenticated
caller receiving a record they did not request, with an audit log that records neither who they
were nor which record it actually was. Steps H4, H5 and H8 together close that chain.
**Outputs.** Rewritten `domain_service`; updated characterization tests re-labelled as approved
changes; `docs/15-modernization/approved-behavior-changes.md`.
**Evidence.** Before/after behaviour table; the approved-change record citing the spec clause.
→ `evidence/15-modernization/EVD-H-05-behaviour-change.md`
**Addresses.** F-30, F-31, F-32, F-36. **Rubric.** 2, 4.

---

### Step H6 — Harden the ETL path

**Action.** Add quarantine and dead-letter handling for malformed rows (**F-40**), a failure
threshold with a non-zero exit code, a run identifier and watermark for idempotency
(**F-41**), and the data-quality rules from F2 as executable gates. Emit a per-run data-quality
report as an evidence artifact.

**Inputs.** F2 data-quality rules; C5 profile; D3 business rules; OQ-14 ruling.
**Depends on.** **F2** (thresholds and quarantine semantics must be agreed first — a
quarantine with no threshold is just a different silence), **OQ-14** (quarantining into
`data/synthetic/` would break `sanity_check.py` per **F-54**).
**Why.** **F-40** is the mechanism by which every data defect found in Step C5 reaches
downstream decisions unflagged. A per-run report also gives Stage N a real operational signal
where **F-46** shows none exists.
**Outputs.** Rewritten `etl/run_daily_batch.py`; quarantine sink; data-quality report format.
**Evidence.** ETL run showing quarantine counts matching the C5 expected defect counts.
→ `evidence/15-modernization/EVD-H-06-etl-dq-report.json`
**Addresses.** F-40, F-41, F-54. **Rubric.** 2.

---

### Step H7 — Rebuild the AI gateway and establish the deterministic/AI boundary

**Action.** Separate deterministic business logic from probabilistic behaviour. Replace the
`PROMPT_TEMPLATE.format(record=record)` construction with a safe, parameterised prompt built
only from fields permitted by `ai-context-policy.yaml`, with untrusted text delimited and
never formatted (**F-22**, **F-23**). Add input sanitisation and injection defences. Validate
output against the F3 AI output schema with a refusal path (**F-25**). Replace
`guardrail_status: "not_enforced"` with a real evaluated guardrail result (**F-24**). Introduce
a version-controlled prompt registry, model configuration, prompt version, config hash and
input hash (**F-27**). Replace the fabricated token estimate with measured token accounting
and a per-request budget (**F-28**). Implement the approval gate so a recommendation cannot
become an action without a recorded human decision (**F-26**).

**Inputs.** D4 AI context policy; F3 AI output schema and security spec; E1 AI qualification;
A6/E2 economics envelope; C8 characterization tests 7, 8.
**Depends on.** **E1** (only justified AI is built), **D4** (field-level permission is what
makes the prompt safe), **F3** (the output schema must exist to validate against), **E2** (the
budget ceiling), **C8** (tests 7–8 pin the current unguarded behaviour).
**Why.** Challenge 9's acceptance standard — *AI recommendations must not silently become
operational decisions* — is currently violated by construction, and the datasets deliberately
contain injection payloads to prove it. Stage L red-teams this implementation directly, so the
guardrail must be real and evaluated, not a literal.
**Outputs.** Rebuilt `ai_gateway`; `prompts/` registry; `docs/20-application/deterministic-ai-boundary.md`.
**Evidence.** Injection test results against seeded payloads; schema validation results; token
measurement sample. → `evidence/15-modernization/EVD-H-07-*`
**Addresses.** F-22–F-29. **Rubric.** 2, 3, 4.

---

### Step H8 — Rebuild audit and correlation

**Action.** Implement the F3 audit event schema: actor, correlation ID, tenant, resource,
action, policy decision, model and prompt version, input hash, approval ID, outcome
(**F-43**). Propagate a correlation ID through UI → API → service → data access → AI
invocation → policy decision → approval → audit event, and backfill it into the event stream
path so new events are never written without one (**F-42**). Move the audit sink off the local
filesystem to an append-only durable store the application cannot rewrite, with a retention
classification (**F-44**). Replace `datetime.utcnow()` with timezone-aware timestamps
(**F-45**). Make `/health` a real dependency check (**F-46**).

**Inputs.** F3 observability spec and event contracts; `observability/otel-notes.md`;
F1 architecture; C8 characterization tests 9, 10.
**Depends on.** **F3** (the schema), **H4** (an audit record cannot carry an actor until
authentication exists — this ordering is mandatory), **H5** (it cannot carry a correct
resource until record identity is deterministic).
**Why.** This step is what converts the system from unprovable to auditable, and it is the
precondition for the Stage N end-to-end reconstruction demonstration and the Challenge 14
acceptance standard. The dependency on H4 and H5 is the sharpest ordering constraint in the
runbook: instrumenting first would produce a complete audit trail of the wrong actor acting
on the wrong record.
**Outputs.** Rewritten `audit` service; correlation middleware; real health check.
**Evidence.** A single business event traced end to end with every field populated.
→ `evidence/15-modernization/EVD-H-08-trace-sample.json`
**Addresses.** F-42–F-46. **Rubric.** 3.

---

### Step H9 — Complete the contracts and extend the repository gate

**Action.** Publish the full OpenAPI contract covering every endpoint and add contract tests
that fail on drift (**F-50**). Extend `scripts/sanity_check.py` — preserving its existing
assertions per **F-55** — to additionally verify: the semantic layer validates; required
evidence directories exist; no secret-shaped literal is present; the OpenAPI contract matches
the live routes. Update `data/manifest.json` deliberately and in a versioned way if OQ-14 so
ruled (**F-54**).

**Inputs.** F3 API contracts; D5 semantic-layer tests; H3 secret scanning; OQ-14 ruling.
**Depends on.** **H4–H8** (the gate must assert the state those steps establish), **F3** (the
contract), **D5** (the semantic-layer test entry point).
**Why.** Document 01 §7 identifies `sanity_check.py` as the repository's one genuine automated
contract. Extending rather than replacing it keeps continuity with the delivered system and
gives the executing team a single executable answer to *"is this repository still well-formed?"*
**Outputs.** Complete `data/contracts/openapi.yaml`; extended `scripts/sanity_check.py`;
contract tests.
**Evidence.** `make smoke` output showing the extended assertions.
→ `evidence/16-repo-validation/EVD-H-09-smoke.txt`
**Addresses.** F-50, F-54, F-55. **Rubric.** 2.

---

### Step H10 — Produce the behaviour-difference report

**Action.** Compare the Stage C baseline against the transformed system. For **every**
difference, classify it as an **approved behaviour change** citing the specification clause
and the Step G4 authorisation scope, or as a **regression** requiring revert. Explicitly
cover every characterization test from Step C8 that now fails.

**Inputs.** C2, C3, C5, C8 baselines; all H2–H9 outputs; F3 specs; G4 authorisation.
**Depends on.** **C8** (no baseline, no comparison), **H2–H9** (the changes), **G4** (the
authorisation scope against which "approved" is judged).
**Why.** This is the core deliverable of Spine 16 and the evidential heart of rubric criterion
1. A transformation that cannot explain every behaviour difference is indistinguishable from a
rewrite, and the Challenge 2 acceptance standard — distinguishing intended legacy behaviour
from defects — is only demonstrated here, at the end, by showing the distinction held.
**Outputs.** `docs/16-repo-validation/behavior-difference-report.md`;
`docs/15-modernization/behavior-preservation-evidence.md`.
**Evidence.** Difference table: test ID → before → after → classification → spec clause →
approver. → `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv`
**Addresses.** Challenges 2, 15. **Rubric.** 1, 2.

---

### Step H11 — Run the repository validation quality gate

**Action.** Run unit, integration, contract, characterization, security and data-contract
tests, plus static analysis, dependency and architecture-conformance checks. Compare against
the Stage C baseline. Produce the validation sign-off and the remaining-debt register.

**Inputs.** H1–H10; C3 baseline; F1 architecture; G3 gate definitions.
**Depends on.** **H10** (differences must be explained before the gate can pass),
**G3** (the gate criteria).
**Why.** Spine 16 is the quality gate that permits Stage I. The remaining-debt register is what
keeps Stage R honest: debt deferred with an owner and a date is a defensible position, debt
silently dropped is not.
**Outputs** (`docs/16-repo-validation/`): `repo-quality-gate.md`, `regression-results.md`,
`architecture-conformance-report.md`, `test-results.md`, `security-scan-summary.md`,
`dependency-scan-summary.md`, `data-contract-results.md`, `remaining-debt-register.md`,
`validation-signoff.md`.
**Evidence.** All raw scan and test outputs. → `evidence/16-repo-validation/`
**Addresses.** Challenges 7, 13, 15. **Rubric.** 2, 3.

---

### Step H12 — Stage H gate review

**Outputs.** `docs/16-repo-validation/stage-h-gate.md`; tag `repo/v2-validated`.

### Stage H exit criteria

| # | Criterion | Verification method |
|---|---|---|
| H-X1 | Every change was made within the Step G4 authorised scope | Transformation log cross-check against the authorisation |
| H-X2 | The documented quick-start now succeeds | `EVD-H-02` vs `EVD-C-02` |
| H-X3 | Zero secret-shaped literals in the working tree; history disposition and rotation plan recorded | `EVD-H-03`; `secrets-hardening.md` |
| H-X4 | `/ai/summarize` is authorised; `clinician` is gone; policy is enforced in the request path, with negative tests | `EVD-H-04`; code review of the request path |
| H-X5 | A missing record returns 404; lookup is on the declared business key; `REC-0001` ambiguity is resolved | `EVD-H-05`; test results |
| H-X6 | ETL quarantines defects, exits non-zero past threshold, and emits a per-run report | `EVD-H-06` |
| H-X7 | No untrusted field reaches the prompt outside `ai-context-policy.yaml`; output is schema-validated; `guardrail_status` is evaluated, not literal | `EVD-H-07`; code review |
| H-X8 | A sample business event traces end to end with actor, correlation ID, policy decision, model version and approval populated | `EVD-H-08` |
| H-X9 | The OpenAPI contract covers every route and contract tests fail on drift | Route-coverage check |
| H-X10 | `make smoke` passes with the extended assertions, and the original assertions are preserved | `EVD-H-09` |
| H-X11 | **Every** behaviour difference is classified approved-change or regression; zero unexplained | `EVD-H-10` |
| H-X12 | Remaining debt is registered with an owner and a date | `remaining-debt-register.md` |

---

# STAGE I — Implementation PRD & Delivery Planning

**Spine stages:** 17, 18.

### Step I1 — Finalise the Implementation PRD

**Action.** Reconcile the E3 Initial PRD with repository findings, architecture decisions and
transformation evidence. Update capabilities, priorities, scope, dependencies, NFRs,
acceptance criteria and release boundaries. Record **every** material change and invalidated
assumption. **Do not copy the Initial PRD unchanged.**
**Inputs.** E3; F1 ADRs; H10 behaviour differences; H11 remaining debt.
**Depends on.** **H10, H11** — the PRD must reflect what the transformation actually proved
possible, including what it proved impossible.
**Why.** This becomes the implementation baseline against which Stages J–N are judged; Stage R
reconciles it into the Final As-Built PRD.
**Outputs** (`docs/17-implementation-prd/`): `implementation-prd.md`, `prd-change-log.md`,
`prioritized-capabilities.md`, `finalized-nfrs.md`, `release-boundaries.md`,
`finalized-acceptance-criteria.md`, `invalidated-assumptions.md`,
`implementation-baseline-signoff.md`. **Rubric.** 4.

### Step I2 — Produce the evidence-driven delivery plan

**Action.** Translate the PRD and specs into increments with stories, dependencies, owners,
tests, evaluation datasets, acceptance conditions, Definition of Done and evidence
requirements. **No work item is complete without its required evidence.**
**Inputs.** I1; F4 traceability; G3 gates.
**Depends on.** **I1** (scope), **F4** (every item must inherit its traceability row).
**Why.** Rubric criterion 4 scores execution quality; a Definition of Done that includes an
evidence artifact is what prevents a Stage R evidence gap discovered too late to fill.
**Outputs** (`docs/18-delivery/`): `delivery-backlog.md`, `increment-plan.md`,
`ownership-map.md`, `definition-of-done.md`, `acceptance-test-plan.md`,
`evaluation-rubric.md`, `evidence-checklist.md`, `delivery-dependencies.md`,
`delivery-risk-register.md`. **Rubric.** 4.

### Step I3 — Stage I gate review

### Stage I exit criteria

| # | Criterion | Verification |
|---|---|---|
| I-X1 | The Implementation PRD differs materially from the Initial PRD and the change log explains why | `prd-change-log.md` |
| I-X2 | Every invalidated assumption is recorded with the evidence that invalidated it | `invalidated-assumptions.md` |
| I-X3 | Every backlog item has an owner, a test and a named evidence artifact | `delivery-backlog.md` column completeness |
| I-X4 | The Definition of Done requires evidence, not just a passing test | `definition-of-done.md` |

---

# STAGE J — Intelligence Core, Application, Integration & Agents

**Spine stages:** 19, 20, 21, 22.

### Step J1 — Build the prompt, model and structured-output layer

**Action.** Implement version-controlled prompts, model configuration, structured outputs,
extraction, and retrieval/grounding where justified. Store executable prompts and configuration
in version-controlled implementation directories as well as documenting them.
**Inputs.** H7 gateway; D4 AI context policy; E1 qualification; F3 schemas; OQ-02 model decision.
**Depends on.** **H7** (the safe gateway is the substrate), **E1** (build only justified AI),
**OQ-02** (a real model must be selected — this is blocking).
**Why.** **F-27** (no provenance, no registry) makes any AI quality claim unreproducible. The
registry is also the input to the Stage Q model-portability comparison.
**Outputs** (`docs/19-intelligence/`): `prompt-registry.md`, `model-configuration.md`,
`extraction-pipeline.md`, `retrieval-pipeline.md`, `rag-design.md`. **Rubric.** 2, 4.

### Step J2 — Build evaluation datasets before any tuning

**Action.** Build golden, edge, adversarial and failure datasets from the synthetic corpus,
including the seeded prompt-injection payloads that `data/README.md` declares. Specify
expected outputs and abstention cases.
**Inputs.** `data/synthetic/*`; D3 business rules; `security/threat-model.md`; C5 defect catalogue.
**Depends on.** **D3** (expected behaviour must be defined before it can be scored),
**C5** (the defect catalogue supplies the edge cases).
**Why.** Spine 19 is explicit: *build evaluation datasets before tuning*. Datasets built after
tuning measure the tuning, not the capability. These datasets are reused unchanged in Stage L
TEVV and in Stage Q, which is what makes the two-model comparison a fair test.
**Outputs.** `docs/19-intelligence/evaluation-dataset-spec.md`; versioned dataset files.
→ `evidence/19-intelligence/` **Rubric.** 3, 4.

### Step J3 — Benchmark, evaluate and gate the intelligence layer

**Action.** Measure retrieval relevance, groundedness, answer quality, hallucination and
unsupported claims, abstention, latency and cost. Benchmark candidate models. Compare against
the E2 cost and latency envelope. Issue the intelligence release gate.
**Inputs.** J1, J2; E2 envelope; F3 acceptance criteria.
**Depends on.** **J2** (datasets must predate evaluation), **E2** (the thresholds).
**Why.** **F-29** means there is no prior quality evidence of any kind; this is the first
defensible measurement. The benchmark also produces the Model A / Model B evidence Stage Q
needs.
**Outputs** (`docs/19-intelligence/`): `model-benchmark.md`, `rag-evaluation-results.md`,
`prompt-evaluation-results.md`, `grounding-results.md`, `quality-latency-cost-results.md`,
`intelligence-release-gate.md`. **Rubric.** 2, 4.

### Step J4 — Engineer the application and services

**Action.** Implement UI, APIs, business logic, persistence and services per spec, keeping
deterministic logic separate from probabilistic behaviour. Implement validation, errors,
authN/authZ, idempotency, accessibility, auditability and observability hooks. Resolve
**OQ-06**: either build the operator portal properly or formally descope it and replace the
vacuous Playwright test (**F-05**, **F-52**).
**Inputs.** I1 PRD; F3 specs; H4, H5, H8 implementations; OQ-06 ruling.
**Depends on.** **H4, H5, H8** (the application builds on the corrected identity, record and
audit layers), **I1** (scope).
**Why.** Rubric criterion 4 (25 marks) requires a working end-to-end workflow. **F-05** and
**F-52** mean the current frontend evidence is a test that passes against nothing — the single
largest threat to that criterion.
**Outputs** (`docs/20-application/`): `application-component-map.md`,
`api-implementation-map.md`, `state-model.md`, `business-logic-map.md`,
`deterministic-ai-boundary.md`, `error-handling-implementation.md`,
`access-control-implementation.md`, `application-test-summary.md`, `application-readiness.md`.
**Addresses.** F-05, F-52. **Rubric.** 4.

### Step J5 — Complete enterprise integration

**Action.** Integrate systems of record, legacy applications, APIs, databases and events.
Validate authentication, authorisation, schemas, contracts, retries, idempotency,
reconciliation, timeouts, stale data, duplicates and dependency failures. Implement the carrier
booking saga with compensation and duplicate suppression (**F-38**) and a retry policy with a
ceiling (**F-39**).
**Inputs.** F3 integration specs; D3 saga rules; C5 duplicate/orphan findings; H6 ETL.
**Depends on.** **D3** (saga semantics), **H6** (quarantine behaviour must exist before
reconciliation can rely on it).
**Why.** The data already shows a retry storm (`retry_count` to 4,995) and three duplicate
bookings. Integration that does not address these ships the defect.
**Outputs** (`docs/21-integration/`): `integration-inventory.md`, `api-contracts.md`,
`data-contracts.md`, `event-contracts.md`, `adapter-map.md`, `authentication-map.md`,
`failure-semantics.md`, `reconciliation-rules.md`, `integration-test-results.md`,
`integration-readiness.md`. **Addresses.** F-38, F-39. **Rubric.** 2.

### Step J6 — Engineer agents, or document not-applicable

**Action.** **Only where Stage E justified agentic behaviour**, engineer the agent runtime:
planner roles, strict tool schemas, tool gateways, state, memory, context management, graph,
loop controls, termination criteria, token/time/tool budgets, retries, evaluator logic,
sandboxing, permissions and recovery. **If agentic AI was rejected at Stage E, create
`docs/22-agentic-engineering/not-applicable.md` with justification rather than inventing agent
artifacts.**
**Inputs.** E1 minimum-agency assessment; A6/E2 loop budget.
**Depends on.** **E1** — this is the clearest case in the spine where a stage may legitimately
produce a justified N/A, and inventing agent artifacts to fill a template is itself a finding.
**Why.** The delivered system has an `ai_agent` persona and an `ai_invocations` dataset but no
agent runtime. Whether to build one is a Stage E decision, and the runbook must not presume it.
**Outputs.** The full agent artifact set, or `not-applicable.md`. **Rubric.** 2, 3.

### Step J7 — Stage J gate review

### Stage J exit criteria

| # | Criterion | Verification |
|---|---|---|
| J-X1 | Prompts and model configuration are version-controlled with a registry and a version per prompt | `prompt-registry.md`; repository paths |
| J-X2 | Evaluation datasets were committed **before** the first evaluation run | Git history timestamps |
| J-X3 | Quality, latency and cost results exist and are compared against the E2 envelope | `quality-latency-cost-results.md` |
| J-X4 | An end-to-end business workflow executes against the running application | Demonstration recording + test results |
| J-X5 | OQ-06 is resolved; no test passes against a non-existent application | `application-test-summary.md`; Playwright suite review |
| J-X6 | Carrier saga duplicate suppression and a retry ceiling are implemented and tested | `integration-test-results.md` |
| J-X7 | Agent artifacts exist **or** a justified `not-applicable.md` exists — never invented | Directory check |

---

# STAGE K — Human Control, Security, Privacy, Responsible AI & Governance

**Spine stages:** 23, 24, 25.

### Step K1 — Define human control and autonomy boundaries

**Action.** Classify every material decision by autonomy level: deterministic, AI-recommends,
AI-executes-after-validation, requires-explicit-human-approval, never-delegated. Define HITL
and HOTL workflows, approval gates, override policy, confidence handling and escalation.
Reconcile with the A5 provisional controls.
**Inputs.** E1 minimum-agency assessment; H7 approval gate; D4 AI context policy; A5 contract.
**Depends on.** **E1** (agency decisions), **H7** (the enforcement mechanism must exist for the
matrix to be real rather than aspirational).
**Why.** **F-26**: the current "approval" is advisory prose in a payload. The autonomy matrix is
what turns it into an enforced state transition, and it is directly scored by rubric criterion 3.
**Outputs** (`docs/23-human-control/`): `autonomy-matrix.md`, `deterministic-control-rules.md`,
`hitl-workflow.md`, `hotl-workflow.md`, `approval-gates.md`, `human-override-policy.md`,
`confidence-handling.md`, `escalation-matrix.md`, `operating-contract-updates.md`,
`human-control-test-results.md`. **Addresses.** F-26, F-36. **Rubric.** 3.

### Step K2 — Threat-model the full attack surface

**Action.** Threat-model application, APIs, identity, data, prompts, retrieval, models, agents,
tools, context, supply chain and integrations. Map the six declared gaps
(`duplicate_tracking_events`, `stale_gps`, `timezone_mismatch`, `duplicate_carrier_booking`,
`route_ignores_restrictions`, `location_data_overexposure`) to STRIDE/MAESTRO as
`security/threat-model.md` instructs. Address prompt and indirect injection, data exfiltration,
insecure output handling, excessive agency, insecure tool use, poisoning, secrets exposure,
authorisation bypass and privacy.
**Inputs.** `security/threat-model.md`; `docs/architecture/known-gaps.md`; F1 security
architecture; H3–H8 implementations.
**Depends on.** **H4, H7, H8** — the model must describe the system as built; threat-modelling
the delivered system would model an architecture that no longer exists.
**Why.** The repository supplies the starter list and explicitly asks for the STRIDE/MAESTRO
mapping. Completing it is directly scored and is the input to Stage L red teaming.
**Outputs** (`docs/24-security-privacy/`): `threat-model.md`, `attack-surface-map.md`,
`security-control-matrix.md`, `privacy-impact-assessment.md`, `prompt-injection-controls.md`,
`agent-security-controls.md`, `data-protection-controls.md`, `responsible-ai-controls.md`,
`security-test-plan.md`, `security-test-results.md`, `residual-security-risks.md`,
`security-readiness.md`. **Addresses.** F-16, F-22, F-23. **Rubric.** 3.

### Step K3 — Implement and test security, privacy and RAI controls

**Action.** Implement the K2 controls within approved scope. Produce the privacy impact
assessment covering driver and vehicle location data (`location_data_overexposure`). Implement
field-level minimisation per `ai-context-policy.yaml`. Run the security test plan.
**Inputs.** K2; D4; F3 security spec.
**Depends on.** **K2** (controls follow threats).
**Why.** Challenge 13's acceptance standard: *security claims must be backed by repeatable
validation.* **Rubric.** 3.
**Outputs.** Implemented controls; `security-test-results.md`; `privacy-impact-assessment.md`.

### Step K4 — Establish governance, compliance and assurance

**Action.** Map applicable regulatory, contractual, organisational and AI-governance
obligations to controls, owners, evidence and approval points (**OQ-04**). Confirm or update
the A5 governance assumptions. Define accountability, AI system registration, change control,
risk acceptance, auditability and evidence retention (**OQ-10**). Produce the model card and
system card.
**Inputs.** B2 decision rights; K1–K3; A5 contract; OQ-04 ruling.
**Depends on.** **K1–K3** (obligations map to controls that exist), **B2** (accountability
needs named owners).
**Why.** **OQ-04** is unresolved in the delivered artifacts: the domain involves customs
agents, cross-border routes and personal location data, but no artifact names a regulatory
regime. Inventing one would be worse than recording it unresolved — but leaving it unaddressed
costs rubric criterion 3 directly.
**Outputs** (`docs/25-governance/`): `compliance-obligations.md`,
`compliance-control-matrix.md`, `governance-model.md`, `accountability-map.md`,
`ai-system-register.md`, `model-card.md`, `system-card.md`, `risk-acceptance-register.md`,
`evidence-retention-policy.md`, `audit-evidence-index.md`,
`operating-contract-governance-updates.md`, `governance-readiness.md`.
**Addresses.** OQ-04, OQ-05, OQ-10. **Rubric.** 3.

### Step K5 — Stage K gate review

### Stage K exit criteria

| # | Criterion | Verification |
|---|---|---|
| K-X1 | Every material decision appears in the autonomy matrix with an enforcement mechanism | `autonomy-matrix.md` enforcement column |
| K-X2 | Approval gates are enforced in code, not advisory text | Code review + `human-control-test-results.md` |
| K-X3 | All six declared brownfield gaps are mapped to STRIDE/MAESTRO with controls | `threat-model.md` |
| K-X4 | A PIA exists covering location data | `privacy-impact-assessment.md` |
| K-X5 | Security tests are repeatable and automated, not one-off | CI job present |
| K-X6 | Regulatory scope is either determined with an owner, or formally recorded as an accepted unresolved risk | `compliance-obligations.md`; `risk-acceptance-register.md` |
| K-X7 | Model card and system card exist and match the J1 configuration | Cross-check |

---

# STAGE L — TEVV & AI Red Teaming

**Spine stage:** 26.

### Step L1 — Write the TEVV plan with predeclared thresholds

**Action.** Define the TEVV plan and **predeclare objective release thresholds** for
functionality, model and RAG quality, groundedness, hallucination, abstention, security,
privacy, resilience and business outcomes.
**Inputs.** J2 datasets; J3 results; F3 acceptance criteria; E2 envelope.
**Depends on.** **J3** (current measured performance informs achievable thresholds), **F3**
(acceptance criteria are the source).
**Why.** The spine requires thresholds be *objective and predeclared where feasible*.
Thresholds set after results are observed are not thresholds. **Rubric.** 3, 4.
**Outputs** (`docs/26-tevv/`): `tevv-plan.md`, `golden-dataset-spec.md`, `edge-dataset-spec.md`,
`adversarial-dataset-spec.md`, `failure-dataset-spec.md`, `evaluation-metrics.md`,
`release-thresholds.md`.

### Step L2 — Execute TEVV

**Action.** Execute across deterministic and probabilistic behaviour using the J2 datasets
unchanged. Evaluate functionality, quality, groundedness, hallucination, abstention, agents
where applicable, security, privacy, resilience and business outcomes.
**Depends on.** **L1** (thresholds first), **J2** (datasets unchanged — modifying them here
invalidates both the gate and the Stage Q comparison).
**Outputs.** `docs/26-tevv/tevv-results.md`. **Evidence.** → `evidence/26-tevv/` **Rubric.** 3, 4.

### Step L3 — Red-team the system

**Action.** Red-team prompt injection (using the seeded payloads), data leakage, control
bypass, excessive agency and tool abuse. Attempt specifically to reproduce the pre-transformation
defects: unauthenticated AI invocation (**F-20**), role self-assertion (**F-17**), cross-entity
record confusion (**F-30**/**F-31**), and unguarded prompt interpolation (**F-22**).
**Depends on.** **K2** (the attack-surface map directs the campaign), **L2** (functional
baseline first).
**Why.** Attempting to reproduce the exact original defects produces the most persuasive
possible security evidence: a documented attack that worked against `baseline/v0.1-as-delivered-bytes`
and fails against `repo/v2-validated`. This is high-value material for rubric criterion 5.
**Outputs.** `docs/26-tevv/red-team-plan.md`, `red-team-findings.md`.
**Evidence.** Attack transcripts, before and after. → `evidence/26-tevv/EVD-L-03-*`
**Addresses.** F-17, F-20, F-22, F-30, F-31. **Rubric.** 3, 5.

### Step L4 — Remediate and gate

**Action.** Remediate findings, record residual TEVV risks, and issue the release gate against
the L1 predeclared thresholds.
**Outputs.** `docs/26-tevv/remediation-evidence.md`, `residual-tevv-risks.md`,
`tevv-release-gate.md`. **Rubric.** 3.

### Step L5 — Stage L gate review

### Stage L exit criteria

| # | Criterion | Verification |
|---|---|---|
| L-X1 | Release thresholds were committed **before** results were produced | Git history timestamps |
| L-X2 | TEVV ran against the unmodified J2 datasets | Dataset checksums match `evidence/19-intelligence/` |
| L-X3 | Red-team attempts include reproduction of F-17, F-20, F-22, F-30 against both baseline and transformed builds | `EVD-L-03` before/after transcripts |
| L-X4 | Every red-team finding is remediated or accepted with a named risk owner | `remediation-evidence.md`; `residual-tevv-risks.md` |
| L-X5 | The release gate decision cites measured values against predeclared thresholds | `tevv-release-gate.md` |

---

# STAGE M — Hardening, Resilience, Incident Response & BC/DR

**Spine stages:** 27, 28, 29.

### Step M1 — Harden and secure the supply chain

**Action.** Harden identity, RBAC, secrets, network and runtime, infrastructure, dependencies,
APIs, CI/CD, build artifacts and supply chain. **Generate an SBOM** and scan source,
dependencies, infrastructure and artifacts. Remove debug behaviour, test secrets, unnecessary
ports, excessive privileges and insecure defaults. Replace the stub Terraform with real IaC per
the OQ-01 platform decision (**F-48**).
**Inputs.** H1–H3; F1 deployment architecture; `supply-chain/dependency-risk-register.md`.
**Depends on.** **H3** (secrets), **F1/OQ-01** (IaC needs a target platform).
**Why.** **F-49**: the risk register names "no SBOM" and "no provenance" as targets with no
artifact behind them. This step produces them. **Rubric.** 2, 3.
**Outputs** (`docs/27-hardening/`): `hardening-plan.md`, `identity-rbac-hardening.md`,
`secrets-hardening.md`, `runtime-hardening.md`, `dependency-hardening.md`,
`supply-chain-controls.md`, `sbom-summary.md`, `vulnerability-register.md`, `scan-results.md`,
`vulnerability-disposition.md`, `production-readiness-checklist.md`.
**Evidence.** SBOM file; scan outputs; disposition per vulnerability.
→ `evidence/27-hardening/` **Addresses.** F-13, F-15, F-48, F-49.

### Step M2 — Design and implement resilience

**Action.** Define and implement timeouts, retries with backoff, circuit breakers, bulkheads,
fallback models and providers, caching, capacity limits, graceful degradation and
**AI-disabled operation**. Prevent retry storms (**F-39**) and cascading failure.
**Inputs.** C5 retry findings; J5 integration; F3 NFRs; K1 autonomy matrix.
**Depends on.** **J5** (the integration layer is where the policies attach), **K1** (degraded
mode must respect the autonomy boundaries — what the system may still do without AI is a human-
control decision, not purely a technical one).
**Why.** Challenge 11's acceptance standard: *the system must define what continues safely when
dependencies fail.* The data already evidences a retry storm. **Rubric.** 2.
**Outputs** (`docs/28-resilience/`): `resilience-architecture.md`, `failure-mode-analysis.md`,
`timeout-retry-policy.md`, `circuit-breaker-policy.md`, `fallback-matrix.md`, `capacity-plan.md`,
`graceful-degradation-design.md`, `ai-disabled-mode.md`.

### Step M3 — Execute failure injection

**Action.** Execute the five drills already specified in
`docs/runbooks/failure-injection-drills.md`: missing correlation IDs in event streams; AI
gateway timeout and core-workflow degradation; duplicate event replay against idempotency;
stale master data traced downstream; forced legacy batch partial failure with audit-evidence
comparison. Record results and recovery evidence.
**Inputs.** `docs/runbooks/failure-injection-drills.md`; M2 implementation; H8 correlation.
**Depends on.** **M2** (controls must exist to be tested), **H8** (the correlation-ID drill is
only meaningful once correlation exists — pre-transformation it would merely re-measure F-42).
**Why.** The repository supplies five well-chosen drills; executing exactly those gives direct,
traceable coverage of Challenge 11 and tests the specific declared failure modes.
**Outputs.** `docs/28-resilience/failure-injection-plan.md`, `failure-injection-results.md`,
`resilience-readiness.md`. **Evidence.** → `evidence/28-resilience/EVD-M-03-drills/`
**Addresses.** F-39, F-41, F-42. **Rubric.** 2, 3.

### Step M4 — Build the incident playbook and BC/DR, and run a tabletop

**Action.** Replace the self-declared incomplete incident runbook (**F-56**) with a severity
model, triage, containment, evidence preservation, communications, recovery, RTO/RPO and
failover. Cover AI-specific incidents: prompt injection, unsafe action, compromised tool, data
leakage, bad retrieval, model/provider failure, cost runaway. **Run a tabletop or simulation.**
**Inputs.** `docs/runbooks/incident-response.md`; K2 threat model; M3 drill results.
**Depends on.** **M3** (real failure data makes the playbook concrete), **K2** (AI incident
classes come from the threat model).
**Why.** **F-56**: the delivered runbook explicitly asks for exactly this content. **Rubric.** 3.
**Outputs** (`docs/29-incident-bcdr/`): `ai-incident-playbook.md`, `incident-severity-matrix.md`,
`containment-procedures.md`, `forensics-evidence-policy.md`, `communications-plan.md`,
`bc-plan.md`, `dr-plan.md`, `rto-rpo.md`, `failover-procedure.md`, `recovery-procedure.md`,
`tabletop-scenario.md`, `tabletop-results.md`, `incident-readiness.md`.

### Step M5 — Stage M gate review

### Stage M exit criteria

| # | Criterion | Verification |
|---|---|---|
| M-X1 | An SBOM exists and every vulnerability has a disposition | `sbom-summary.md`; `vulnerability-disposition.md` |
| M-X2 | IaC provisions real infrastructure and emits no credential artifact | `main.tf` review; plan output |
| M-X3 | Retry ceilings and circuit breakers are implemented and tested | `timeout-retry-policy.md`; test results |
| M-X4 | AI-disabled mode is specified and demonstrated | `ai-disabled-mode.md`; drill evidence |
| M-X5 | All five declared drills executed with recorded results | `EVD-M-03-drills/` contains five result sets |
| M-X6 | The incident runbook is complete and a tabletop has been run with results | `tabletop-results.md` |

---

# STAGE N — Release, Observability, FinOps & Vendor Risk

**Spine stages:** 30, 31, 32, 33.

### Step N1 — Implement observability and define SLOs

**Action.** Instrument application, infrastructure, data, retrieval, models and agents. Capture
privacy-safe logs, metrics and traces for requests, retrieval, prompt and config versions,
model latency, tokens, tool calls, errors and business outcomes — exactly the target list in
`observability/otel-notes.md`. Define SLOs, SLAs, alerts and error budgets. Build dashboards and
alerts as code.
**Inputs.** `observability/otel-notes.md`; F3 observability spec; H8 correlation; C1 KPIs.
**Depends on.** **H8** (correlation must exist before traces mean anything), **C1** (SLOs
should align to the frozen KPI definitions).
**Why.** **F-46**: no tracing, metrics, SLOs, dashboards or alerts exist today, and `/health`
is a static literal. **Rubric.** 3.
**Outputs** (`docs/31-observability/`): `observability-architecture.md`, `logging-spec.md`,
`metrics-spec.md`, `tracing-spec.md`, `ai-telemetry-spec.md`, `agent-telemetry-spec.md`,
`dashboard-catalog.md`, `alert-catalog.md`, `slo-sla-definitions.md`, `error-budget-policy.md`,
`operational-runbook.md`, `observability-validation.md`.

### Step N2 — Demonstrate end-to-end incident reconstruction

**Action.** Select one business event and reconstruct it completely: actor → request → policy
decision → data accessed → model and prompt version → recommendation → human approval → final
action → audit record → trace ID. Produce the **before/after** comparison showing what could
not be reconstructed on `baseline/v0.1-as-delivered-bytes` and what can now.
**Inputs.** N1 instrumentation; H8 audit; C5 correlation baseline (32.8% null, 983 of 3,000).
**Depends on.** **N1** (traces), **H8** (audit schema), **C5** (the before-state measurement).
**Why.** This is simultaneously the Challenge 8 acceptance standard (*explain one business
event end to end*) and the Challenge 14 acceptance standard (*show what happened, who
influenced it, and what cannot yet be proven*). It is the single most persuasive artifact for
rubric criterion 3 and the natural centrepiece of the Stage Q demo.
**Outputs.** `docs/25-governance/audit-evidence-index.md`;
`docs/31-observability/incident-reconstruction-example.md`.
**Evidence.** Full reconstruction, before and after.
→ `evidence/31-observability/EVD-N-02-reconstruction.json`
**Addresses.** F-42, F-43, F-44, F-46. **Rubric.** 3, 5.

### Step N3 — Plan and execute the release

**Action.** Define environment promotion, approvals, deployment method, feature flags,
canary/phased release, migration, validation, monitoring, go/no-go criteria and rollback
triggers. **Verify backup and rollback before cutover.**
**Inputs.** G2 feature flags; G3 cutover/rollback; M1 hardening; L4 release gate.
**Depends on.** **L4** (do not release through an unpassed quality gate), **M1** (do not release
unhardened).
**Outputs** (`docs/30-release/`): `release-plan.md`, `environment-promotion-plan.md`,
`deployment-strategy.md`, `feature-flag-plan.md`, `cutover-checklist.md`,
`go-no-go-criteria.md`, `rollback-plan.md`, `backup-validation.md`, `release-approvals.md`,
`deployment-evidence.md`, `release-outcome.md`. **Rubric.** 2.

### Step N4 — Measure actual economics

**Action.** Measure actual input/output/context/retrieval/tool tokens, model calls, cache hits,
retries, latency, throughput, infrastructure cost and human-oversight cost. Calculate unit
economics **per request, per case, per workflow and per business outcome**. Identify token and
value leakage. Optimise without violating the L1 quality thresholds.
**Inputs.** A6/E2 envelope; N1 telemetry; C1 KPI baseline; L1 thresholds.
**Depends on.** **N1** (measurement requires instrumentation — **F-28** means no real token
data exists before this), **E2** (the baseline to compare against), **L1** (optimisation must
not breach quality gates).
**Why.** Challenge 12's acceptance standard: *cost must be explained per business outcome, not
only as total spend.* **Rubric.** 2.
**Outputs** (`docs/32-finops/`): `production-token-dashboard-spec.md`,
`baseline-vs-actual-token-analysis.md`, `model-usage-analysis.md`, `cache-effectiveness.md`,
`cost-per-request.md`, `cost-per-case.md`, `cost-per-workflow.md`, `cost-per-outcome.md`,
`token-leakage-analysis.md`, `optimization-backlog.md`, `finops-model.md`, `tco-model.md`,
`cost-guardrails.md`. **Addresses.** F-28, F-57.

### Step N5 — Assess vendor and concentration risk

**Action.** Assess model, platform, infrastructure, data and service providers for
availability, contractual terms, security and privacy, data usage, regulatory constraints,
price risk, portability, concentration, lock-in, substitution and exit feasibility.
**Inputs.** OQ-01 platform; OQ-02 model; M1 SBOM.
**Depends on.** **OQ-01, OQ-02** — before those are resolved there are no vendors; the
delivered system has none, since `local-sim-v1` is an in-process simulator.
**Why.** Stage Q's two-model comparison is itself portability evidence and should be cited here.
**Outputs** (`docs/33-vendor-risk/`): `vendor-inventory.md`, `vendor-scorecards.md`,
`third-party-risk-assessment.md`, `data-processing-dependencies.md`,
`concentration-risk-analysis.md`, `lock-in-analysis.md`, `portability-assessment.md`,
`substitution-strategy.md`, `exit-plan.md`, `vendor-risk-acceptance.md`. **Rubric.** 3.

### Step N6 — Stage N gate review

### Stage N exit criteria

| # | Criterion | Verification |
|---|---|---|
| N-X1 | Traces, metrics and logs are emitted with correlation IDs; dashboards and alerts exist as code | `observability-validation.md`; repository paths |
| N-X2 | SLOs are defined with error budgets and owners | `slo-sla-definitions.md` |
| N-X3 | One business event is reconstructed end to end, with the before-state gap documented | `EVD-N-02` |
| N-X4 | Backup and rollback were verified **before** cutover | `backup-validation.md` timestamp precedes `deployment-evidence.md` |
| N-X5 | Cost is reported per business outcome, not only as total spend | `cost-per-outcome.md` |
| N-X6 | Actual economics are compared against the A6/E2 envelope with variance explained | `baseline-vs-actual-token-analysis.md` |
| N-X7 | An exit plan exists for every critical vendor | `exit-plan.md` |

---

# STAGE O — Outcome Measurement, Value Leakage & Benefits

**Spine stages:** 34, 35, 36.

### Step O1 — Measure after-intervention KPIs

**Action.** Measure using the **frozen Stage C1 definitions**, unchanged. Include successes,
failures, exceptions, overrides and adoption. Confirm measurement-window and population
comparability before making any claim.
**Depends on.** **C1** (frozen definitions — the spine explicitly forbids changing KPI
definitions to improve results), **N1** (instrumentation produces the data).
**Outputs** (`docs/34-after-kpis/`): `after-intervention-kpi-sheet.md`,
`production-performance-report.md`, `adoption-metrics.md`, `exception-metrics.md`,
`human-override-metrics.md`, `measurement-data-quality.md`, `kpi-comparability-check.md`.
**Rubric.** 1, 4.

### Step O2 — Analyse variance and value leakage

**Action.** Compare C1 and O1 using the frozen definitions and comparable populations. Quantify
improvement, deterioration and deviation. Identify leakage from low adoption, overrides, errors,
rework, latency, control friction, AI or infrastructure cost, or workflow displacement.
**Avoid attributing all change to the intervention where confounders exist** — and note that
because the KPI baseline rests on proxies (**F-57**), confounder analysis is unusually important
here and its limits must be stated.
**Depends on.** **O1**, **C1**.
**Outputs** (`docs/35-value-leakage/`): `before-after-analysis.md`, `kpi-variance-table.md`,
`benefit-variance.md`, `value-leakage-analysis.md`, `confounder-analysis.md`,
`causal-findings.md`, `adoption-leakage.md`, `cost-leakage.md`, `corrective-action-backlog.md`.
**Rubric.** 1.

### Step O3 — Model benefits, ROI and NPV

**Action.** Translate **only verified** improvements into financial value. Include adoption,
productivity, quality, risk, revenue and cost effects, model/token/infrastructure costs and
human oversight. Avoid double-counting. Test optimistic, expected and downside scenarios.
**Depends on.** **O2** (only verified improvements qualify), **N4** (actual cost side).
**Why.** **OQ-09**: no financial data exists in the delivered artifacts, so every monetary
figure is an assumption. The sensitivity and double-counting analyses are what keep this
defensible; presenting a single ROI number would not be.
**Outputs** (`docs/36-benefits/`): `benefit-assumptions.md`, `verified-benefits.md`,
`cost-model.md`, `roi-model.md`, `npv-model.md`, `payback-analysis.md`, `scenario-analysis.md`,
`sensitivity-analysis.md`, `double-counting-check.md`, `benefits-realisation-dashboard-spec.md`,
`benefits-signoff.md`. **Rubric.** 4.

### Step O4 — Stage O gate review

### Stage O exit criteria

| # | Criterion | Verification |
|---|---|---|
| O-X1 | KPI definitions are byte-identical to the C1 frozen set | Automated diff |
| O-X2 | Comparability of measurement window and population is confirmed before any claim | `kpi-comparability-check.md` |
| O-X3 | Confounders are analysed and improvement is not wholly attributed to the intervention | `confounder-analysis.md` |
| O-X4 | Every monetary figure traces to a stated assumption or a verified measurement | `benefit-assumptions.md`; `verified-benefits.md` |
| O-X5 | A downside scenario is modelled, not only optimistic and expected | `scenario-analysis.md` |

---

# STAGE P — Operating Model, Handover, Drift, Scale & Retirement

**Spine stages:** 37, 38, 39, 40, 41.

### Step P1 — Define the target operating model and RACI
Convert the A5 engagement contract into steady-state ownership for application, data, models,
prompts, retrieval, agents, security, incidents, observability, costs, vendors, governance and
business outcomes. Define support tiers, change approval, service ownership, escalation and
decision rights. **Depends on** B2 (named owners) and K4 (accountability map).
**Outputs** (`docs/37-operating-model/`): `target-operating-model.md`, `raci.md`,
`service-ownership-map.md`, `model-ownership.md`, `data-ownership.md`,
`agent-tool-ownership.md`, `security-ownership.md`, `finops-ownership.md`, `support-model.md`,
`change-governance.md`, `decision-rights.md`, `escalation-model.md`,
`operating-contract-closure.md`. **Rubric.** 3.

### Step P2 — Hand over with operator exercises
Transfer architecture, code, configuration, prompts, model settings, data pipelines,
operational procedures, security, governance and runbooks. **Confirm by practical exercise**
that the receiving team can deploy, observe, diagnose, roll back and recover independently.
**Depends on** M4 (runbooks), N1 (observability), P1 (owners). **Why:** a handover asserted but
not demonstrated is the most common post-engagement failure, and the exercise results are
evidence.
**Outputs** (`docs/38-handover/`): `handover-index.md`, `knowledge-transfer-plan.md`,
`architecture-handover.md`, `engineering-handover.md`, `ai-rag-agent-handover.md`,
`security-handover.md`, `operations-handover.md`, `operator-exercises.md`,
`operator-exercise-results.md`, `open-handover-items.md`, `handover-acceptance-signoff.md`.
**Rubric.** 3, 5.

### Step P3 — Establish drift and continuous evaluation
Define continuous evaluation across data, knowledge, retrieval, prompts, models, agents,
application quality, adoption, reliability, latency and cost. Define thresholds triggering
investigation or controlled change. **Do not permit untracked prompt or model changes in
production.** **Depends on** J1 (registry), L1 (thresholds), N1 (telemetry).
**Outputs** (`docs/39-continuous-improvement/`): `drift-framework.md`, `data-drift-metrics.md`,
`knowledge-drift-metrics.md`, `retrieval-drift-metrics.md`, `prompt-model-drift-metrics.md`,
`agent-drift-metrics.md`, `evaluation-cadence.md`, `change-trigger-thresholds.md`,
`continuous-evaluation-plan.md`, `controlled-change-process.md`, `improvement-backlog.md`.
**Rubric.** 3.

### Step P4 — Define scale and the 90-day roadmap
Identify **only** capabilities, components, prompts, controls, contracts, evaluation assets and
patterns with demonstrated evidence for reuse. Assess adjacent use cases. **Prevent copying
first-use-case assumptions or debt.** **Depends on** O2 (evidence of what worked), H11 (the
remaining-debt register names what must not be propagated).
**Outputs** (`docs/40-scale/`): `reusable-components.md`, `pattern-catalog.md`,
`accelerator-pack.md`, `adjacent-use-case-inventory.md`, `reuse-readiness-assessment.md`,
`scale-risk-assessment.md`, `scale-out-backlog.md`, `90-day-roadmap.md`, `scale-governance.md`.
**Rubric.** 2.

### Step P5 — Define retirement criteria
Define safe retirement for models, prompts, indexes, APIs, agents, applications, databases,
infrastructure and vendors — including the legacy paths retired under G2. Address retention,
legal hold, archival, dependency removal, access and key revocation, migration, contracts and
audit evidence. **Depends on** G2 (coexistence retirement triggers), K4 (retention policy).
**Outputs** (`docs/41-retirement/`): `retirement-criteria.md`, `dependency-clearance.md`,
`data-retention-plan.md`, `archive-plan.md`, `legal-hold-check.md`, `access-revocation-plan.md`,
`secret-key-revocation.md`, `vendor-termination-plan.md`, `decommission-checklist.md`,
`retirement-evidence.md`. **Rubric.** 3.

### Step P6 — Stage P gate review

### Stage P exit criteria

| # | Criterion | Verification |
|---|---|---|
| P-X1 | Every asset in the RACI has a named owner, or an explicitly accepted unresolved gap | `raci.md` |
| P-X2 | The receiving team demonstrated deploy, observe, diagnose, rollback and recover | `operator-exercise-results.md` |
| P-X3 | Untracked prompt or model change in production is technically prevented, not merely prohibited | `controlled-change-process.md` + enforcement mechanism |
| P-X4 | Reusable assets carry evidence of fitness; none inherits registered debt | `reuse-readiness-assessment.md` vs `remaining-debt-register.md` |
| P-X5 | Key and secret revocation covers every credential found in Step H3, including in history | `secret-key-revocation.md` |

---

# STAGE Q — Model Portability Validation & Demonstration

**Source of requirement:** Challenge Guide page 6.

### Step Q1 — Regenerate the application from the semantic layer using a second model

**Action.** Using **only** the `semantic-layer/` artifacts, the Implementation PRD and the
Stage F specs — and **not** the Model A implementation — regenerate the application (or the
agreed representative subset) with a second model (**OQ-02**). Record the generation prompts,
the model and version, and the full output.
**Inputs.** D1–D5 semantic layer; I1 PRD; F3 specs; J1 prompt registry.
**Depends on.** **D6** (the layer must have passed its gate and must contain no
model-specific content, or the comparison tests the layer's bias rather than the models),
**I1, F3** (the specification inputs).
**Why.** This is the explicit Challenge Guide requirement *Test Semantic Layer with new model*.
It is also the strongest available evidence for the Stage N5 portability assessment and for
lock-in risk: a semantic layer that reproduces the system under a different model is a
demonstrated abstraction, not a claimed one.
**Outputs.** `docs/40-scale/semantic-layer-portability-test.md`; the Model B build.
**Evidence.** Generation transcripts; the Model B artifact. → `evidence/40-scale/EVD-Q-01-*`
**Rubric.** 2, 4.

### Step Q2 — Compare and contrast both applications

**Action.** Compare Model A and Model B builds across functional completeness, specification
conformance, semantic-layer fidelity, code quality, security control implementation, test pass
rate against the **unchanged J2/L1 datasets and thresholds**, latency, token cost and
divergence from the Implementation PRD. State which differences are model-attributable and
which reveal ambiguity in the semantic layer or the specs — and feed the latter back as
corrective actions.
**Depends on.** **Q1**, **L2** (both builds must be evaluated against identical predeclared
thresholds, or the comparison is not a measurement).
**Why.** The comparison's most valuable output is not which model won: it is the list of
specification ambiguities that only became visible when a second model interpreted them.
**Outputs.** `docs/40-scale/model-comparison.md`; `docs/39-continuous-improvement/` corrective
actions. **Evidence.** Side-by-side scorecard. → `evidence/40-scale/EVD-Q-02-comparison.csv`
**Rubric.** 2, 4, 5.

### Step Q3 — Prepare and rehearse the demonstration

**Action.** Build the demo script around the strongest evidence rather than around features:
(1) the Step C2 quick-start failing on the as-delivered baseline, then succeeding; (2) the
Step L3 red-team attack succeeding against `baseline/v0.1-as-delivered-bytes` and failing against
`repo/v2-validated`; (3) the Step N2 end-to-end reconstruction, before and after;
(4) the Step M3 AI-disabled degraded-mode drill; (5) the Step Q2 model comparison;
(6) the Step N4 cost-per-outcome figure. Rehearse. Prepare answers for the predictable
challenges: *what did you not fix and why*; *what can you still not prove*; *what would you do
with another two weeks*. Resolve **OQ-16** (demo environment) and **OQ-17** (time budget).
**Depends on.** **C2, L3, N2, M3, Q2, N4** — each is a demo beat and must exist first.
**Why.** Rubric criterion 5 (10 marks) scores clarity of storytelling, demo quality and the
ability to explain trade-offs and limitations. Limitations stated voluntarily score better than
limitations discovered by an evaluator.
**Outputs.** `docs/42-executive/demo-day-script.md`; `elevator-pitch.md`.
**Evidence.** Recorded rehearsal. → `evidence/42-executive/EVD-Q-03-demo-rehearsal`
**Rubric.** 5.

### Step Q4 — Stage Q gate review

### Stage Q exit criteria

| # | Criterion | Verification |
|---|---|---|
| Q-X1 | The Model B build was produced from the semantic layer and specs only, without reference to the Model A implementation | Generation transcripts |
| Q-X2 | Both builds were evaluated against identical unchanged datasets and predeclared thresholds | Dataset checksums; threshold file SHA |
| Q-X3 | Differences are classified model-attributable or specification-ambiguity | `model-comparison.md` |
| Q-X4 | Specification ambiguities revealed by the comparison are logged as corrective actions | `improvement-backlog.md` |
| Q-X5 | The demo has been rehearsed end to end within the agreed time budget | Rehearsal recording |

---

# STAGE R — Executive Defence, Final As-Built PRD & Production Evidence Pack

**Spine stages:** 42, FINAL; Challenge Guide challenges 15 and 16.

### Step R1 — Make the production readiness decision

**Action.** Evaluate readiness on tests, controls, evidence, open risks, ownership and
operational maturity. Produce the readiness checklist, residual risk register, risk-owner table
and deferred-work list. Issue an explicit **go / no-go**. State plainly what is ready, what is
not, and what risk is accepted and by whom.
**Inputs.** All stage gates; H11 remaining debt; L4 residual TEVV risks; K2 residual security
risks; M5, N6, O4, P6, Q4.
**Depends on.** All preceding gates — a readiness decision that is not an aggregation of gate
outcomes is an opinion.
**Why.** Challenge 15's acceptance standard is exactly this tripartite statement. A
`CONDITIONAL GO` with named accepted risks will score better than an unqualified `GO` that a
reviewer can falsify from the evidence pack.
**Outputs.** `docs/42-executive/production-readiness-decision.md`;
`docs/42-executive/residual-risks.md`; risk-owner table. **Rubric.** 1, 3, 5.

### Step R2 — Assemble the Production Evidence Pack

**Action.** Populate **the delivered `PRODUCTION_EVIDENCE_PACK_TEMPLATE.md`** — all fifteen
sections — from the `evidence/` tree. Every section cites specific evidence files by path and
SHA-256. Verify every `MANIFEST.md` is complete and every hash resolves.
**Inputs.** `PRODUCTION_EVIDENCE_PACK_TEMPLATE.md`; the complete `evidence/` tree; F4
traceability.
**Depends on.** **R1** (the pack carries the readiness decision), **F4** (the traceability
matrices are the pack's index), and every evidence-producing step.
**Why.** Challenge 16's acceptance standard: *a reviewer can verify the transformation without
relying on verbal explanation.* Using the repository's own template rather than a new structure
demonstrates that the delivered artifacts were read and honoured.
**Outputs.** `docs/42-executive/production-evidence-pack.md` (completed from the template).
**Evidence.** Hash-verified manifest covering the whole tree.
→ `evidence/EVIDENCE-INDEX.md` **Rubric.** 1, 3, 5.

### Step R3 — Write the executive defence

**Action.** Produce the evidence-backed executive narrative: original problem and baseline,
validated root causes, intervention choice, **why AI was or was not appropriate**, architecture
and ADRs, brownfield transformation, intelligence engineering, control framework, TEVV evidence,
production outcomes, economics, realised benefits, **failures**, trade-offs, remaining risks and
next steps. **Every material claim must map to lifecycle evidence.**
**Depends on.** **R1, R2** (the narrative is a reading of the pack, not a parallel account).
**Why.** Rubric criteria 1 and 5. Including failures is not modesty — it is what makes the
successes credible under questioning.
**Outputs** (`docs/42-executive/`): `executive-narrative.md`, `problem-to-value-story.md`,
`architecture-defence.md`, `ai-decision-defence.md`, `risk-control-summary.md`,
`tevv-summary.md`, `production-outcomes.md`, `economic-value-summary.md`, `lessons-learned.md`,
`residual-risks.md`, `next-step-recommendations.md`, `executive-evidence-index.md`.
**Rubric.** 1, 5.

### Step R4 — Produce the Final As-Built PRD

**Action.** Create the authoritative baseline of what was **actually delivered, validated,
released and accepted**. Reconcile the E3 Initial PRD, the I1 Implementation PRD, specs, ADRs,
implementation, configuration, TEVV evidence, data architecture, AI behaviour, integrations,
HITL boundaries, security and privacy controls, governance obligations, SLO commitments,
operating model, actual economics, production KPIs, benefits, residual risks and accepted
limitations. **Classify every original requirement as Delivered / Changed / Deferred / Rejected
/ Superseded with rationale and evidence. Do not copy earlier PRDs unchanged.**
**Depends on.** **E3, I1** (the two prior PRDs being reconciled), **R1–R3** (outcomes and
decisions), **F4** (traceability).
**Why.** This is the authoritative baseline for operations, audit, onboarding, support and
future change. The disposition matrix is also the cleanest possible answer to a CTO asking what
happened to any specific requirement.
**Outputs** (`docs/final-prd/`): `final-as-built-prd.md`, `requirement-disposition-matrix.md`,
`final-capability-map.md`, `as-built-architecture.md`, `final-api-interface-baseline.md`,
`final-data-knowledge-baseline.md`, `final-ai-agent-baseline.md`,
`final-security-governance-baseline.md`, `final-nfr-baseline.md`,
`final-acceptance-evidence-map.md`, `implemented-vs-deferred.md`, `known-limitations.md`,
`residual-risk-register.md`, `production-kpi-baseline.md`, `final-economics-baseline.md`,
`final-operating-boundaries.md`, `final-ownership-map.md`, `approved-roadmap.md`,
`final-product-baseline-signoff.md`. **Rubric.** 4.

### Step R5 — Final gate and submission

**Action.** Verify every stage gate is closed, every open question in Document 04 is resolved or
formally accepted with an owner, and every rubric criterion has mapped evidence per Document 03.
Tag the final state. Submit.
**Outputs.** `docs/42-executive/final-gate.md`; tag `release/v1-production-candidate`.

### Stage R exit criteria

| # | Criterion | Verification |
|---|---|---|
| R-X1 | The readiness decision states what is ready, what is not, and what risk is accepted and by whom | `production-readiness-decision.md` |
| R-X2 | All fifteen sections of the delivered evidence-pack template are populated with cited evidence | Section-by-section review |
| R-X3 | Every cited evidence file exists and its SHA-256 matches the manifest | Automated hash verification across `evidence/` |
| R-X4 | Every material claim in the executive narrative maps to a lifecycle evidence artifact | `executive-evidence-index.md`; reviewer sample |
| R-X5 | The narrative includes failures and trade-offs, not only successes | `lessons-learned.md` |
| R-X6 | Every original requirement is classified Delivered / Changed / Deferred / Rejected / Superseded with evidence | `requirement-disposition-matrix.md`; no unclassified rows |
| R-X7 | Every one of the 57 findings has a disposition: fixed (with evidence), deferred (with owner and date), or accepted (with approver) | `EVD-F-04` finding-coverage matrix, final revision |
| R-X8 | Every rubric criterion has mapped evidence, and criteria that cannot be satisfied are stated explicitly | Document 03 coverage matrix |
| R-X9 | Every Document 04 open question is resolved or formally accepted | Document 04, final revision |

---

## Appendix A — Stage dependency summary

```
A ─→ B ─→ C ─→ D ─→ E ─→ F ─→ G ─┬─→ H ─→ I ─→ J ─┬─→ K ─→ L ─→ M ─→ N ─→ O ─→ P ─┐
     (read-only through G)        │                │                                │
                        G4 authorisation gate      └─────────────→ Q ←──────────────┤
                        (first write permitted)         (needs D, I, F, J, L)       │
                                                                     └──→ R ←───────┘
```

**The three ordering constraints that must not be relaxed:**

1. **C8 before H** — characterization tests must pin current behaviour before any change,
   otherwise Step H10 cannot distinguish an approved behaviour change from a regression, and
   the Challenge 2 and 15 acceptance standards fail.
2. **H4 and H5 before H8** — identity and record-resolution must be correct before audit
   instrumentation, otherwise the system produces a complete, trustworthy-looking audit trail
   of the wrong actor acting on the wrong record.
3. **D before Q** — the semantic layer must be gated and model-neutral before the second-model
   regeneration, otherwise the comparison measures the layer's embedded bias rather than model
   portability.
