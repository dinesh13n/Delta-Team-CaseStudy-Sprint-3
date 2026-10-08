# Quality, Latency and Cost Envelope

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0C provisional AI economics envelope |
| Runbook step | A6 (runbook/02-TRANSFORMATION-RUNBOOK.md, Stage A) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | **PROVISIONAL**, Draft; approvers UNRESOLVED (OQ-05) |
| Evidence sources | evidence/00-preflight/EVD-A-06-ai-economics-profile.json; data/synthetic/ai_invocations.csv; data/synthetic/events.jsonl; apps/api/services/ai_gateway.py |
| Assumptions | Marked ASM in text; none is a measurement |
| Unresolved issues | OQ-02 (models), OQ-08/09 (KPIs, financial data), OQ-12, OQ-18 |
| Residual risks | Fixture figures are synthetic and may not resemble production |

**[M]** measured in the fixture (dataset-declared, synthetic), **[ASM]** assumption, **[UNK]** unknown. This pack does not decide that AI is justified; that is Stage E.

## 1. Measured [M]
Event latency: min 15 ms, p50 1,667 ms, p95 13,707 ms (13,709 by index method), p99 14,774, max 14,999, mean 4,382 (EVD-A-06). These are fixture values, not a measured system, and latency is environment-dependent (A3).

## 2. Provisional constraints [ASM], PROVISIONAL
| Dimension | Constraint | Note |
|---|---|---|
| AI response latency, interactive | p95 <= 3,000 ms end to end | the fixture p95 is far above this |
| Non-AI API latency | p95 <= 500 ms | ASM |
| Cost per request | <= 2.25 cost units (fixture mean) until a currency is defined | [M] mean 2.245 |
| Cost per case | UNKNOWN: cases cannot be tied to cost from the data | UNK |
| Quality | no labelled outcomes exist; a quality metric must be defined in Stage E | UNK |
| Human review | required on every AI recommendation | code message |

## 3. Trade-off statement
Tighter latency and lower cost push towards S1/S2; richer summaries push towards S3. The envelope fixes the limits only; the choice is Stage E.
