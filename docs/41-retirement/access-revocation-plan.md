# Access revocation plan

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (plan) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Remove: human access to the repository and platform, service accounts, CI tokens, the HS256 signing secret (rotate = all sessions end), `ops` and `auditor` scrape/verify credentials, IdP application registration (when one exists), backup storage access. Record each revocation with time and operator. After revocation, verify refusal (a token signed with the old secret returns 401).
