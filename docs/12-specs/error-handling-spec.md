# Error handling specification

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

Body for every error: `application/problem+json` with `type`, `title`, `status`, `detail` (no internals), `correlation_id`, optional `policy_decision_id`.
| Condition | Status | Audit | Notes |
|---|---|---|---|
| no/invalid/expired token | 401 | auth.denied | `WWW-Authenticate: Bearer` |
| policy deny | 403 | <action>.denied with rule id | no data in body |
| key not found | 404 | not logged as error | exact match only |
| malformed id, bad query | 422 | no | |
| already decided | 409 | no | |
| rate limit | 429 | yes | AI endpoint only, 30/min per subject [ASM] |
| data layer or provider failure | 503 | yes | provider failure falls back to deterministic first; 503 only if that also fails |
| unexpected | 500 | yes | generic detail; stack trace in log only |
Never return 200 for an error (baseline defect: `{"error":"forbidden"}` with 200).
