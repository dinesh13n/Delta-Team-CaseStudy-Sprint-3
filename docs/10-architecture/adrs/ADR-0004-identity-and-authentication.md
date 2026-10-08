# ADR-0004: Verified identity via signed bearer tokens (resolves OQ-07 provisionally)

| Field | Value |
|---|---|
| Stage | F: Target Architecture, Data and Context Strategy, Specs, Traceability (Spine 10) |
| Runbook step | F1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/09-initial-prd/; docs/06-root-cause/; docs/07-repo-assessment/; semantic-layer/access-semantics.yaml; subtree docs/architecture/target-state-principles.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- **Status:** Proposed, PROVISIONAL (owner UNRESOLVED)
- **Date:** 2026-10-08
- **Context:** Role comes from a header the caller sets (F-17); no identity provider is chosen (OQ-07).
- **Decision:** Bearer JWT with claims sub, persona, tenant and allowed purposes. Verification sits behind a TokenVerifier port: HS256 with an environment secret for local and tests; RS256 against an OIDC JWKS for a real provider (configuration only). Header role is removed. No provider is assumed.
- **Consequences:** Real IdP connection is a deployment step (BLOCKED until OQ-07 owner names one).
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
