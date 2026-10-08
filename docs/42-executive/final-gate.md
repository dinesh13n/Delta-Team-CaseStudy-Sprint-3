# Final gate and submission

| Field | Value |
|---|---|
| Stage | R |
| Runbook step | R5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL; self-signed |
| Evidence sources | all stage gates; evidence/EVIDENCE-INDEX.md; runbook/04-OPEN-QUESTIONS-FINAL-REVISION.md |
| Assumptions | See assumptions in body |
| Unresolved issues | 13 open questions; Q1-Q3 not performed |
| Residual risks | See residual-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Stage gates
| Stage | Gate document | Result |
|---|---|---|
| A | docs/00-preflight/stage-a-gate.md | PASS (self-signed) |
| B | docs/03-problem-value/stage-b-gate.md | PASS (self-signed) |
| C | docs/07-repo-assessment/stage-c-gate.md | PASS |
| D | docs/11-data-context/stage-d-gate.md | PASS |
| E | docs/09-initial-prd/stage-e-gate.md | PASS |
| F | docs/13-traceability/stage-f-gate.md | PASS |
| G | docs/14-transformation/stage-g-gate.md | PASS, authorisation unsigned (D-009) |
| H | docs/16-repo-validation/stage-h-gate.md | CONDITIONAL PASS |
| I | docs/18-delivery/stage-i-gate.md | PASS |
| J | docs/19-intelligence/stage-j-gate.md | CONDITIONAL PASS (no real model) |
| K | docs/23-human-control/stage-k-gate.md | PASS |
| L | docs/26-tevv/stage-l-gate.md | PASS (same-agent grading) |
| M | docs/28-resilience/stage-m-gate.md | CONDITIONAL PASS (M-X2 NOT MET) |
| N | docs/31-observability/stage-n-gate.md | CONDITIONAL PASS |
| O | docs/34-after-kpis/stage-o-gate.md | CONDITIONAL PASS (no benefit) |
| P | docs/37-operating-model/stage-p-gate.md | PASS design / OPEN people |
| Q | docs/40-scale/stage-q-gate.md | **CONDITIONAL: Q1-Q3 not performed** |
| R | this document | **CONDITIONAL** |
Every gate is self-signed by the operator, PROVISIONAL (GOV-10). No gate has an independent signature.

## Stage R exit criteria
| # | Criterion | Result | Evidence |
|---|---|---|---|
| R-X1 | Readiness decision states ready / not ready / risk accepted and by whom | **MET** | production-readiness-decision.md |
| R-X2 | All 15 template sections populated with cited evidence | **MET** (15 headings; NOT MET areas stated in-section) | production-evidence-pack.md |
| R-X3 | Every cited evidence file exists, SHA-256 matches manifest | **MET**: 113 of 113 manifest rows verified; 200 of 200 inline citations match | EVD-R-03 |
| R-X4 | Every material claim maps to an evidence artifact | **PARTIAL**: index of 34 claims written; no reviewer sample (no reviewer) | executive-evidence-index.md |
| R-X5 | Narrative includes failures and trade-offs | **MET** | lessons-learned.md |
| R-X6 | Every original requirement classified | **MET**: 48 rows, 0 unclassified | requirement-disposition-matrix.md |
| R-X7 | Each of the 57 (now 62) findings has a disposition | **PARTIAL**: all 62 dispositioned (43 fixed, 4 fixed in tree, 10 partial, 2 changed, 2 deferred, 1 proposed-accepted); owners are roles, no dates agreed, no approver | EVD-F-04b |
| R-X8 | Every rubric criterion has mapped evidence; unsatisfiable stated | **MET** (table below) | this document |
| R-X9 | Every open question resolved or formally accepted | **NOT MET**: 13 open, 0 formally accepted by an owner | 04-OPEN-QUESTIONS-FINAL-REVISION.md |

## Rubric coverage (Document 03)
| Criterion (marks) | Strongest evidence | What cannot be claimed |
|---|---|---|
| R1 As-Is understanding (20) | EVD-C-02 transcript; 62-finding register; data profile; flow-to-code trace; 5 root causes | RC-1 (partial modernisation ownership) not confirmed by an owner interview |
| R2 Repo 2.0 design (25) | ADR-0002..0010; semantic layer; specs; red team 10/12 → 0/12; CI green 3.11/3.14 | platform, IaC and traces absent; portability untested |
| R3 Governance, security (20) | audit chain and reconstruction; autonomy matrix; threat model; 25 security tests; SBOM | no named owners; 0 of 12 acceptances signed; credentials unrevoked; no independent review |
| R4 PRD and working app (25) | three PRDs; traceability; 176 tests; running service; Chromium run 10/10 | no real model; thin view only; no deployment |
| R5 Presentation (10) | demo script (28 s offline beats), pitch, limitations stated voluntarily | rehearsal by author only; no audience |

## Corrections made at this gate
D-013 (coverage gate scope, found by the first real CI run), D-014 (file modes, test-count note), 58 evidence files late-registered, F-04/F-06 dispositions updated after reading the web app, `OQ-24` reference removed.

## Tags (not yet on GitHub)
The cloud workspace could not publish tags: `git push` of a tag and the GitHub API tag endpoints are refused by the session's egress policy (HTTP 403, "Write access to this GitHub API path is not permitted"). This was not worked around. The branch `main` is pushed. The operator creates the three tags from a clone that has pulled `main`:

```
git pull origin main
git tag -a baseline/v1-characterized 4c84af1 -m "Characterization tests present; created retroactively on the import commit"
git tag -a repo/v2-validated 9c1ce82 -m "Transformed repo validated: CI green on Python 3.11 and 3.14"
git tag -a release/v1-production-candidate <hash of the latest commit on main> -m "Candidate for a synthetic-data pilot, NOT a production release"
git push origin baseline/v1-characterized repo/v2-validated release/v1-production-candidate
```
Honest note on `baseline/v1-characterized` and `repo/v2-validated`: Stages A-P were committed in one import commit (4c84af1), so the runbook's ordering proofs (characterization tests committed before the Stage H changes; thresholds and datasets committed before results) cannot be shown by git history. They rest on file timestamps recorded in the gate documents. `repo/v2-validated` points at the commit whose first CI run failed; the green state is 9c1ce82 and later, so for a validated tag use 9c1ce82 or the final commit instead.

`release/v1-production-candidate` marks a **candidate for a synthetic-data pilot**, not a production release.
