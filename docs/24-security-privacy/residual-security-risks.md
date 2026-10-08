# Residual security risks

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | threat-model.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Risk | Severity | Owner (role) | Decision |
|---|---|---|---|---|
| R-SEC-01 | HS256 shared secret: any holder mints any persona; JWKS verifier is a fail-closed stub | High | Security owner | accepted for pilot; fix = IdP (OQ-07) |
| R-SEC-02 | secrets exposed in git history (F-09..F-12, baseline tags) | Low (synthetic) | Security owner | accepted; **rotate**; history preserved by decision (OQ-19) |
| R-SEC-03 | rate limit in memory, per process | Low | Platform | accepted |
| R-SEC-04 | purpose defaulting | Medium | Security owner | accepted; fix = require purpose |
| R-SEC-05 | chunked body cap absent | Low | Platform | accepted; proxy limit |
| R-SEC-06 | no TLS/at-rest evidence (no platform) | High | Platform | OPEN (OQ-01) |
| R-SEC-07 | real-model injection behaviour untested | High if enabled | AI governance owner | OPEN (OQ-02) |
| R-SEC-08 | CI and branch protection unproven | Medium | Repo owner | OPEN |
| R-SEC-09 | no independent security review | Medium | Security owner | OPEN |
| R-SEC-10 | stale_gps cannot be detected | Medium | Data owner | OPEN |
