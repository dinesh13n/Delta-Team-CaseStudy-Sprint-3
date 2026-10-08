# Observability architecture

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (code) / CONDITIONAL (no collector, no platform) |
| Evidence sources | evidence/31-observability/EVD-N-01-observability-validation.json (SHA-256 b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485) |
| Assumptions | [ASM] Prometheus-compatible collector will be the platform's choice |
| Unresolved issues | OQ-01, OQ-05; no collector run |
| Residual risks | N-R-01 alerts never seen firing |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What exists [VF]
| Signal | Mechanism | Where |
|---|---|---|
| Metrics | in-process registry rendered as Prometheus text at `GET /metrics` (role `ops` only) | `apps/api/metrics.py`, `apps/api/main.py` |
| Logs | one JSON line per request to stdout: ts, level, route, status, latency, `correlation_id`, `actor_role`, `data_load_id` | `observe` middleware |
| Audit | hash-chained JSONL: actor, role, resource, policy decision, outcome, correlation id, approval id, AI detail | `apps/api/audit_chain.py` |
| Approval record | JSONL: who requested, who decided, when | `apps/api/ai/approvals.py` |
| Correlation | `X-Correlation-ID` accepted (validated) or generated, echoed on the response, written to logs and audit | `correlation.py` |
| Data lineage | `X-Data-Load-Id` header and `data_load_id` in logs and AI audit detail | M3/N1 |
| Alerts, dashboards | as code under `observability/` (15 alert rules, 16 dashboard panels) | validated, see below |

## What does not exist [VF]
- No Prometheus, Grafana, log shipper or collector has been run. Rules were checked for syntax and for references to metrics the service really exports; **no alert has been observed firing or routing**.
- No distributed tracing. `trace_id` is the correlation id; there are no spans and no OpenTelemetry SDK (see tracing-spec.md). PARTIAL.
- No log retention, access control or shipping design for the logs (platform undecided, OQ-01).
- No on-call tool, paging route or named recipient (OQ-05).

## Design choices
1. **Audit is the evidence source; metrics are the early warning; logs are the debugging aid.** Nothing in a metric or a log is relied on for accountability.
2. **No sensitive values in telemetry.** Labels are bounded enumerations (route template, status, reason, decision, generated_by). Subject identifiers appear in audit, not in metric labels. Logs carry the role, not the subject.
3. **Metric labels are bounded.** `auth_denied_total{reason}` uses a sanitised, truncated reason string (≤ 40 chars) so an attacker cannot create unbounded series with crafted tokens.
4. **Pull model.** Prometheus scrapes `/metrics` with an `ops` bearer token. The token must be a platform-issued service credential; none exists yet.

## Known limits [VF]
- `/metrics` runs a full `audit.verify()` per scrape, O(n) in audit size. At a 15 s scrape interval and a large audit file this becomes a load source. Mitigation: cache the verification result for N seconds or move verification to a periodic job (backlog, DEBT-N1-01).
- Counters live in process memory and reset at restart; with more than one replica each exports its own series (fine for Prometheus `sum`, but `audit_chain_valid` is per replica).
- The renderer emits no `# HELP` / `# TYPE` lines. Prometheus accepts this; typed tooling will not know counters from gauges.
- Counters that carry a dynamic label (`auth_denied_total`, `policy_denied_total`) do not exist until the first event. The alerts on them use `rate() > 1`, which is not sensitive to the first event. The safety-relevant counters are created at zero at start-up (see metrics-spec.md).
