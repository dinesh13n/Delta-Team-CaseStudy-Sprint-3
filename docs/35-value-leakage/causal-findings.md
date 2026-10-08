# Causal findings

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/26-tevv; evidence/31-observability |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Finding | Cause | Strength |
|---|---|---|
| 10 of 12 attacks succeeded on baseline, 0 on v2 | specific code changes (token verification, policy, guardrails, rate limit) | strong: same attacks, both builds |
| Actor and correlation present on 10 of 10 audit events | the audit v2 writer | strong, by construction |
| Past edit detected | hash chain | strong, tested |
| K1 to K8 unchanged | none acted on them | trivial |
| Business outcome effect | unknown | none: not measurable |
