# Responsible AI controls

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | docs/25-governance/model-card.md, system-card.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Principle | Control | Evidence | Gap |
|---|---|---|---|
| Human oversight | every suggestion needs a human decision | K1 | no four-eyes |
| Transparency | `generated_by`, `model`, `prompt_version`, `config_hash`, `token_source`, label "approval required" in the view | gateway, view | none |
| Accuracy and grounding | facts only from the record; `unsupported_claim_rate` 0.0 | eval | real model untested |
| Fairness | the summary has no personal attributes; inputs are operational | design | no bias evaluation (not meaningful on this data) |
| Privacy | minimisation, masking | PIA | retention open |
| Robustness | fallback, breaker, timeout | M2 | real failures untested |
| Accountability | audit chain with actor and approval id | K1 | owners unnamed |
| Contestability | a user can reject any suggestion | K1 | rejection reason not analysed |
| Misuse prevention | rate limit, persona limits | K2 | |
