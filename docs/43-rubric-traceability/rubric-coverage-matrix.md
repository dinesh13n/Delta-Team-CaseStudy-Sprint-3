# Rubric coverage matrix (verified)

| Field | Value |
|---|---|
| Stage | S: Evidence index and rubric traceability (runbook/03-EVIDENCE-RUBRIC-TRACEABILITY.md) |
| Runbook step | 03-1 (Doc 03 section 2) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PROVISIONAL: every named artifact resolves; acceptance standards judged by the author |
| Evidence sources | EVD-S-01-coverage-matrix.csv; docs/ and evidence/ trees at commit after ab37ec8 |
| Assumptions | Self-assessment by the same agent that built the evidence; no independent reviewer |
| Unresolved issues | OQ-01..05, OQ-18, OQ-19 (see blocker-status.md) |
| Residual risks | Statuses are the author's judgement against the standard in Document 03; an independent reviewer may rate lower |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Method
1. Every artifact named in the "Primary evidence" column of Document 03 section 2 (92 names, 36 sub-dimensions) was resolved to files in the repository by name or pattern. All 92 resolve; 4 needed a manual path (`ADR-00XX` is ADR-0002..0010, `ADR-0001` is in the app subtree, `semantic-layer/*` and `CODEOWNERS` are at repo paths). [VF] `EVD-S-01-coverage-matrix.csv` lists each resolved file with its SHA-256.
2. A name resolving is **not** the same as the standard being met. Each sub-dimension was then judged against its acceptance standard, using the stage gates and the checks quoted in the reason. Where a check was cheap to run, it was run in this step (debt register coverage of finding IDs; AI mentions in the problem statement).
3. Statuses: **MET** the standard is met by the evidence; **PARTIAL** met in part, the gap is stated; **NOT MET** the standard is not met and could be; **BLOCKED** an external decision prevents it (Document 03 section 3).

## Result
| Criterion | MET | PARTIAL | NOT MET | BLOCKED | Sub-dimensions |
|---|---|---|---|---|---|
| R1 | 6 | 1 | 0 | 0 | 7 |
| R2 | 5 | 4 | 0 | 0 | 9 |
| R3 | 5 | 2 | 1 | 1 | 9 |
| R4 | 4 | 1 | 0 | 1 | 6 |
| R5 | 4 | 1 | 0 | 0 | 5 |
| **Total** | 24 | 9 | 1 | 2 | 36 |

## Corrections made while resolving
- `docs/07-repo-assessment/technical-debt-register.md` covered 60 of 62 finding IDs; F-61 and F-62 were added so the Document 03 standard ("cross-references all finding IDs") holds. [VF]
- Document 03 says 12 discovery artifacts; there are 13. Document 03 says 57 findings; there are 62. Both are stated as found, not hidden.

## Matrix
| Rubric | Sub-dimension | Status | Files | Primary evidence (first 3) | Why |
|---|---|---|---|---|---|
| R1 | Understanding Repo 1.0 | **MET** | 11 | `docs/00-preflight/discovery/system-landscape.md`, `docs/00-preflight/discovery/security-observability-overview.md`, `docs/00-preflight/discovery/assumptions-unknowns.md` (+8 more) | 13 discovery artifacts (runbook said 12), current-state set and repo assessment, built from code, data, configuration and tests. Caveat: root cause RC-1 (who owns the partial modernisation) was not confirmed by an owner interview. |
| R1 | Identifying gaps and inconsistencies | **MET** | 1 | `evidence/04-baseline-kpis/EVD-C-05-data-profile.json` | 62 findings (runbook said 57; five found after Stage A); declared-versus-implemented gaps named (F-05 portal, F-29 AI, F-50 contract); data profile and flow-to-code trace present. |
| R1 | Technical debt | **MET** | 3 | `docs/07-repo-assessment/technical-debt-register.md`, `docs/07-repo-assessment/legacy-pattern-register.md`, `docs/07-repo-assessment/partial-migration-register.md` | `technical-debt-register.md` now cross-references all 62 finding IDs (it covered 60; F-61 and F-62 were added in this run, step 03-1). |
| R1 | Risk identification | **MET** | 2 | `docs/00-preflight/discovery/initial-risk-register.md`, `docs/06-root-cause/evidence-confidence-matrix.md` | `initial-risk-register.md` and `evidence-confidence-matrix.md` carry supporting evidence, contradicting evidence and a confidence level per cause. |
| R1 | Behavioural baseline | **MET** | 5 | `evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt`, `evidence/07-repo-assessment/EVD-C-03-junit.xml`, `evidence/07-repo-assessment/EVD-C-03-coverage.xml` (+2 more) | Documented quick-start recorded failing on the as-delivered tag (EVD-C-02); 12 characterization tests pin 11 behaviours (5 stay green, 7 xfail by approved change). |
| R1 | Business problem | **MET** | 2 | `docs/03-problem-value/problem-statement.md`, `docs/01-engagement/engagement-go-no-go.md` | `problem-statement.md` is technology-neutral (0 mentions of AI, LLM or model, checked by search in this run). |
| R1 | Before/after proof | **PARTIAL** | 3 | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv`, `evidence/31-observability/EVD-N-02-reconstruction.json`, `docs/35-value-leakage/kpi-variance-table.md` | Behaviour diff classified with 0 unexplained and one business event reconstructed end to end (EVD-N-02). No business KPI moved: the variance table holds proxies only and states no benefit was measured (B-5, B-6). |
| R2 | Improved architecture | **MET** | 11 | `docs/10-architecture/target-architecture.md`, `docs/10-architecture/adrs/ADR-0002-supersede-0001-partial-modernization.md`, `docs/10-architecture/adrs/ADR-0003-target-runtime-and-dependencies.md` (+8 more) | Options compared (`architecture-options.md`); ADR-0002..0010 (the original ADR-0001 is in the app subtree and ADR-0002 supersedes it). |
| R2 | AI workflow | **MET** | 4 | `docs/19-intelligence/prompt-registry.md`, `docs/20-application/deterministic-ai-boundary.md`, `evidence/15-modernization/EVD-H-07-ai-gateway-results.json` (+1 more) | Prompt registry with locked hashes, deterministic boundary, suggest-only output with approval record; red-team RT-10 (action without approval) fails. Quality of a real model is unmeasured (B-1). |
| R2 | Data / evidence design | **MET** | 9 | `docs/11-data-context/data-contracts.md`, `docs/21-integration/data-contracts.md`, `docs/11-data-context/data-quality-rules.md` (+6 more) | Semantic layer validates against its schema, generates its JSON and has 16 tests; data contracts, quality rules and provenance policy exist. |
| R2 | Decisioning | **PARTIAL** | 4 | `semantic-layer/access-semantics.yaml`, `07-logistics-shipment-fleet-routing-ops/policy/opa/access.rego`, `07-logistics-shipment-fleet-routing-ops/policy/opa/access_test.rego` (+1 more) | Role, entity, field and purpose are enforced, with Rego generated from `access-semantics.yaml`. Scope narrowing is reported but not enforced (declared gap, `scope_enforced=false`); risk is handled through the autonomy matrix, not the access decision. |
| R2 | Controls | **MET** | 5 | `evidence/15-modernization/EVD-H-03-secret-scan.json`, `evidence/15-modernization/EVD-H-04-negative-access-tests.txt`, `evidence/15-modernization/EVD-H-04-policy-allow-deny-matrix.csv` (+2 more) | Secret scan, negative access tests, smoke test and SBOM present; the tree needs no sensitive value. The credentials remain in git history and are not revoked (B-13, 4 findings FIXED-IN-TREE). |
| R2 | Resilience | **PARTIAL** | 3 | `docs/28-resilience/resilience-architecture.md`, `docs/28-resilience/ai-disabled-mode.md`, `evidence/28-resilience/EVD-M-03-resilience-tests-after-drills.txt` | Resilience architecture, AI-disabled mode and five drills pass. M-X2 NOT MET: IaC provisions nothing because no platform is chosen (OQ-01, B-4). |
| R2 | Reproducibility | **PARTIAL** | 2 | `evidence/15-modernization/EVD-H-02-quickstart-after.txt`, `07-logistics-shipment-fleet-routing-ops/Dockerfile` | Quick-start succeeds after the fix, hash-locked requirements, Dockerfile. No real IaC (B-4); |
| R2 | Delivery pipeline | **MET** | 2 | `evidence/15-modernization/EVD-H-01-pipeline-run.txt`, `docs/16-repo-validation/repo-quality-gate.md` | CI on GitHub: first real run failed on the coverage gate (D-013), second run green on Python 3.11 and 3.14; the pipeline uploads artifacts. Branch protection was not enabled when last checked. |
| R2 | Portability | **PARTIAL** | 2 | `evidence/40-scale/EVD-Q-01-preregistration.json`, `evidence/40-scale/EVD-Q-02-comparison.csv` | Run once on a four-behaviour subset with a same-vendor model: safety behaviour carried over, AI-output fidelity did not (2 of 8 gates fail), eight specification gaps open (IMP-Q04..Q13). |
| R3 | Human oversight | **MET** | 3 | `docs/23-human-control/autonomy-matrix.md`, `docs/23-human-control/approval-gates.md`, `docs/23-human-control/human-control-test-results.md` | Approval enforced in code (decision endpoint, 409 on a second decision, approval record); closes F-26; human-control tests pass. |
| R3 | Explainability | **MET** | 3 | `docs/19-intelligence/prompt-registry.md`, `docs/19-intelligence/grounding-results.md`, `docs/31-observability/ai-telemetry-spec.md` | Every AI response carries model, model version, prompt version and config hash; the audit event carries an input hash. Deterministic provider only: no real-model explanation exists. |
| R3 | Auditability | **MET** | 3 | `evidence/15-modernization/EVD-H-08-trace-sample.json`, `evidence/31-observability/EVD-N-02-reconstruction.json`, `docs/25-governance/audit-evidence-index.md` | Hash-chained audit v2 with tamper detection; one event reconstructed end to end (field coverage 10 of 10) with the before-state gap documented. |
| R3 | Risk controls | **NOT MET** | 3 | `docs/24-security-privacy/security-control-matrix.md`, `docs/24-security-privacy/residual-security-risks.md`, `docs/26-tevv/residual-tevv-risks.md` | Residual risks have role-level owners only; 0 of 12 risk acceptances are signed; no approver exists (OQ-05, B-8). The standard asks for a named owner and an acceptance record. |
| R3 | Security | **MET** | 2 | `evidence/26-tevv/EVD-L-03-redteam-v2.json`, `evidence/26-tevv/EVD-L-03-redteam-baseline.json` | Repeatable validation: red team 10 of 12 attacks succeed at baseline and 0 of 12 on v2, 25 security tests, bandit triaged, pip-audit 0, SBOM. Graded by the same agent that built it. |
| R3 | Compliance | **BLOCKED** | 4 | `docs/25-governance/compliance-obligations.md`, `docs/25-governance/model-card.md`, `docs/25-governance/system-card.md` (+1 more) | No regulatory regime is named (OQ-04, B-3). A candidate obligations set exists, labelled an unvalidated assumption, with a validation plan and risk acceptance RA-01 (unsigned). |
| R3 | Observability | **PARTIAL** | 2 | `docs/31-observability/slo-sla-definitions.md`, `docs/31-observability/observability-validation.md` | SLOs, dashboards and alerts as code are validated offline; correlation flows API to data to AI to policy to approval to audit. No collector, no traces, no deployed scrape; the UI is a thin view. |
| R3 | Safe AI boundaries | **MET** | 2 | `docs/08-ai-qualification/deterministic-vs-ai-boundaries.md`, `docs/24-security-privacy/prompt-injection-controls.md` | Injection payloads seeded into the data (RT-07, RT-08) are defended; untrusted text is delimited and sanitised; 0 injection-marker leaks in 192 evaluation cases. |
| R3 | Change governance | **PARTIAL** | 3 | `evidence/14-transformation/EVD-G-04-authorisation-record.txt`, `docs/39-continuous-improvement/controlled-change-process.md`, `.github/CODEOWNERS` | CODEOWNERS and a controlled-change process exist; prompt hashes are locked by script. The authorisation record EVD-G-04 is unsigned and branch protection was not enabled when last checked, so an untracked change is not technically prevented. |
| R4 | PRD quality | **MET** | 3 | `docs/09-initial-prd/initial-prd.md`, `docs/17-implementation-prd/implementation-prd.md`, `docs/final-prd/final-as-built-prd.md` | Three distinct PRDs (initial, implementation, final as-built); the later two are reconciliations with a change log. |
| R4 | Requirement traceability | **MET** | 3 | `docs/13-traceability/requirements-traceability-matrix.md`, `evidence/13-traceability/EVD-F-04-finding-coverage-matrix.csv`, `docs/final-prd/requirement-disposition-matrix.md` | Finding coverage matrix (62 rows) and requirement disposition matrix (48 rows, 0 unclassified); no orphan requirement found. Dispositions have role owners but no approver. |
| R4 | Functional implementation | **MET** | 2 | `docs/20-application/application-test-summary.md`, `docs/21-integration/integration-test-results.md` | 176 tests pass on the repository suite; every characterization difference is explained (0 unexplained); coverage gate 80% on apps and etl. |
| R4 | End-to-end workflow | **PARTIAL** | 1 | `evidence/31-observability/EVD-N-02-reconstruction.json` | A complete workflow (lookup, summary, approval, audit, reconstruction) runs against the running service and the thin view passes 10 of 10 browser checks. No recording with a person; the demo rehearsal was by the author, offline. |
| R4 | Working AI capabilities | **BLOCKED** | 3 | `docs/19-intelligence/rag-evaluation-results.md`, `docs/26-tevv/tevv-results.md`, `docs/19-intelligence/intelligence-release-gate.md` | No real model was ever called (B-1, OQ-02, OQ-03). The governed AI workflow runs on a deterministic provider and passes 192 of 192 evaluation cases; model quality, latency and cost are unmeasured. |
| R4 | Evidence-driven delivery | **MET** | 2 | `docs/18-delivery/definition-of-done.md`, `docs/18-delivery/evidence-checklist.md` | Definition of done and evidence checklist exist; every evidence file is in a hash manifest (134 of 134 rows verified). |
| R5 | Storytelling | **MET** | 2 | `docs/42-executive/executive-narrative.md`, `docs/42-executive/problem-to-value-story.md` | Executive narrative and problem-to-value story map claims to evidence (34-claim index). |
| R5 | Demo quality | **PARTIAL** | 1 | `docs/42-executive/demo-day-script.md` | Demo script with 28 s of offline beats rehearsed by the author; no audience, no recording of a person, budget unconfirmed (OQ-16, OQ-17; Q-X5 partial). |
| R5 | Explaining design choices | **MET** | 2 | `docs/42-executive/architecture-defence.md`, `docs/42-executive/ai-decision-defence.md` | ADR set, architecture defence and AI decision defence state rejected alternatives. |
| R5 | Trade-offs and limitations | **MET** | 3 | `docs/final-prd/known-limitations.md`, `docs/42-executive/lessons-learned.md`, `docs/42-executive/residual-risks.md` | Known limitations, lessons learned and residual risks state failures voluntarily (R-X5 met). |
| R5 | Answering evaluator questions | **MET** | 3 | `evidence/13-traceability/EVD-F-04-finding-coverage-matrix.csv`, `evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv`, `evidence/EVIDENCE-INDEX.md` | "What happened to finding X?" is one lookup in `EVD-F-04b-finding-disposition-final.csv`; the rubric-aware evidence index built in this run adds findings and criteria per file. |
