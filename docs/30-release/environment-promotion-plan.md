# Environment promotion plan

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (design only) |
| Evidence sources | apps/api/config.py; tests/test_security_suite.py |
| Assumptions | See body |
| Unresolved issues | OQ-01; staging data policy |
| Residual risks | N-R-09 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Environment | Purpose | Data | Identity | AI | Exists? |
|---|---|---|---|---|---|
| local | developer, CI | synthetic fixture | HS256 dev tokens, `legacy_header` allowed | deterministic | **yes** (the only one ever run) |
| test | integration, TEVV re-runs | synthetic | HS256 with per-env secret | deterministic or candidate model | no |
| staging | pre-production rehearsal, restore drill | synthetic or masked copy [UNK: owner decision] | IdP test tenant | as production | no |
| production | real operations | real | IdP, asymmetric keys | per go/no-go | no |

## Promotion rules
- The same image digest moves forward; configuration differs only by environment variables (no rebuild per environment).
- `APP_ENV` other than `local` forces: no `legacy_header`, no ephemeral secret, docs/openapi off, secret ≥ 32 chars. Start-up fails otherwise (tested).
- Promotion from test to staging needs CI green and the evaluation suite at thresholds; staging to production needs go/no-go.
- Data is never promoted between environments by copying audit logs.
