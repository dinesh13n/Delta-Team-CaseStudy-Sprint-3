# Authentication map

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Inbound: bearer JWT (HS256 now; RS256/JWKS later, stub fails closed). Outbound to model/carrier: none live; when added, per-environment credentials from a secret store, never from the repo (secrets-hardening.md). Dev tokens: `scripts/issue_dev_token.py`, refused unless `APP_ENV=local`.
