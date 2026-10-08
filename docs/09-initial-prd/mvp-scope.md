# MVP Scope (includes OQ-06 ruling)

| Field | Value |
|---|---|
| Stage | E: Intervention Qualification and Initial PRD (Spine 9) |
| Runbook step | E3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/03-problem-value/; docs/08-ai-qualification/; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## MVP
FR-01..FR-20 delivered as a service with a thin read-only operations view, a validated data intake, a governed exception summary and a traceable audit chain, all on a platform-neutral container target (readiness only, OQ-20 default).

## OQ-06 ruling (operator portal)
Decision: a **thin read-only operations view** (record lookup and exception summary, plain HTML served by the service) is IN the MVP; a full Angular portal is OUT (deferred). Reason: the rubric rewards a working application, and a thin view demonstrates the API and approvals without a framework dependency. Owner: Product owner UNRESOLVED; ruling by the operator, PROVISIONAL.

## Future scope
ETA prediction and route optimisation (I7, I8) once real history exists; carrier saga implementation; full portal; agentic handling (OQ-18).
