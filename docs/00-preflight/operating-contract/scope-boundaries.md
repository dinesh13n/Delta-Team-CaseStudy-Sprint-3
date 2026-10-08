# Scope Boundaries

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0B provisional operating contract |
| Runbook step | A5 (runbook/02-TRANSFORMATION-RUNBOOK.md, Stage A) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | **PROVISIONAL**, Draft pending named approvers (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/ (A4 pack); runbook/00-RUNBOOK-OVERVIEW.md section 6; runbook/04-OPEN-QUESTIONS-REGISTER.md; docs/00-preflight/operating-contract/decision-log.md |
| Assumptions | The operator acts for every role slot only to keep work moving; this is not an assignment of ownership |
| Unresolved issues | OQ-01, OQ-02, OQ-03, OQ-05, OQ-11 (blocking) |
| Residual risks | Every approval below is self-issued until named approvers exist |

Every owner, approver and decision right in this contract is **PROVISIONAL**. No owner has been invented. Where the table says UNRESOLVED, nobody has been assigned.

## 1. In scope [VF from runbook 00 section 2]
- Understanding, baselining and (after authorisation) transforming `07-logistics-shipment-fleet-routing-ops/`, with evidence mapped to the five rubric criteria.
- Documents, evidence and semantic-layer files at the wrapper repository root (`docs/`, `evidence/`, `semantic-layer/`, `runbook/`).

## 2. Out of scope
- Any production system, real data, real credentials or real customers. Nothing in the repository connects to one (A4 system-landscape.md).
- Re-architecture beyond what the Challenge Guide's 16 challenges require.
- Rewriting the training PDFs, the rubric image or the prompt guidelines at the repository root.

## 3. Exclusions needing a decision
| Item | Status |
|---|---|
| Operator web portal (apps/web) | OQ-06, unresolved |
| Agentic AI | OQ-18, unresolved |
| Real deployment versus readiness only | OQ-20, unresolved |
| Regulatory regime and location-data rules | OQ-04, OQ-21, unresolved |

## 4. Boundary of the baseline
The as-delivered subtree is the frozen reference (`baseline/v0.1-as-delivered-bytes`). Any statement about "current behaviour" means that subtree.
