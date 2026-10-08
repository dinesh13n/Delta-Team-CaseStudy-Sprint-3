# Security specification

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | openapi.yaml; schemas/; docs/09-initial-prd; docs/10-architecture; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; open items in docs/12-specs/spec-readiness.md |
| Residual risks | Specs are PROVISIONAL until OQ-01/02/03/05/11 are ruled |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. Identity: bearer JWT, HS256 with secret from environment (dev) or JWKS (ADR-0004). Claims: sub, role, tenant, exp. Clock skew 60 s. The `X-User-Role` header is ignored.
2. Authorisation: persona x entity x field x purpose from `access-semantics.yaml`; deny by default; Rego generated from the same YAML with a parity test (ADR-0005).
3. Secrets: environment only; start-up fails outside local mode if missing; secret scan in CI and pre-commit (closes F-09..F-14 in H).
4. AI: allow-listed context, untrusted text delimited, output schema-validated, no tool or action execution, human approval record, rate limit.
5. Audit: tamper-evident chain; `/audit/verify`.
6. Input: strict patterns on ids; request size limit 64 KiB; no file upload.
7. Transport: TLS terminates at the platform (deployment-neutral); HSTS at the edge [ASM].
8. Logging: no tokens, no secrets, no raw prompts with personal data.
Threat model update: Stage M.
