# Identity and RBAC hardening

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (pilot) / CONDITIONAL (production) |
| Evidence sources | apps/api/security/*, tests/test_security_suite.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Item | State |
|---|---|
| Algorithm pinned to HS256; `alg=none` and tampered payloads rejected | tested |
| Secret length ≥ 32; missing secret fails start-up outside `local` | `config.validate` |
| Ephemeral secret generated in local mode only | `Services.__init__` |
| Required claims `exp`, `sub`, string non-empty `role`; unknown role denied | tested |
| Platform roles `ops` (metrics) and `auditor` (audit verify) do not imply data roles or each other | tested |
| Per-subject AI rate limit | tested |
| Purpose claim optional; **defaults to the first declared purpose** | RL-02 / R-SEC-04, accepted |
| JWKS / OIDC verifier | fail-closed stub: every token refused when `AUTH_MODE=jwks` (no IdP, OQ-07) |
| Token issuance | dev script, refuses unless `APP_ENV=local` |
| Token lifetime and revocation | default dev TTL 3600 s; no revocation list; no refresh |
| Service-to-service identity | none (no services) |

Production needs: IdP with asymmetric keys and key rotation, explicit purpose claims, short TTL, revocation strategy. These are not designed in detail because the IdP is undecided.
