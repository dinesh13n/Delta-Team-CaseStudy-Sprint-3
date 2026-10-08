# Provisional Operating Contract

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

## 1. Purpose
Governs what may be done, by whom, to which parts of the engagement, from Stage A to the Stage H gate. It is the only change-control surface until Step H1 creates CODEOWNERS and branch protection (findings F-01, F-08).

## 2. Parties and role slots (PROVISIONAL)
| Role | Holder | Status |
|---|---|---|
| Transformation Lead (FDE) | Dinesh, executing engineer, acting | PROVISIONAL, self-held |
| Repository Owner | none named | UNRESOLVED |
| Security Owner | none named | UNRESOLVED |
| SRE / Operations Owner | none named | UNRESOLVED |
| Data Owner | none named | UNRESOLVED |
| AI Governance Owner | none named | UNRESOLVED |
| Compliance Owner | none named | UNRESOLVED |
| Business Sponsor | none named | UNRESOLVED |
| CTO (audience; write authorisation, OQ-11) | not named in artifacts | UNRESOLVED |

## 3. Authority in force
- Read-only analysis and evidence capture for Stages A to G: authorised by the operator's instruction of 2026-10-08 (decision-log D-004).
- Any modification inside `07-logistics-shipment-fleet-routing-ops/` (Stage H onward): **NOT authorised**. Needs written authorisation (OQ-11) at Step G4.
- Gate sign-offs: self-issued by the operator and marked PROVISIONAL until OQ-05 is answered.

## 4. Companion documents
scope-boundaries, repository-write-boundaries, environment-access-boundaries, data-use-constraints, provisional-tool-agent-permissions, provisional-human-approval-rules, evidence-contract, change-control-rules, stop-conditions, open-governance-decisions, operating-contract-readiness (all in this folder).

## 5. Precedence
If a document conflicts with this contract, this contract wins; if this contract conflicts with a named approver's written instruction, the instruction wins and the contract is amended through change-control-rules.
