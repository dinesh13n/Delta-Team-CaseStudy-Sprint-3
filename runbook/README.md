# Brownfield → Production-Grade Transformation Runbook

**Target system:** `07-logistics-shipment-fleet-routing-ops` — Logistics: Shipment, Fleet,
Routing & Exception Operations
**Prepared by:** AI-FDE Transformation Team — Delta-Team
**Version:** v1.0 · **Date:** 2026-10-08 · **Status:** Draft for CTO review

---

## What this package is

An execution-ready runbook for transforming the delivered brownfield repository into a
production-grade repository, with complete and verifiable evidence for every claim.

**Scope constraint honoured:** this package is the preparation of the runbook only. No
repository file was created, modified, refactored or executed in producing it. The only
activity performed against the repository was read-only inspection and read-only data
profiling, with all scripts and outputs written outside the repository tree.

---

## Contents

| Read in this order | Document | What it gives you |
|---|---|---|
| 1 | **00 — Overview** | Scope, evidence contract, directory spine, role slots, how to use the runbook, and the hard prerequisite that must be met before any step runs |
| 2 | **01 — Baseline Assessment** | 57 findings with file-level evidence, severity and rubric linkage; what is genuinely sound and must be preserved; the three findings that shape everything else |
| 3 | **02 — The Runbook** | 18 stages, 102 numbered steps. Each step states its action, inputs, the earlier step it depends on **and why**, its outputs, the evidence it must capture and where that evidence is stored. Each stage ends with verifiable exit criteria |
| 4 | **03 — Evidence & Rubric Traceability** | Rubric coverage matrix mapping every criterion to the steps and evidence artifacts that satisfy it, plus an explicit list of the criteria the current artifacts **cannot yet satisfy**, each with a fallback |
| 5 | **04 — Open Questions Register** | 23 open questions with owners, blocked steps and a recommended default for each, so work is never blocked by an unanswered question |

Each document is provided as both `.md` and `.docx`.

---

## The three things to know before reading further

**1. The repository is not under version control.** `git rev-parse` returns *"fatal: not a git
repository"*. The Delivery Spine requires every artifact to be version-controlled, to never
overwrite prior evidence, and to preserve baselines for before/after comparison. None of those
is possible today, which is why Step A1 establishes version control and an immutable
as-delivered tag before anything else happens.

**2. The system's deficiency is provability, not just code quality.** About one third (32.8%) of the event stream carries no correlation ID. The audit record has no actor. The audit sink is a local file
the audited process writes. The pipeline produces no evidence. Four of the five rubric criteria
are scored on demonstrable proof, so evidence infrastructure is Stage A, not a late-stage
activity.

**3. The findings and the marks are not in the same place.** Thirty-one of the fifty-seven
findings map to Governance, Risk, Security & Compliance (20 marks); only seven map to PRD &
Working Application Execution (25 marks). Left to its own gravity, the findings register will
pull effort away from the working application. That trade-off should be made deliberately at
Step I2, not discovered late. See Document 03 §4.

---

## The five decisions needed from the CTO first

1. **OQ-11** — Who authorises the first write to the repository, and when? Everything from
   Stage H onward is blocked without it; Stages A–G can proceed in the meantime.
2. **OQ-05** — Who are the named approvers? Every gate signature depends on it, and the
   Delivery Spine forbids inventing owners.
3. **OQ-02** — Which two models? The Challenge Guide's second-model comparison cannot be
   simulated or substituted.
4. **OQ-01** — Which target platform? Four stages of infrastructure, identity, secrets and
   release work are platform-shaped.
5. **OQ-12** — What is the time budget? It governs the trade-off in point 3 above.

Full detail, with recommended defaults for each, in Document 04.
