# Support model

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (proposed tiers) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Tier | Who | Handles | Out of hours |
|---|---|---|---|
| 1 | service desk / operations (UNRESOLVED) | "I cannot sign in", "the page is empty" → check `/ready`, data freshness | none defined |
| 2 | SRE / Dev (UNRESOLVED) | alerts, restarts, kill switch, restore | none defined |
| 3 | Dev lead + domain owner | code and data defects | none |
| Security | Security Owner | AUTH denials, leak alerts | page severity only |
Response targets: **none set** (no SLA). Pager and rota: none.
