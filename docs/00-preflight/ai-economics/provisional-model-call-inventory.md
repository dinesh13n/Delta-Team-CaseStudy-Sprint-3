# Provisional Model Call Inventory

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

| Call | Trigger | Location | Status |
|---|---|---|---|
| Record summary and recommendation | `POST /ai/summarize/{id}` | `apps/api/services/ai_gateway.py` | Simulated (no provider call) |
| ETA prediction | none | none | Declared, absent |
| Route optimisation | none | none | Declared, absent |
| Exception copilot | none | none | Declared, absent |

- [M] Models in the dataset: the `model` column holds 14 distinct non-model words (for example `approved`, `manual`, `standard`) and 1 blank; no real model identifier exists. The code constant is `local-sim-v1`.
- [UNK] Real provider, model name and price (OQ-02).
- Provisional inventory for design: 1 live-call site, up to 3 declared.
