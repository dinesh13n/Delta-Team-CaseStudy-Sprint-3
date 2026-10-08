# Feature flag plan

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/10-architecture; docs/11-data-context; docs/12-specs |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; platform OQ-01 |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Flag | Env var | Values | Default | Controls | Rollback |
|---|---|---|---|---|---|
| FF-01 | AUTH_MODE | hs256, jwks, legacy_header | hs256 | H4 identity. legacy_header allowed ONLY when APP_ENV=local (it is the vulnerability F-17) | set legacy_header locally only; in non-local environments rollback = redeploy previous tag |
| FF-02 | LOOKUP_MODE | exact, legacy | exact | H5 | set legacy for comparison; incident rollback = redeploy previous tag |
| FF-03 | DATA_LAYER | curated, fixture | curated | H6 | set fixture |
| FF-04 | AI_PROVIDER | deterministic, model | deterministic | H7 | set deterministic |
| FF-05 | AI_GUARDRAILS | enforce | enforce (not switchable off outside tests) | H7 | n/a, by design |
| FF-06 | ~~AUDIT_VERSION~~ | WITHDRAWN (N3, D-013) | n/a | there is no v1 audit writer in the new code, so no switch exists; the flag was planned in G and never built | rollback = redeploy previous tag; the v1 format is not producible |
| FF-07 | AI_ENABLED | true, false | true | kill switch for the AI endpoint (returns 503) | set false |
| FF-08 | DATA_MAX_AGE_S | seconds, 0 = off | 0 (off) | M3: `/ready` reports `data_fresh` when > 0 | set 0 |
| FF-09 | AI_PROVIDER_TIMEOUT_S, AI_BREAKER_THRESHOLD, AI_BREAKER_RESET_S | numbers | 5, 5, 30 | M2 resilience tuning | restore defaults |
| FF-10 | AI_RATE_PER_MINUTE | integer per subject | 30 | M1 | raise or lower; restart required |
Deliberate behaviour changes: H4 (FF-01), H5 (FF-02), H6 (FF-03), H7 (FF-04/05/07), H8 (FF-06). Each has a rollback in `rollback-strategy.md`. Flags are read once at start-up and logged.


## N3 amendment (2026-10-08)
FF-06 withdrawn; FF-08..FF-10 added for flags introduced in M. All flags are environment variables read at start-up: a change needs a restart. No runtime flag service exists. See docs/30-release/feature-flag-plan.md for the release view.
