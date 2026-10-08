# Observability specification

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

Built on `observability/otel-notes.md` (AI telemetry fields) and made binding here.
- Logs: JSON, one line per request: ts, level, correlation_id, method, route, status, latency_ms, actor_role.
- Metrics (`/metrics`): `http_requests_total{route,status}`, `http_request_duration_seconds` histogram, `ai_requests_total{generated_by,abstained}`, `ai_tokens_total`, `ai_cost_units_total`, `ai_fallback_total{reason}`, `ai_guardrail_blocked_total`, `etl_rows_total{outcome}`, `etl_quarantine_ratio`, `audit_chain_valid` gauge.
- AI telemetry per call: token_count, latency_ms, model_version, prompt_version, fallback_reason, guardrail_result, cost_units.
- Traces: OpenTelemetry-compatible span names are specified; export is optional and off by default [ASM].
- SLO candidates: p95 read <= 500 ms; AI p95 <= 3,000 ms; correlation coverage 100% of new events.
