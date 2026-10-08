# System specification

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

## Scope
A modular monolith (ADR-0002) exposing the API in `api-contracts/openapi.yaml`, a curated data layer behind a DataRepository port, a policy engine driven by `semantic-layer/access-semantics.yaml`, an AI gateway for one use case (I9 exception summary, suggest-only), and a hash-chained audit log.
## Request pipeline (every protected endpoint)
1. Assign or accept `X-Correlation-ID` (generated if absent or malformed).
2. Verify bearer token (TokenVerifier port). Failure -> 401, audit `auth.denied`.
3. Validate path/query parameters against the schema. Failure -> 422.
4. Evaluate policy (persona, entity, field, purpose). Deny -> 403, audit with rule id.
5. Execute use case through ports. Not found -> 404.
6. Filter/mask fields per policy. Write audit event. Return body with `X-Correlation-ID`.
## State
No server-side session. Persistent state: curated data files, quarantine files, audit log, approval records. State transitions are in `features/` specs.
## Constraints
Single process, synchronous, Python 3.14 target (ADR-0003). No outbound network except the optional model provider. Default provider is deterministic, so the system works with no model.
