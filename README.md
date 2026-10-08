# AI-FDE Sprint 3 — Brownfield Repo Transformation Case Study

**Programme:** Birlasoft Forward Deployed Engineer (FDE) training — Sprint 3
**Team:** Delta-Team
**Target system:** `07-logistics-shipment-fleet-routing-ops` — Logistics: Shipment, Fleet,
Routing & Exception Operations
**Status:** Runbook prepared, pre-execution

---

## ⚠️ This repository is private and must stay private

The delivered brownfield repository contains **intentionally planted credential-shaped
values** — they are part of the exercise, not an accident:

| Value | Location | Finding |
|---|---|---|
| `Welcome123` | `legacy/reconcile_legacy.py`, `.env.example` | F-09, F-10 |
| `sk-workshop-hardcoded-example` | `.env.example` | F-11 |
| `replace-me-but-currently-shared` | `.env.example` | F-12 |

All data in `data/synthetic/` is synthetic, and all credentials above are fictitious
workshop values with no real-world validity. They are preserved deliberately so that the
transformation's before/after evidence remains verifiable. **Do not make this repository
public, and do not reuse any of these values anywhere.**

---

## Contents

| Path | What it is |
|---|---|
| `07-logistics-shipment-fleet-routing-ops/` | The delivered brownfield repository — three coexisting engineering generations (legacy batch scripts, partially modernised FastAPI services, an ungoverned AI gateway) plus synthetic operational data with seeded defects |
| `runbook/` | **The deliverable.** Six documents in Markdown and Word: overview, baseline assessment (57 findings), the 18-stage / 102-step transformation runbook, rubric traceability, and the open-questions register |
| `Prompts-Guidlines/` | The AI-FDE End-to-End Production Delivery Spine, prompt template and prompt anatomy |
| `AI-FDE_Brownfield_Repo_Transformation_Challenge_Guide.pdf` | The 16 core transformation challenges and their acceptance standards |
| `Semantic_Layer_capture.pdf` | Semantic layer structure and format rationale |
| `Evaluation Rubrics.jpeg` | The five scoring criteria (100 marks) |

**Start with `runbook/README.md`.**

---

## Where the work stands

Analysis and runbook preparation are complete. **No file in
`07-logistics-shipment-fleet-routing-ops/` has been modified or executed** — the repository
is byte-identical to what was delivered, which is what makes the Stage C behavioural
baseline and every later before/after claim verifiable.

Execution has not begun. Two things gate it:

1. **Written authorisation to modify the repository** (Open Question OQ-11). Runbook Stages
   A–G are read-only and can proceed without it; Stage H onward cannot.
2. **Four further blocking decisions** — target platform (OQ-01), the two models for the
   mandated comparison (OQ-02), network egress policy (OQ-03) and named approvers (OQ-05).

See `runbook/04-OPEN-QUESTIONS-REGISTER.md` §7 for the full list, each with a recommended
default so work is never blocked by an unanswered question.

---

## A note on repository structure

The runbook's **Step A1** calls for version control to be initialised *at the root of the
brownfield repository*, with the delivered tree committed byte-identical and tagged
`baseline/v0-as-delivered`.

This repository wraps the brownfield repo together with its supporting artifacts and the
runbook, so that root is `07-logistics-shipment-fleet-routing-ops/` rather than the
repository root. When executing Step A1, the as-delivered assertion and the baseline tag
apply to **that subtree**, and the `git diff` checks in the Stage A, B, C and G exit criteria
should be scoped to it:

```bash
git diff baseline/v0-as-delivered -- 07-logistics-shipment-fleet-routing-ops/
```

The alternative — a separate repository per concern — keeps Step A1 literal but splits the
evidence pack across repositories, which works against the Challenge 16 acceptance standard
that *a reviewer can verify the transformation without relying on verbal explanation*. The
single-repository structure was chosen for that reason; the scoping adjustment above is the
cost.

---

## Evaluation rubric

| # | Criterion | Marks |
|---|---|---|
| 1 | As-Is Understanding & Problem Identification | 20 |
| 2 | Repo 2.0 Solution Design & Engineering | 25 |
| 3 | Governance, Risk, Security & Compliance | 20 |
| 4 | PRD & Working Application Execution | 25 |
| 5 | Presentation, Demonstration & Defence | 10 |
| | **Total** | **100** |

Rubric coverage, including the criteria the current artifacts cannot yet satisfy, is mapped
in `runbook/03-EVIDENCE-RUBRIC-TRACEABILITY.md`.

## Execution status (2026-10-08)

All 18 stages (A-R) of `runbook/02-TRANSFORMATION-RUNBOOK.md` have been executed once by a single agent under the operator's instruction. Result: **NO-GO for production on real data; CONDITIONAL GO for a controlled pilot on synthetic data.** Start with `docs/42-executive/production-readiness-decision.md`, then `docs/42-executive/production-evidence-pack.md` and `evidence/EVIDENCE-INDEX.md` (every evidence file is hash-listed).

Not done, stated plainly: a portable AI-output specification (the Stage Q second-model run, `claude-haiku-5-5` on a subset, passed the safety gates and failed 2 of 8 fidelity gates; eight specification gaps are open), any real AI model, any deployment, any named owner or independent review, revocation of credentials still present in git history, branch protection. See `docs/42-executive/residual-risks.md` and `docs/42-executive/final-gate.md`.
