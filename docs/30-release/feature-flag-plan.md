# Release feature-flag plan

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (plan matches code) |
| Evidence sources | apps/api/config.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | restart-only flags mean a flag flip is a brief outage |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Flags are environment variables read at start-up (apps/api/config.py). No runtime flag service; a change needs a restart. The authoritative table is `docs/14-transformation/feature-flag-plan.md`, amended in N3.

| Flag | Release use |
|---|---|
| AI_ENABLED | kill switch; **off at first production deploy** |
| AI_PROVIDER | `deterministic` until TEVV passes on a candidate model |
| AUTH_MODE | `hs256` for pilot, `jwks` once an IdP exists (stub fails closed today) |
| LOOKUP_MODE, DATA_LAYER | defaults only; legacy values refused outside local |
| DATA_MAX_AGE_S | set to the ETL schedule + margin when a scheduler exists |
| AI_RATE_PER_MINUTE, AI_PROVIDER_TIMEOUT_S, AI_BREAKER_* | tuning, defaults tested |

**FF-06 AUDIT_VERSION is withdrawn (D-013):** the plan in G assumed a v1 audit writer could be kept; none exists in the new code, so the flag was never built and cannot be offered as a rollback. Rollback of audit format is a redeploy of the previous tag.
