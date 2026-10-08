# Token Flow Scenarios

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

## 1. Measured per-invocation tokens [M] (EVD-A-06)
353 parsed rows: sum 904,432; mean 2,562; p50 2,618; p95 4,795; min 40; max 4,989; none above 16,000. The CSV gives one `token_count` with no input/output split. [UNK] split.

## 2. Flow per scenario (S3 GenAI, single call)
`record -> prompt build -> model -> summary -> human review`.
Tokens per request: T = T_in + T_out with T from 2,562 mean (range 40 to 4,989). [ASM] T_out is a minority share; share unknown.

## 3. Sensitivity (illustrative, ASM)
| Case | Tokens per request | Basis |
|---|---|---|
| Low | 40 | dataset min |
| Typical | 2,562 | dataset mean |
| High | 4,989 | dataset max |
| High with one retry | 9,978 | ASM: 1 retry doubles the call |

## 4. Agentic S4 multiplier
[ASM] N steps x per-step tokens; for N=5 at typical, 12,810 per request. Not evidence, only arithmetic; no loops exist today.
