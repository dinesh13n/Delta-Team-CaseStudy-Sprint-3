# Volume Assumptions

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

| Quantity | Value | Class |
|---|---|---|
| Records in fixture per entity | 354 (351 unique ids per file after duplicates) | [M] |
| AI invocations in fixture | 354 | [M] |
| Events in fixture | 3,000 | [M] |
| Time span of the fixture | unknown; `tracking_events.event_time` and `promised_at` contain impossible values | [UNK] |
| Production request rate | unknown | [UNK] |

Scenario multipliers for planning only [ASM]: 1x (354 per period), 10x, 100x. No claim is made about which applies. Events carry no `shipment_id` ([M], field list in EVD-A-06), so cost cannot be attributed per shipment from this data.
