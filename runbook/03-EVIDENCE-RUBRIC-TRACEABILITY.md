# Brownfield → Production-Grade Transformation Runbook

## Document 03 — Evidence Index & Rubric Traceability

| Field | Value |
|---|---|
| **Document** | 03 — Evidence Index & Rubric Traceability |
| **Version** | v1.0 |
| **Date** | 2026-10-08 |
| **Author / Agent** | AI-FDE Transformation Team — Delta-Team |
| **Status** | Draft for CTO review |
| **Evidence sources** | `Evaluation Rubrics.jpeg`; Challenge Guide; Delivery Spine; Documents 01 and 02 |
| **Purpose** | Make rubric coverage auditable at a glance, and state explicitly which criteria the current artifacts cannot yet satisfy |

---

## 1. The rubric

| # | Criterion | What it covers | Marks |
|---|---|---|---|
| **R1** | As-Is Understanding & Problem Identification | Understanding Repo 1.0, identifying gaps, risks, inconsistencies, technical debt and business problem | **20** |
| **R2** | Repo 2.0 Solution Design & Engineering | Quality of improved architecture, AI workflow, data/evidence design, decisioning, controls, resilience and overall solution thinking | **25** |
| **R3** | Governance, Risk, Security & Compliance | Human oversight, explainability, auditability, risk controls, security, compliance, observability and safe AI decision boundaries | **20** |
| **R4** | PRD & Working Application Execution | Quality of PRD, traceability of requirements, functional implementation, end-to-end workflow and working AI capabilities | **25** |
| **R5** | Presentation, Demonstration & Defence | Clarity of storytelling, quality of demo, ability to explain design choices, trade-offs, limitations and answer evaluator questions | **10** |
| | **TOTAL** | | **100** |

---

## 2. Rubric → evidence coverage matrix

Each row names the runbook steps that produce evidence for the criterion, the specific
primary evidence artifacts, and the acceptance standard the evidence must meet.

### R1 — As-Is Understanding & Problem Identification (20 marks)

| Sub-dimension | Producing steps | Primary evidence | Acceptance standard |
|---|---|---|---|
| Understanding Repo 1.0 | A4, C4, C7 | `docs/00-preflight/discovery/*` (12 artifacts); `docs/05-current-state/*`; `docs/07-repo-assessment/repo-assessment.md` | Evidence comes from code, data, configuration, tests or repository documentation — never from assumption |
| Identifying gaps and inconsistencies | A4, C4, C5, C7 | Document 01 findings register (57 findings); flow-to-code trace table; `EVD-C-05-data-profile.json` | Declared-versus-implemented gaps are named (F-05 portal, F-29 AI capabilities, F-50 contract) |
| Technical debt | C7 | `technical-debt-register.md`; `legacy-pattern-register.md`; `partial-migration-register.md` | Register cross-references all 57 finding IDs |
| Risk identification | A4, C6, K2 | `initial-risk-register.md`; `evidence-confidence-matrix.md` | Each cause carries supporting evidence, contradictory evidence and a confidence level |
| Behavioural baseline | C2, C3, C8 | `EVD-C-02-quickstart-transcript.txt`; `EVD-C-03-*` JUnit/coverage; `EVD-C-08-characterization-junit.xml` | The documented quick-start is recorded **failing**; 11 behaviours are pinned and labelled intended-legacy or defect |
| Business problem | B1, B3 | `problem-statement.md`; `engagement-go-no-go.md` | Technology-neutral; names no AI |
| Before/after proof | H10, N2, O2 | `EVD-H-10-behaviour-diff.csv`; `EVD-N-02-reconstruction.json`; `kpi-variance-table.md` | Every behaviour difference classified approved-change or regression; zero unexplained |

**Strongest available evidence for R1:** the paired Step C2 / Step H2 transcripts — the
project's own documented entry point recorded failing on the as-delivered tag and succeeding
afterwards. This is empirical rather than asserted, and it is cheap to produce.

### R2 — Repo 2.0 Solution Design & Engineering (25 marks)

| Sub-dimension | Producing steps | Primary evidence | Acceptance standard |
|---|---|---|---|
| Improved architecture | F1 | `target-architecture.md`; ADR set; **`ADR-00XX` superseding `ADR-0001`** | Options compared; every material decision has an ADR |
| AI workflow | H7, J1, J2, J3 | `prompt-registry.md`; `deterministic-ai-boundary.md`; `EVD-H-07-*`; `quality-latency-cost-results.md` | AI recommendations cannot silently become operational decisions |
| Data / evidence design | D1–D5, F2 | `semantic-layer/*`; `data-contracts.md`; `data-quality-rules.md`; `provenance-policy.md` | Semantic layer validates, is tested, and generates its JSON |
| Decisioning | D4, H4, K1 | `access-semantics.yaml`; `policy/opa/` with tests; `autonomy-matrix.md` | Access decisions consider role, resource, purpose, scope and risk |
| Controls | H3, H4, H9, M1 | `EVD-H-03-secret-scan.json`; `EVD-H-04-*`; `EVD-H-09-smoke.txt`; `sbom-summary.md` | No sensitive value required in committed code or example config |
| Resilience | M2, M3 | `resilience-architecture.md`; `ai-disabled-mode.md`; `EVD-M-03-drills/` (five drills) | The system defines what continues safely when dependencies fail |
| Reproducibility | H2, M1 | `EVD-H-02-quickstart-after.txt`; lockfiles; `Dockerfile`; real IaC | A new team can reproduce the environment from documented steps |
| Delivery pipeline | H1, H11 | `EVD-H-01-pipeline-run.txt`; `repo-quality-gate.md` | The pipeline generates evidence, not only executes commands |
| Portability | Q1, Q2 | `EVD-Q-01-*`; `EVD-Q-02-comparison.csv` | The application regenerates from the semantic layer under a second model |

### R3 — Governance, Risk, Security & Compliance (20 marks)

| Sub-dimension | Producing steps | Primary evidence | Acceptance standard |
|---|---|---|---|
| Human oversight | K1, H7 | `autonomy-matrix.md`; `approval-gates.md`; `human-control-test-results.md` | Approval is enforced in code, not advisory text (closes F-26) |
| Explainability | J1, J3, N1 | `prompt-registry.md`; `grounding-results.md`; `ai-telemetry-spec.md` | Model version, prompt version and input hash accompany every invocation |
| Auditability | H8, N2, R2 | `EVD-H-08-trace-sample.json`; `EVD-N-02-reconstruction.json`; `audit-evidence-index.md` | One business event reconstructed end to end, with the before-state gap documented |
| Risk controls | K2, K3, L4 | `security-control-matrix.md`; `residual-security-risks.md`; `residual-tevv-risks.md` | Every residual risk has a named owner and an acceptance record |
| Security | H3, H4, K2, K3, L3, M1 | `EVD-L-03-*` before/after attack transcripts; scan results; SBOM | Security claims are backed by repeatable validation |
| Compliance | K4 | `compliance-obligations.md`; `model-card.md`; `system-card.md`; `evidence-retention-policy.md` | Obligations map to controls, owners, evidence and approval points |
| Observability | N1, N2 | `slo-sla-definitions.md`; dashboards and alerts as code; `observability-validation.md` | Correlation flows UI → API → data → AI → policy → approval → audit |
| Safe AI boundaries | E1, H7, K1, L3 | `deterministic-vs-ai-boundaries.md`; `prompt-injection-controls.md`; red-team findings | Injection payloads seeded in the data are demonstrably defended |
| Change governance | H1, G4, P3 | `CODEOWNERS`; `EVD-G-04-authorisation.pdf`; `controlled-change-process.md` | Untracked prompt or model change in production is technically prevented |

### R4 — PRD & Working Application Execution (25 marks)

| Sub-dimension | Producing steps | Primary evidence | Acceptance standard |
|---|---|---|---|
| PRD quality | E3, I1, R4 | `initial-prd.md`; `implementation-prd.md`; `final-as-built-prd.md` | Three distinct PRDs; the later ones are reconciliations, not copies |
| Requirement traceability | F4, R4 | `requirements-traceability-matrix.md`; `EVD-F-04-finding-coverage-matrix.csv`; `requirement-disposition-matrix.md` | Bidirectional; no orphan requirements; every finding has a disposition |
| Functional implementation | H2–H9, J4, J5 | `application-test-summary.md`; `integration-test-results.md`; coverage reports | Characterization differences all explained |
| End-to-end workflow | J4, N2, Q3 | Demonstration recording; `EVD-N-02-reconstruction.json` | A complete business workflow executes against the running application |
| Working AI capabilities | J1–J3, L2 | `rag-evaluation-results.md`; `tevv-results.md`; `intelligence-release-gate.md` | Quality measured against datasets committed before evaluation |
| Evidence-driven delivery | I2 | `definition-of-done.md`; `evidence-checklist.md` | No work item complete without its evidence |

### R5 — Presentation, Demonstration & Defence (10 marks)

| Sub-dimension | Producing steps | Primary evidence | Acceptance standard |
|---|---|---|---|
| Storytelling | R3 | `executive-narrative.md`; `problem-to-value-story.md` | Every material claim maps to lifecycle evidence |
| Demo quality | Q3 | `demo-day-script.md`; rehearsal recording | Rehearsed within the agreed time budget (OQ-17) |
| Explaining design choices | F1, R3 | ADR set; `architecture-defence.md`; `ai-decision-defence.md` | Rejected alternatives are stated, not just the chosen option |
| Trade-offs and limitations | R1, R3, R4 | `known-limitations.md`; `lessons-learned.md`; `residual-risks.md` | Failures are stated voluntarily |
| Answering evaluator questions | F4, R2 | `EVD-F-04` finding matrix; `EVIDENCE-INDEX.md` | *"What happened to finding X?"* is answerable in one lookup |

---

## 3. Rubric criteria the current artifacts **cannot yet satisfy**

This section is the honest accounting the Challenge Guide's final submission standard
demands. Each item states what blocks it, which open question governs it, and what the
fallback position is if the blocker is not removed.

### 3.1 Hard blockers — cannot be satisfied at all without an external decision

| ID | Rubric | What cannot be satisfied | Why | Governing OQ | Fallback if unresolved |
|---|---|---|---|---|---|
| **B-1** | R4 | **"Working AI capabilities"** | The only AI code path is an in-process simulator whose output is the record's first column value (F-29). No model, no provider, no credentials and no network permission are specified anywhere in the delivered artifacts. | OQ-02, OQ-03 | Implement against a locally runnable open-weights model and state the constraint explicitly; score R4 on the governed AI *workflow* rather than on model quality |
| **B-2** | R2, R4 | **Second-model comparison** (Challenge Guide p.6) | Requires two distinct models. None is specified. | OQ-02 | None. If only one model is available, the Stage Q comparison cannot be performed and must be declared not-performed with the reason — not simulated |
| **B-3** | R3 | **Compliance obligations mapping** | No regulatory regime is named in any artifact, despite customs agents, cross-border routing and personal location data. | OQ-04 | Document a *candidate* obligations set clearly marked as an unvalidated working assumption, plus a validation plan; record the gap in the risk-acceptance register |
| **B-4** | R2, R3 | **Infrastructure-as-Code, identity, secrets management, deployment** | `infra/terraform/main.tf` names no provider (F-48). Every one of these depends on knowing the target platform. | OQ-01 | Produce a platform-neutral design plus one worked reference implementation, clearly labelled as illustrative |
| **B-5** | R1, R4 | **Business KPI baseline** (Spine 4) | No business metric exists anywhere in the repository (F-57). Spine 4 requires a *frozen before-state baseline* that Stages 34–36 compare against. | OQ-08 | Use declared proxies from `events.jsonl` and `ai_invocations.csv`, label every one a proxy with its limitations, and state the comparability caveat in Stage O |
| **B-6** | R4 | **ROI / NPV / benefits realisation** (Spine 36) | No cost, revenue, headcount or rate data exists. Every monetary figure would be invented. | OQ-09 | Present a parameterised model with explicit assumption inputs and a sensitivity analysis; never present a single ROI figure as a measurement |

### 3.2 Soft blockers — satisfiable, but only if a decision is made early

| ID | Rubric | Risk | Why | Governing OQ |
|---|---|---|---|---|
| **B-7** | R4 | **End-to-end workflow with a UI** | `apps/web/` is two TypeScript classes; the README's Angular portal does not exist (F-05) and the Playwright test passes against nothing (F-52). Building a real portal is substantial work; descoping it weakens the end-to-end demonstration. | OQ-06 |
| **B-8** | R3 | **Named approvers for every gate** | No stakeholder is named anywhere. The Spine forbids inventing owners. Gates without approvers produce evidence nobody has accepted. | OQ-05 |
| **B-9** | R3 | **Vendor and concentration risk** (Spine 33) | There are currently no vendors — `local-sim-v1` is in-process. The assessment is vacuous until OQ-01 and OQ-02 resolve. | OQ-01, OQ-02 |
| **B-10** | R5 | **Demonstration** | No demo environment, no time budget and no audience format are specified. | OQ-16, OQ-17 |
| **B-11** | R2 | **Data remediation** | `scripts/sanity_check.py` asserts exactly 354 rows per CSV, so quarantining defective rows breaks the repository's own contract (F-54). | OQ-14 |
| **B-12** | R3 | **Agentic engineering** (Spine 22) | The repository has an `ai_agent` persona and an `ai_invocations` dataset but no agent runtime. Whether to build one is a Stage E decision. | OQ-18 |
| **B-13** | R1, R3 | **Secret history exposure** | Step A1 commits the as-delivered tree, which contains live-looking credentials (F-09, F-10, F-12). Removing them later does not remove them from history. | OQ-19 |

### 3.3 Criteria fully satisfiable with the delivered artifacts alone

For balance, the following require **no** external decision and can be completed entirely from
what was delivered. These should be executed first, because they de-risk the score floor:

- **R1 in full.** Every sub-dimension is satisfiable from the repository, the data and the
  recorded baseline behaviour. R1 is worth 20 marks and depends on no open question.
- **R2 partially** — semantic layer (Stage D), reproducibility fixes (H2), record-identity
  and ETL correctness (H5, H6), contract completion (H9), resilience drills (M3). These are
  worth most of R2's design and engineering weight.
- **R3 substantially** — identity and authorisation (H4), AI guardrails (H7), audit and
  correlation (H8), threat model (K2), red teaming (L3), observability and reconstruction
  (N1, N2). Only the compliance sub-dimension is blocked.
- **R5 in full**, provided the demo is built on evidence produced by the above.

---

## 4. Finding → rubric coverage summary

| Rubric | Findings whose remediation produces evidence for this criterion | Count |
|---|---|---|
| R1 | F-01, F-02, F-03, F-05, F-19, F-29, F-30, F-32, F-33–F-38, F-42, F-51, F-53, F-54, F-57 | 19 |
| R2 | F-04, F-06, F-07, F-28, F-30, F-31, F-32, F-36–F-41, F-47–F-50, F-53–F-55 | 20 |
| R3 | F-01, F-08–F-29, F-42–F-47, F-49, F-56 | 31 |
| R4 | F-02, F-05, F-29, F-32, F-50, F-52, F-57 | 7 |
| R5 | Derived — R5 evidence is the presentation of R1–R4 evidence | — |

**Observation for the CTO.** Thirty-one of the fifty-seven findings map to R3 (Governance,
Risk, Security & Compliance), which carries 20 marks, while only seven map to R4 (PRD &
Working Application Execution), which carries 25. The delivered repository's defects are
concentrated in governance, but the marks are concentrated in execution. **The effort
allocation implied by the findings register is therefore not the effort allocation implied by
the rubric.** Stages H–K must not be allowed to consume the time budget that Stage J Step J4
(a genuinely working end-to-end workflow) and Stage E Step E3 / Stage R Step R4 (PRD quality
and requirement disposition) require. This is the single most important scheduling judgement
in the engagement, and it should be made deliberately at Step I2 when the increment plan is
set — not discovered late.

---

## 5. Evidence index structure

The final `evidence/EVIDENCE-INDEX.md` produced at Step R2 must carry one row per evidence
artifact with these columns, so that rubric coverage can be audited mechanically:

| Column | Content |
|---|---|
| Evidence ID | `EVD-<stage>-<nn>-<slug>` |
| File path | Path within `evidence/` |
| SHA-256 | Hash at time of production |
| Produced by | Runbook step ID |
| Produced at | UTC timestamp |
| Operator | Human or agent identity, including model version where applicable |
| Command | The exact command or procedure that produced it |
| Findings addressed | Finding IDs from Document 01 |
| Rubric criteria | R1–R5 |
| Cited by | The `docs/` artifact(s) that reference it |

**Verification at Step R5:** every row's hash resolves; every `docs/` citation resolves to a
row; every one of the 57 findings appears in at least one row or in the deferred/accepted
register; every rubric criterion has at least one row, or appears in §3 above with a stated
reason and fallback.
