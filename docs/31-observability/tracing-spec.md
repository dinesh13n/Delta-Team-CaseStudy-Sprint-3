# Tracing specification

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PARTIAL |
| Evidence sources | apps/api/correlation.py; scripts/reconstruct.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-04 no cross-service trace |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## State [VF]
There is **no distributed tracing**: no OpenTelemetry SDK, no spans, no exporter. What exists is the correlation id, which serves as a trace identifier within this single process:

| Hop | Carries the id? |
|---|---|
| Inbound request (header `X-Correlation-ID`, validated, else generated) | yes |
| Response header | yes |
| Request log line | yes |
| Policy decision record | yes (`decision_id` linked from the audit event) |
| Audit event | yes |
| AI gateway call | yes (passed as `correlation_id`; stored in the AI audit detail) |
| Approval record | yes (`correlation_id` stored at registration) |
| Outbound model call | **no**: the id is not sent to a provider (no provider is wired) |
| Source event stream | **no**: the source has no correlation column (F-M3-01); lineage is `load_id` + `source_row` instead |

## Why this is adequate for now and when it stops being
One process, no outbound calls: the correlation id gives a complete in-process path (see incident-reconstruction-example.md). It stops being adequate when a real model, an IdP, a queue or a second service is added. At that point W3C `traceparent` propagation and spans around the provider call are needed.

## Target (not built)
- Accept and emit `traceparent`; use its trace-id as the correlation id when present.
- Spans: request, policy decision, data read, provider call (attributes: model name/version, prompt version, token estimate, outcome), human decision.
- Sampling: 100% of AI calls (volume is low and each is evidence), head-sampled for the rest.
- Never attach prompt text or record values as span attributes.

The existing `observability/otel-notes.md` states the same target; it is unchanged.
