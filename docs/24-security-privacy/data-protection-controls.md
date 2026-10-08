# Data protection controls

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (technical) / CONDITIONAL (organisational) |
| Evidence sources | tests/test_security_suite.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Control | Status |
|---|---|
| Data classification (public, internal, personal, sensitive-location) | proposed in this document; applied in policy via masked/forbidden fields |
| Encryption in transit | platform TLS, not implemented in repo (ASM, OQ-01) |
| Encryption at rest | platform (ASM) |
| Access control | policy engine, tested |
| Masking | field override, tested |
| Minimisation for AI | allow-list, tested |
| Log hygiene | ids and statuses only; no token, no secret, no location (tested for secrets in OpenAPI/metrics/ready) |
| Backups | verified in N3 (restore test) |
| Deletion / retention | not implemented (P-06, P-07) |
| Test data | synthetic only; poisoned test rows are constructed and kept in `/tmp`, not committed |
