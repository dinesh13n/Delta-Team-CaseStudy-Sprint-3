# Metrics specification

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/31-observability/EVD-N-01-observability-validation.json (SHA-256 b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-03 cardinality of route label if route templates are not used for unknown paths |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

All names below were found in the live `/metrics` output of the validation workload (EVD-N-01). [VF]

| Metric | Type | Labels | Meaning | Used by |
|---|---|---|---|---|
| http_requests_total | counter | route, status | every request | ApiHighErrorRate, AiRateLimitHits, dashboards |
| http_request_duration_seconds | histogram | route | request latency | ApiLatencyP95High |
| auth_denied_total | counter | reason | rejected credentials (401) | AuthDeniedSpike |
| policy_denied_total | counter | entity | policy denials (403) | PolicyDeniedSpike |
| ai_requests_total | counter | generated_by, abstained | AI responses by producer | AiFallbackRateHigh |
| ai_request_duration_seconds | histogram | generated_by | AI endpoint latency | AiLatencyP95High |
| ai_tokens_total | counter | none | estimated tokens (see ai-telemetry-spec) | dashboard |
| ai_fallback_total | counter | reason | model not used; deterministic answer returned | AiOutputLeakBlocked, AiFallbackRateHigh |
| ai_guardrail_blocked_total | counter | none | schema-violation abstains only | AiSchemaViolations |
| ai_decisions_total | counter | decision | human approve / reject | AiSuggestionsRejectedHigh |
| audit_chain_valid | gauge | none | 1 if the hash chain verifies at scrape time | AuditChainBroken |
| data_load_age_seconds | gauge | none | seconds since last published ETL run, -1 if unreadable | DataStale, DataLoadMissing |
| ai_circuit_open | gauge | none | 1 when the model circuit breaker is not closed | AiCircuitOpen |

## Defect found and fixed during N1 [VF]
The validation run showed `ai_guardrail_blocked_total` absent from the output until its first increment. A counter that does not exist yet makes `increase()` and `rate()` alerts miss the first event, which is the event that matters most for a leak. Fix: the application now creates `ai_guardrail_blocked_total`, `ai_fallback_total{reason=<6 known reasons>}` and `ai_decisions_total{decision=<2>}` at zero at start-up. Test: `tests/test_observability.py`.

## Semantics that are easy to get wrong
- **The output leak check does not increment `ai_guardrail_blocked_total`.** It produces `ai_fallback_total{reason="output_policy_violation"}`. The leak alert uses the latter. The tabletop (M4) originally named the former; the playbook should be read with this in mind.
- `ai_guardrail_blocked_total` counts only responses whose `guardrail_status` is `blocked` (schema violation abstain). Non-JSON model output produces `ai_fallback_total{reason="invalid_output"}` instead (observed in the workload).
- `429` is visible only as `http_requests_total{status="429"}`; there is no dedicated rate-limit counter.

## Not implemented
- `ai_cost_units_total` (named in the earlier observability spec): there is no price data. Cost is estimated offline from token counts in finops docs (N4). Deviation recorded.
- Per-tenant labels: single-tenant fixture; adding a tenant label would be a cardinality decision for the owner.
- `stale_gps` counters: the source has no timestamp, so staleness cannot be measured (see slo-sla-definitions.md).
