# API contracts

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

The complete machine-readable contract is `api-contracts/openapi.yaml` (OpenAPI 3.0.3, validated with openapi-spec-validator, 10 operations). It closes **F-50**, because the brownfield fragment `data/contracts/openapi-fragment.yaml` only described `/health`.
| # | Method and path | Purpose | Auth | Success | Errors |
|---|---|---|---|---|---|
| 1 | GET /health | liveness | none | 200 | |
| 2 | GET /ready | readiness | none | 200 | 503 |
| 3 | GET /metrics | metrics | token, role ops | 200 | 401,403 |
| 4 | GET /shipments | list | token | 200 | 401,403,422 |
| 5 | GET /shipments/{id}/events | events | token | 200 | 401,403,404,422 |
| 6 | GET /records/{id} | exact key lookup | token | 200 | 401,403,404,422 |
| 7 | POST /ai/summarize/{id} | suggest-only summary | token | 200 | 401,403,404,422,429,503 |
| 8 | POST /ai/summaries/{id}/decision | approve or reject | token, reviewer role | 200 | 401,403,404,409,422 |
| 9 | GET /audit/verify | chain check | token, auditor role | 200 | 401,403 |
| 10 | GET /kpis | K1..K10 | token | 200 | 401,403 |
## Behaviour differences from the brownfield API (intentional, to be reported in H11)
| Area | Baseline [VF] | Target |
|---|---|---|
| Role | `X-User-Role` header trusted, default operator | verified bearer token, role from claims |
| Unknown key | first row returned (silent) | 404 |
| Invalid key shape | accepted | 422 |
| Denial | `{"error":"forbidden"}` with HTTP 200 | 403 problem body |
| Summary | `guardrail_status: not_enforced` | schema-validated output, abstention path |
| Compatibility | | `summary`, `model`, `guardrail_status` keys are retained (test_api_contract) |
Versioning: URL-stable in 1.x, additive changes only; breaking changes need a new major and an ADR.
