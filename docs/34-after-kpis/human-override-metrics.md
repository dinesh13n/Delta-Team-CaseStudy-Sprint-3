# Human override metrics

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT MEASURABLE (no real reviewers) |
| Evidence sources | apps/api/main.py; docs/23-human-control |
| Assumptions | See body |
| Unresolved issues | reviewers |
| Residual risks | HC-R-01, HC-R-03 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Override = a reviewer rejects or changes a suggestion. The system records approve and reject decisions (`ai_decisions_total`, `ai.decision` audit, approval store), so the metric is computable once reviewers exist. Today the only decisions are from tests and the author-run simulations; counting them would be fabrication.

Design points the data will show: self-approval is allowed (HC-R-01); there is no approval expiry (HC-R-03); the dashboard panel "Human decisions" and alert `AiSuggestionsRejectedHigh` read this metric.
