# AI-disabled mode

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (M-X4) |
| Evidence sources | evidence/28-resilience/EVD-M-03-drills/drill-2-ai-gateway-timeout.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Specification.** `AI_ENABLED=false` removes the AI capability only. `POST /ai/summarize/{id}` returns 503 problem+json "AI disabled"; `/records`, `/shipments`, `/shipments/{id}/events`, `/kpis`, `/ready`, `/health`, `/metrics`, `/audit/verify`, the decision route for existing suggestions, and the operations view all continue. The operations view shows the 503 message instead of a suggestion.
**Why it is safe.** No business step depends on an AI output: the AI is advice, never a gate (K1 D-06, D-09).
**How to switch.** Set the variable and restart (no hot reload).
**Demonstration.** Drill 2, phase 4: AI 503, core endpoints 200 (`drill-2-ai-gateway-timeout.json`), and `tests/test_resilience.py::test_ai_disabled_mode_keeps_the_core_workflow`.
**Business view.** Dispatchers lose the summary and the suggested next step; they keep the record, the event list and KPIs, which are what they used before the transformation.
