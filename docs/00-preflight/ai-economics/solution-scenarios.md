# Solution Scenarios

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

Four ways to deliver the exception-summary and recommendation capability. No scenario is recommended here.

| Scenario | What it is | Cost driver | Latency driver | Evidence basis |
|---|---|---|---|---|
| S1 Deterministic software | Rules and templates over the CSV/event data | engineering time | milliseconds, in-process | current code returns a templated string |
| S2 Conventional automation | Scheduled batch plus rules/statistical scoring (ETL already exists) | engineering and compute | batch window | `etl/run_daily_batch.py` |
| S3 GenAI assist | One model call per record, human approves | tokens per call x volume | model latency plus network | dataset tokens/call; [ASM] model unknown |
| S4 Agentic AI | Multi-step tool use and loops | tokens x steps x retries | sum of step latencies | no evidence; OQ-18 excludes by default |

- [ASM] S4 is out of scope until OQ-18 is answered.
- [UNK] Accuracy of any scenario: no labelled outcomes exist in the fixture (the `human_override` column holds mixed non-boolean values).
