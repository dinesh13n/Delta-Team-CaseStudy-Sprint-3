# Identity and access control

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/09-initial-prd/functional-requirements.md; openapi.yaml |
| Assumptions | See body |
| Unresolved issues | See spec-readiness.md |
| Residual risks | Provisional |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Behaviour.** Verify the bearer token, derive persona from the `role` claim, evaluate the policy for (persona, entity, field, purpose). Allowed fields are returned, masked fields are replaced by `"***"`, denied entities return 403. Unknown persona -> deny. Every decision is audited with the rule id.
**Configuration.** `AUTH_MODE=hs256|jwks`, `AUTH_SECRET` (required unless `APP_ENV=local`), `AUTH_JWKS_URL`.
**State.** Stateless.

**Requirements.** FR-03, FR-04, FR-05, FR-19. **Findings addressed.** F-17, F-18, F-19, F-20, F-21. **Acceptance criteria.** see `../acceptance-criteria.md`.
