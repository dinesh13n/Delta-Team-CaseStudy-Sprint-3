# Workload Assumptions

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

## 1. Where AI exists today
- [M] One AI touchpoint in code: `POST /ai/summarize/{record_id}` -> `ai_gateway.summarize_record` (simulated; no model call; `time.sleep(0.01)`). Declared but absent: ETA prediction, route optimisation, exception copilot (`docs/architecture/current-state.md`).
- [M] The code's token figure is `len(prompt.split()) * 2`, an estimator, not a measurement (`ai_gateway.py` line 10).
- [M] Dataset: 354 `ai_invocations` rows (one has a blank `token_count`), 505 events whose entity is `ai_invocations`, 356 events by actor `ai_agent`.

## 2. Assumptions
| ID | Assumption |
|---|---|
| ASM-W1 | AI would assist exception investigation (flow 4) first, because it is the only flow with an AI endpoint |
| ASM-W2 | A request is one record summarised or one recommendation produced |
| ASM-W3 | The period covered by the fixture is unknown, so no per-day rate is derived |
| ASM-W4 | Human review remains in the loop (code returns "Review and approve before action") |

## 3. Unknowns
- [UNK] Real request volume, peak/average ratio, users and period (UNK-7 in assumptions-unknowns.md).
- [UNK] Which of the three declared capabilities would be built (OQ-18, OQ-06).
