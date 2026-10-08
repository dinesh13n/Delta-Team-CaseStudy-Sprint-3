# Failure mode analysis

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | drills, tests |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Failure | Detection | Effect | Mitigation | Drill |
|---|---|---|---|---|---|
| FM-01 | model slow | timeout metric / `ai_fallback_total{reason="provider_timeout"}` | AI answers late, falls back at the timeout | timeout 5 s | D2 |
| FM-02 | model down | `provider_error`, then `circuit_open` | AI is deterministic only | breaker | D2 |
| FM-03 | model returns invalid JSON | `schema_invalid` | fallback | validation | eval failure set |
| FM-04 | model leaks a forbidden value | `output_policy_violation`, `ai_guardrail_blocked_total` | fallback, event audited | leak scan | eval, M4 tabletop |
| FM-05 | ETL crashes mid-run | non-zero exit, no new report | stale data, no corruption | staged publish | D5 |
| FM-06 | damaged input rows | `ROW-SHAPE`/BR-* quarantine, ratio > 5 % fails the run | rows excluded with reasons | quarantine | D5 |
| FM-07 | duplicate events | BR-01/BR-02 | not double counted | de-dup | D3 |
| FM-08 | duplicate booking request | idempotency key | one booking | saga | D3, J5 sim |
| FM-09 | carrier transient errors | retry counter | bounded retries | ceiling 5, backoff | J5 sim |
| FM-10 | data not refreshed | `/ready` 503 `data_fresh` when `DATA_MAX_AGE_S` set | stale answers | freshness gate | D4 |
| FM-11 | missing correlation id | generated at the edge | trace still possible | middleware | D1 |
| FM-12 | audit log unwritable | `/ready` audit check | requests still served? **see note** | readiness | not drilled |
| FM-13 | audit file edited | `/audit/verify` | detected | hash chain | tests |
| FM-14 | process crash | platform restart | in-memory rate limits and breaker state reset; approvals persisted | JSONL stores | not drilled |
| FM-15 | disk full | write errors | audit append fails | **no handling designed** | not drilled |

Notes: FM-12/FM-15: the audit write is on the request path. If it raises, the request returns the generic 500 (fail closed: no unaudited action). This was reasoned from the code, not drilled. FM-14 was not drilled either.
