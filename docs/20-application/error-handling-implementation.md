# Error handling implementation

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

All errors are `application/problem+json` (`errors.py`): 401 (no/invalid token, `WWW-Authenticate: Bearer`), 403 (policy, includes `policy_decision_id`), 404, 409, 422, 429 (`Retry-After`), 503 (AI disabled/unavailable), 500 (generic body, no internals). Provider failures never surface as 5xx: the gateway falls back and records `fallback_reason`. Tests: `test_contract_ops`, `test_identity_policy`, `test_ai_gateway`.
