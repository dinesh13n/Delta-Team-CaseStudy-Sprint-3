# Cost Scenarios

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
- Events carry `cost_units`: total 6,735.29 over 3,000 events, mean 2.245, p95 4.276 (EVD-A-06). The unit and currency are not defined [UNK].
- Mapping cost to a shipment is impossible: events lack a shipment identifier.

## 2. Token cost model (formula, no prices)
Cost per request = (T_in x P_in + T_out x P_out) / 1,000,000, where prices P are per-million-token rates of a chosen model. [UNK] P_in, P_out (OQ-02). No price is assumed here.

## 3. Relative scale by scenario [ASM]
| Scenario | Tokens per period at 1x (354 requests, typical) | At 10x | At 100x |
|---|---|---|---|
| S3 GenAI | 906,948 | 9,069,480 | 90,694,800 |
| S3 with 1 retry on 10% | 997,643 | 9,976,430 | 99,764,300 |
| S4 agentic (5 steps) | 4,534,740 | 45,347,400 | 453,474,000 |
| S1 / S2 | 0 model tokens | 0 | 0 |

(Computed as requests x 2,562; the 1x row is close to the dataset sum 904,432.)
