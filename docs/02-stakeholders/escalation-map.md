# Escalation Map

| Field | Value |
|---|---|
| Stage | B: Stakeholders (Spine 2) |
| Runbook step | B2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md; docs/01-engagement/* |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-05 |
| Residual risks | No independent approver exists |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Trigger | First contact | Then |
|---|---|---|
| Stop condition hit | Operator | CTO |
| Blocking open question needed by next step | Operator | Role owner when named; else default applied and logged |
| Security finding with real credential | Operator immediately | Security Owner |
| Disagreement with a runbook claim | Operator (approve correction) | log in decision-log |
