# Functional Requirements

| Field | Value |
|---|---|
| Stage | E: Intervention Qualification and Initial PRD (Spine 9) |
| Runbook step | E3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/03-problem-value/; docs/08-ai-qualification/; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Requirement | Business req | Findings | Intervention | Success criterion |
|---|---|---|---|---|---|
| FR-01 | Return exactly the requested record by exact key, or 404 not-found; never another record | BR-1 | F-31,F-32 | I1 | SC-1 |
| FR-02 | Reject identifiers that do not match the entity key pattern, including cross-entity ids such as REC-0001 | BR-2 | F-30 | I1 | SC-2 |
| FR-03 | Require a verified identity (signed token) on every endpoint except liveness/readiness | BR-3 | F-17,F-19,F-20 | I2 | SC-3 |
| FR-04 | Decide access per persona, entity, field, purpose and scope from access-semantics; mask or deny sensitive fields | BR-3 | F-18,F-21,F-16 | I2 | SC-3 |
| FR-05 | Return 401 or 403 with a problem body on denial and audit the denial | BR-3,BR-4 | F-17,F-43 | I2,I6 | SC-3 |
| FR-06 | Validate intake against semantic rules, quarantine invalid rows with reasons, report counts, exit non-zero above a threshold | BR-5 | F-33..F-38,F-40,F-41 | I3 | SC-5 |
| FR-07 | Produce a versioned curated data layer from the immutable fixture; never edit the fixture | BR-5 | F-54 | I3 | SC-5 |
| FR-08 | Detect more than one active carrier booking per shipment at intake and report it | BR-5 | F-38 | I4 | SC-5 |
| FR-09 | Provide an exception summary for a shipment case with sources, confidence, model and prompt version, token count and cost | BR-6 | F-25,F-27,F-28,F-29 | I9 | SC-6 |
| FR-10 | Build prompts only from allow-listed fields; treat free text as delimited data; no template-injection | BR-6 | F-22,F-23 | I9 | SC-6 |
| FR-11 | Validate model output against a schema with an abstention path and a deterministic fallback | BR-6 | F-24,F-25 | I9 | SC-6 |
| FR-12 | Record a human approve or reject decision with an approval id before any suggestion is acted on | BR-6 | F-26 | I9 | SC-6 |
| FR-13 | Write audit events with actor, correlation id, tenant, resource, policy decision, model and prompt version, input hash, approval id into a tamper-evident chain | BR-4 | F-43,F-44,F-45 | I6 | SC-4 |
| FR-14 | Accept or generate a correlation id per request and carry it to audit records, logs and responses | BR-4 | F-42 | I6 | SC-4 |
| FR-15 | Expose liveness and readiness; readiness reflects the data layer | BR-8 | F-46 | I1 | SC-8 |
| FR-16 | Publish a complete OpenAPI contract for every endpoint | BR-8 | F-50 | all | SC-8 |
| FR-17 | Expose operational and AI metrics (requests, latency, tokens, cost) | BR-6 | F-46,F-28 | I9 | SC-6 |
| FR-18 | Provide a thin read-only operations view for record lookup and exception summary (OQ-06 ruling) | BR-1 | F-05 | I1,I9 | SC-1 |
| FR-19 | Load configuration and secrets from the environment; refuse to start with missing secrets outside local development | BR-7 | F-09..F-14 | I2 | SC-7 |
| FR-20 | Be installable and testable from a clean checkout with locked dependencies | BR-8 | F-02,F-03,F-04,F-07 | all | SC-8 |
