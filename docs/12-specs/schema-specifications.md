# Schema specifications

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | openapi.yaml; schemas/; docs/09-initial-prd; docs/10-architecture; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; open items in docs/12-specs/spec-readiness.md |
| Residual risks | Specs are PROVISIONAL until OQ-01/02/03/05/11 are ruled |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Schema | File | Purpose | Closes |
|---|---|---|---|
| Audit event | `schemas/audit-event.schema.json` | actor, correlation_id, tenant, resource, policy_decision, model and prompt version (`model`), input_hash, approval_id, prev_hash/hash | F-43 |
| AI summary output | `schemas/ai-summary-output.schema.json` | summary, recommendation, abstention, guardrail, provenance, `requires_human_approval` const true | F-25 |
| Semantic layer | `semantic-layer/schemas/semantic-layer.schema.json` | entities, rules, metrics | D5 |
| API types | `api-contracts/openapi.yaml#/components/schemas` | request and response | F-50 |
Checks: `evidence/12-specs/EVD-F-03-schema-checks.txt` (3 valid instances accepted, 5 invalid rejected). Hash chain: `hash = SHA-256(canonical_json(event without hash) + prev_hash)`; genesis `prev_hash` is 64 zeros. `tenant` is "default" until multi-tenancy is ruled [ASM].
