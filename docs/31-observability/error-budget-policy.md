# Error budget policy

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (proposed; no owner) |
| Evidence sources | See body |
| Assumptions | [ASM] 30-day window and thresholds |
| Unresolved issues | owner not named |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Based on the proposed 99.5% availability SLO over 30 days: budget = 0.5% of requests, about 3.6 hours of full outage equivalent. [INF]

| Budget consumed | Action (proposed) |
|---|---|
| < 50% | normal delivery |
| 50% to 100% | reliability work first; changes limited to fixes and hardening |
| ≥ 100% | release freeze except fixes for the cause; written review within 5 working days |

AI safety and audit integrity have **no budget**: any breach is an incident (incident-severity-matrix), not a budget draw.

## Conditions
- The policy only means something when an owner can freeze releases. No owner is named (OQ-05, RACI in P stage).
- With one process and a static fixture, the budget cannot be burned by real traffic; the table is a template for production.
