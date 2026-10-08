# Preliminary FinOps Baseline

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

- [M] Current spend: none attributable; the AI path is simulated, so real model cost today is 0.
- [M] Dataset-declared consumption: 904,432 tokens over 353 invocations; 6,735.29 cost units over 3,000 events.
- [M] `ai_gateway.py` reports `token_estimate` that is a word count x 2; it is not recorded anywhere (audit log omits tokens).
- Gaps [UNK]: tags or owners for cost, budgets, unit of `cost_units`, billing source.
- Baseline to carry forward (frozen in Stage C): tokens/call distribution, events per `business_entity`, cost_units per event.
