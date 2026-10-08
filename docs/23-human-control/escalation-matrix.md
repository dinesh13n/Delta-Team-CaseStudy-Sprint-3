# Escalation matrix

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | apps/api/metrics.py |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Trigger | First responder (role) | Escalate to (role) | Time target |
|---|---|---|---|
| Audit chain invalid | platform auditor | security owner, then incident commander | immediate |
| Forbidden-field value in an AI output (guardrail blocked count rising) | AI governance owner | security owner | same day |
| Quarantine ratio above threshold | data owner | business owner | next business day |
| Carrier saga failures above threshold | integration owner | carrier manager | same day |
| AI fallback rate above threshold for 1 h | platform on-call | AI governance owner | 1 h |
| Suspected token forgery (repeated `auth.denied`) | security on-call | security owner | 1 h |

[VF] The triggers map to metrics that exist (`/metrics`: `policy_denied_total`, `ai_fallback_total`, `ai_guardrail_blocked_total`, `http_requests_total`) or to endpoints that exist (`/audit/verify`).
[UNK] Role holders, contact paths and time targets are proposals: no named person or on-call system exists (OQ-05). This document is CONDITIONAL on those being filled in.
