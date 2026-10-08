# Adoption metrics

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT MEASURABLE (no users) |
| Evidence sources | docs/31-observability/ai-telemetry-spec.md |
| Assumptions | See body |
| Unresolved issues | users |
| Residual risks | O-R-02 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Adoption of the AI suggestion, the dashboards, or the API by operations staff: **zero real users, so no adoption data exists.** The audit trail would carry it (`ai.summary` and `ai.decision` events by actor); the table below is what will be read from it. [VF] for the gap.

| Metric | Source | Value |
|---|---|---|
| Distinct actors using the AI endpoint per week | audit `ai.summary` by subject | none (test subjects only) |
| Suggestions requested vs decided | `ai_requests_total` vs `ai_decisions_total` | no real decisions |
| Share of exceptions handled with a suggestion | needs case ids | not possible (no case id, cost-per-case.md) |
| Time from suggestion to decision | audit timestamps | test data only |

Tests and tabletop events must be filtered out of any future adoption count; they carry synthetic subjects (`alice`, `mallory`, `oncall`).
