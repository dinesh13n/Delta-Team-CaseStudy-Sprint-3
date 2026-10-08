# Human-on-the-loop workflow

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (design) / partly measured |
| Evidence sources | evidence/21-integration/EVD-J-05-saga-simulation.json, evidence/28-resilience/EVD-M-02-resilience-tests.txt |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Human-on-the-loop applies to **automated deterministic flows** that run without a person per item: the daily ETL batch, the carrier saga and the KPI computation.

| Flow | What the human watches | Intervention |
|---|---|---|
| Daily ETL | quarantine ratio (baseline 1.41 %, 30 of 2124 rows) | owner reviews `data/quarantine/*.csv`; threshold alert in N1 |
| Carrier saga | failed bookings, duplicate suppression count, retries at ceiling | failed bookings land in a queue for a person (simulation: 38 of 1000 failed, 0 multi-bookings) |
| AI gateway | fallback rate, guardrail-blocked count, circuit state | switch `AI_ENABLED=false`; the core workflow continues (tested) |
| Audit chain | `GET /audit/verify` valid | platform auditor runs it on a schedule |

[ASM] The alert thresholds are proposals (observability-spec) and have never fired in a real environment.
[VF] The kill switch and the degradation to the deterministic provider are tested (`test_resilience.py`).
