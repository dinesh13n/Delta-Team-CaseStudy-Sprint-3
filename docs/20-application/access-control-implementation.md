# Access control implementation

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H4/J4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS; scope narrowing not enforceable |
| Evidence sources | EVD-H-04 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Request path: bearer token -> `Hs256Verifier` -> `Claims(subject, role, tenant, purpose)` -> `PolicyEngine.decide(persona, entity, action, purpose)` -> `filter_row` (mask `***` / drop) -> audit event with the decision id.
- Default deny; unknown persona or entity is denied (403).
- 8 personas from `semantic-layer/access-semantics.yaml`; `clinician` (foreign persona) is absent (F-19).
- Generated Rego (`policy/opa/access.rego`) is checked for currency in `make smoke` and for full-grid parity with the Python engine (OPA 1.21.1 run in H4).
- Platform roles `ops` and `auditor` are an [ASM] outside the persona matrix (DEBT / OQ-05).
- Scope-narrowed personas: the engine reports the scope but cannot enforce it (no hub/fleet attribute in data): `scope_enforced=false` is returned in decisions and recorded in the audit event.
Evidence: EVD-H-04 (16 negative tests, allow/deny matrix CSV).
