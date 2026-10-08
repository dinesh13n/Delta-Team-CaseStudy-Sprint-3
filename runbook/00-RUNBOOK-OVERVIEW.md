# Brownfield → Production-Grade Transformation Runbook

## Document 00 — Overview, Scope and Operating Contract

| Field | Value |
|---|---|
| **Stage** | Runbook preparation (pre-execution) |
| **Document** | 00 — Overview, Scope and Operating Contract |
| **Version** | v1.0 |
| **Date** | 2026-10-08 |
| **Author / Agent** | AI-FDE Transformation Team — Delta-Team |
| **Status** | Draft for CTO review |
| **Target system** | `07-logistics-shipment-fleet-routing-ops` (Logistics: Shipment, Fleet, Routing & Exception Operations) |
| **Evidence sources** | Delivered repository tree; `AI-FDE_Brownfield_Repo_Transformation_Challenge_Guide.pdf`; `AI_FDE_End-to-End_Production_Delivery_Spine.pdf`; `Prompt Template.pdf`; `Prompt_Anatomy.pdf`; `Semantic_Layer_capture.pdf`; `Evaluation Rubrics.jpeg`; read-only data profiling executed 2026-10-08 |
| **Audience** | CTO, Engineering Leadership, Security, SRE, Compliance |

---

## 1. Purpose of this package

This package is a **runbook, not an implementation**. It describes — step by step, in
execution order — how an engineer who was not part of this analysis can transform the
delivered brownfield repository into a production-grade repository, and how to capture
evidence that will survive engineering, security, SRE, compliance and executive review.

Per the task scope constraint, **no repository file has been created, modified, refactored
or executed as part of producing this runbook.** The only activity performed against the
repository was read-only inspection and read-only data profiling (scripts were written and
executed outside the repository tree; no output was written into the repository).

### What this package contains

| # | Document | Purpose |
|---|---|---|
| 00 | `00-RUNBOOK-OVERVIEW.md` | Scope, operating contract, evidence contract, directory conventions, roles, how to use the runbook (this document) |
| 01 | `01-BASELINE-ASSESSMENT.md` | The evidence-based as-is assessment that justifies every step in the runbook: 57 findings with file-level evidence, severity and rubric linkage |
| 02 | `02-TRANSFORMATION-RUNBOOK.md` | The runbook itself: 18 stages, 102 numbered steps, each with inputs, dependency rationale, outputs, evidence and storage location, plus per-stage exit criteria |
| 03 | `03-EVIDENCE-RUBRIC-TRACEABILITY.md` | Evidence index and bidirectional rubric coverage matrix; explicit list of rubric criteria the current artifacts **cannot yet satisfy** |
| 04 | `04-OPEN-QUESTIONS-REGISTER.md` | 23 open questions and blocking decisions that must be resolved by named owners, with the steps they block |

Each document is supplied in both Markdown (`.md`) and Microsoft Word (`.docx`) form.

---

## 2. Scope

### 2.1 In scope

- The delivered repository `07-logistics-shipment-fleet-routing-ops/` in its entirety:
  `apps/` (FastAPI services and the web scaffold), `etl/`, `legacy/`, `data/` (six CSV
  datasets and one JSONL event stream), `docs/`, `tests/`, `infra/`, `policy/`,
  `security/`, `supply-chain/`, `observability/`, `scripts/`, `api-examples/`,
  `.github/workflows/`.
- The transformation journey mandated by the Challenge Guide (16 core challenges).
- The artifact and directory spine mandated by the End-to-End Production Delivery Spine
  (stages 0A, 0B, 0C and 1–42, plus FINAL).
- The semantic layer extraction and dual-model comparison required by the Challenge Guide
  (page 6) and `Semantic_Layer_capture.pdf`.
- Evidence production sufficient to score against all five rubric criteria.

### 2.2 Out of scope for this document

- Executing any step. This runbook is the deliverable; Stage A Step A1 is the first action
  an executing engineer takes.
- Inventing stakeholders, owners, regulatory obligations, financial figures or target
  platforms that the delivered artifacts do not state. Where such information is required
  and absent, it is recorded in Document 04 as an open question, not assumed.

### 2.3 Scope constraint inherited by the executing team

The Delivery Spine declares that **discovery stages are read-only unless the prompt
explicitly authorises modification**. In this runbook, Stages A–G are read-only.
The first stage that modifies repository code is **Stage H**, and it must not begin until
the Stage G exit criteria — including an approved transformation backlog and an explicit
written authorisation from the repository owner — are met (see Open Question OQ-11).

---

## 3. Evidence contract

Every stage of this runbook inherits the **Global Workshop Execution Contract** from the
Delivery Spine:

> Analyse / Execute → Generate Required Artifacts → Save to Defined Repository Path →
> Cite Evidence → Record Assumptions & Unknowns → Validate Completion Gate → Proceed

### 3.1 Mandatory header block

Every artifact produced by any step **must** begin with this block. A step is not complete
if its artifact lacks it.

```markdown
| Field | Value |
|---|---|
| Stage | <spine stage number and name> |
| Runbook step | <e.g. C4> |
| Version | vX.Y |
| Date | YYYY-MM-DD |
| Author / Agent | <human name or agent id + model version> |
| Status | Draft | In Review | Approved | Superseded |
| Evidence sources | <repo paths, test ids, log files, scan outputs, approved stakeholder evidence> |
| Assumptions | <list, or "none"> |
| Unresolved issues | <list, or "none"> |
| Residual risks | <list, or "none"> |
```

### 3.2 Evidence classification

Every material statement in every artifact must be classified as one of:

- **Verified Fact** — directly observable in a repository file, a test result, a log, a
  scan output or approved stakeholder evidence, with the source cited.
- **Inference** — a conclusion drawn from one or more Verified Facts, with the reasoning
  stated.
- **Assumption** — a working position adopted to make progress, with the invalidation
  trigger stated.
- **Unknown** — information required but not available. Must be raised into the open
  questions register.

**Assumptions must never be presented as facts.** Where evidence is insufficient, record
`Unknown` rather than inventing an answer.

### 3.3 Evidence storage convention

Two parallel trees are used and both must be version-controlled:

| Tree | Content | Rationale |
|---|---|---|
| `docs/<NN-stage-folder>/` | Human-readable Markdown artifacts named exactly as the Delivery Spine mandates | The spine is the audit index; reviewers navigate by stage number |
| `evidence/<NN-stage-folder>/` | Machine-generated raw evidence: JUnit XML, coverage XML, SBOM, scan JSON, profiling CSV, trace exports, screenshots, terminal transcripts | Narrative claims are only defensible if the raw artifact that produced them is retained |

**Raw evidence file naming:** `EVD-<stage>-<nn>-<slug>.<ext>`
(example: `EVD-C-03-baseline-pytest-junit.xml`).

**Immutability rule:** evidence files are append-only. A re-run produces a new file with an
incremented `<nn>`; prior baselines are never overwritten, because before/after comparison
is the core of the Stage O value claim and of rubric criterion 1.

### 3.4 Evidence manifest

Each `evidence/<NN-stage-folder>/` directory must contain a `MANIFEST.md` listing, for every
raw file: filename, SHA-256, producing step ID, producing command, UTC timestamp, operator,
and the artifact(s) in `docs/` that cite it. This is what allows a reviewer to verify the
transformation without relying on verbal explanation (Challenge 16 acceptance standard).

---

## 4. Directory spine to be created

The executing team creates the following inside the repository. This is reproduced from the
Delivery Spine and is **mandatory**; deviations must be recorded as exceptions.

```
docs/
├── 00-preflight/{discovery,operating-contract,ai-economics}/
├── 01-engagement/        ├── 15-modernization/        ├── 29-incident-bcdr/
├── 02-stakeholders/      ├── 16-repo-validation/      ├── 30-release/
├── 03-problem-value/     ├── 17-implementation-prd/   ├── 31-observability/
├── 04-baseline-kpis/     ├── 18-delivery/             ├── 32-finops/
├── 05-current-state/     ├── 19-intelligence/         ├── 33-vendor-risk/
├── 06-root-cause/        ├── 20-application/          ├── 34-after-kpis/
├── 07-repo-assessment/   ├── 21-integration/          ├── 35-value-leakage/
├── 08-ai-qualification/  ├── 22-agentic-engineering/  ├── 36-benefits/
├── 09-initial-prd/       ├── 23-human-control/        ├── 37-operating-model/
├── 10-architecture/adrs/ ├── 24-security-privacy/     ├── 38-handover/
├── 11-data-context/      ├── 25-governance/           ├── 39-continuous-improvement/
├── 12-specs/features/    ├── 26-tevv/                 ├── 40-scale/
├── 13-traceability/      ├── 27-hardening/            ├── 41-retirement/
├── 14-transformation/    ├── 28-resilience/           ├── 42-executive/
└── final-prd/
evidence/                 (mirror of the above, raw machine-generated evidence)
semantic-layer/           (per Semantic_Layer_capture.pdf — see Stage D)
```

**Conflict to resolve:** the delivered repository already contains `docs/discovery/`
("reserved for system discovery notes"), which collides conceptually with the spine's
`docs/00-preflight/discovery/`. The runbook's recommendation is that the spine path is
authoritative and `docs/discovery/README.md` becomes a pointer. This is **OQ-13** and must
be ruled on before Stage A completes.

---

## 5. Stage map

| Stage | Name | Spine stages covered | Read-only? | Primary rubric criteria |
|---|---|---|---|---|
| **A** | Engagement Mobilisation & Read-Only Orientation | 0A, 0B, 0C | Yes | 1 |
| **B** | Qualification, Stakeholders & Problem Framing | 1, 2, 3 | Yes | 1 |
| **C** | Baseline: KPIs, Current State, Root Cause, Behaviour | 4, 5, 6, 7 | Yes | 1 |
| **D** | Semantic Layer Extraction | (11 pre-cursor; Guide p.6) | Yes | 1, 2 |
| **E** | Intervention Qualification & Initial PRD | 8, 9 | Yes | 2, 4 |
| **F** | Target Architecture, Data/Context Strategy & Specs | 10, 11, 12, 13 | Yes | 2, 4 |
| **G** | Transformation & Migration Planning | 14 | Yes | 2 |
| **H** | Repo 2.0 — Modernization & Validation | 15, 16 | **No** | 2, 4 |
| **I** | Implementation PRD & Delivery Planning | 17, 18 | No | 4 |
| **J** | Intelligence Core, Application, Integration, Agents | 19, 20, 21, 22 | No | 2, 4 |
| **K** | Human Control, Security/Privacy/RAI, Governance | 23, 24, 25 | No | 3 |
| **L** | TEVV & AI Red Teaming | 26 | No | 3 |
| **M** | Hardening, Resilience, Incident & BC/DR | 27, 28, 29 | No | 2, 3 |
| **N** | Release, Observability, FinOps, Vendor Risk | 30, 31, 32, 33 | No | 2, 3 |
| **O** | Outcome Measurement, Value Leakage, Benefits | 34, 35, 36 | No | 1, 4 |
| **P** | Operating Model, Handover, Drift, Scale, Retirement | 37–41 | No | 3 |
| **Q** | Model Portability Validation & Demo | Guide p.6 | No | 4, 5 |
| **R** | Executive Defence, Final As-Built PRD & Evidence Pack | 42, FINAL | No | 1, 5 |

---

## 6. Roles

The delivered artifacts name no individuals. These are **role slots**, to be filled before
Stage B completes (OQ-05). Until filled they must be recorded as `UNRESOLVED`, never
invented — the Delivery Spine is explicit: *"Do not invent owners where none have been
assigned; record them as unresolved governance gaps."*

| Role | Responsibility in this runbook | Status |
|---|---|---|
| Transformation Lead (FDE) | Owns the runbook, stage gates, evidence completeness | UNRESOLVED |
| Repository Owner | Authorises Stage H (first write stage) | UNRESOLVED |
| Security Owner | Owns Stages K, L, M security evidence and residual-risk acceptance | UNRESOLVED |
| SRE / Operations Owner | Owns Stages M, N, P operational evidence and SLOs | UNRESOLVED |
| Data Owner | Owns Stage C data baseline and Stage D semantic layer sign-off | UNRESOLVED |
| AI Governance Owner | Owns Stage E AI-vs-no-AI decision and Stage K autonomy matrix | UNRESOLVED |
| Compliance Owner | Owns Stage K obligations mapping and evidence retention | UNRESOLVED |
| Business Sponsor | Owns Stage B value framing and Stage R go/no-go acceptance | UNRESOLVED |

---

## 7. How to use this runbook

1. Read Document 01 first. Every step in Document 02 exists because of a finding in
   Document 01; a step whose finding you cannot reproduce should be challenged, not executed.
2. Work stages in order, **A through R**. Cross-stage dependencies are stated explicitly on
   every step, with the reason the dependency exists.
3. Do not begin a stage until the preceding stage's **Exit Criteria** table is fully green.
   A stage may exit as `CONDITIONAL PASS` only when every amber item has a named owner, a
   date and an entry in the residual-risk register.
4. Close every step with the **Required Final Response** format from `Prompt Template.pdf`:
   stage status (PASS / CONDITIONAL PASS / BLOCKED), key findings, major risks,
   assumptions/unknowns, artifacts created, blocking issues, recommended next action.
5. Maintain Document 04 as a live register. A step that surfaces a new unknown adds a row;
   it does not quietly assume.

---

## 8. Hard prerequisite before any step runs

**The delivered repository is not under version control.** `git rev-parse` returns
*"fatal: not a git repository"*, and there is no `.gitignore`, `LICENSE`, `CODEOWNERS` or
`SECURITY.md` (Finding F-01, Document 01).

The Delivery Spine requires that every generated artifact "be version-controlled", "not
overwrite prior evidence silently" and "preserve earlier baselines so before/after
comparison remains possible". **None of those three requirements can be met until the
repository is placed under version control.** Step A1 therefore initialises version control
and takes an immutable pre-transformation tag before anything else happens.

---

## 9. Summary of what the evidence shows today

A one-paragraph executive framing, expanded with evidence in Document 01:

> The delivered system is a credible three-generation brownfield estate: a legacy batch
> script with a hardcoded shared database password, a partially modernised FastAPI service
> whose authorisation is a client-supplied HTTP header, and a new AI endpoint that
> interpolates untrusted record content into a prompt, returns `guardrail_status:
> "not_enforced"`, carries no human approval gate and is callable with no authorisation
> check at all. Beneath it sits 2,124 rows of synthetic operational data in which 66.4% of
> 3,000 events carry no correlation identifier, every one of the six datasets contains three
> duplicate business keys and a fully-blank mandatory row, and a single identifier —
> `REC-0001` — is simultaneously the primary key of a shipment, a tracking event, a vehicle,
> a route, a carrier booking and an AI invocation. The audit log records no actor, no
> correlation ID and no approval. The test suite is three assertions long, one of which
> asserts the defect; as shipped it cannot even execute, because the dependency its own
> import requires is absent from `requirements.txt`. The system is not production-ready, and
> the gap is not primarily one of code quality — it is that almost nothing it does can
> currently be proven.
