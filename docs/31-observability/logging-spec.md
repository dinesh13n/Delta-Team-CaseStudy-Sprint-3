# Logging specification

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/main.py observe middleware; tests/test_security_suite.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-02 retention undefined |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Request log line (stdout, JSON) [VF]
| Field | Source | Sensitive? |
|---|---|---|
| ts | UTC ISO-8601 | no |
| level | INFO default (`LOG_LEVEL`) | no |
| route | route template, not the raw path (no record ids) | no |
| status | HTTP status | no |
| latency_ms | middleware timer | no |
| correlation_id | header or generated | no |
| actor_role | verified claim, `-` if unauthenticated | low |
| data_load_id | current published ETL run | no |

## Rules
- Request bodies, tokens, authorization headers, query strings and AI prompts are **never** logged. Test coverage: security suite asserts no token or secret in logs.
- Subject identity belongs in the audit record, not in the log, so log access does not need the audit's access control.
- Errors return RFC 7807 problem bodies without stack traces; unexpected exceptions return a generic 500 and are logged without payload.
- Log level `DEBUG` is not the default anywhere (F-13).

## Gaps
- Log retention, shipping, and who may read them: undecided (OQ-01).
- No log-based alerts. All alerts are metric-based.
- Because no subject appears in the log line, a log line alone cannot say who made a request; the correlation id links it to the audit record.
