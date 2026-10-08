# Model B build notes

Scope built: the four behaviours in BUILD-BRIEF.md (record lookup, identity and policy, AI summary with guardrail, hash-chained audit), plus /health and /ready and /openapi.json.

## Files read (bundle only)
Directory: `scratchpad/q1/bundle/`. Files read:
- BUILD-BRIEF.md
- docs/17-implementation-prd/: all eight files (implementation-prd, release-boundaries, prioritized-capabilities, finalized-acceptance-criteria, finalized-nfrs, invalidated-assumptions, prd-change-log, implementation-baseline-signoff)
- docs/12-specs/: system-spec, api-contracts.md, api-contracts/openapi.yaml, features/FEAT-01..FEAT-06, security-spec, error-handling-spec, schema-specifications, event-contracts, interface-contracts, nfr-spec, acceptance-criteria, business-rules, observability-spec, spec-readiness, schemas/ai-summary-output.schema.json, schemas/audit-event.schema.json
- docs/19-intelligence/prompt-registry.md
- semantic-layer/: README, entities.yaml, relationships.yaml, enum-violations.md, business-rules.yaml, status-taxonomy.yaml, access-semantics.yaml, ai-context-policy.yaml, glossary.md, metrics.yaml (first 80 lines only)
- data/curated/*.csv (headers, row counts, and aggregate checks through Python)

Not read: semantic-layer/generated/, semantic-layer/schemas/, semantic-layer/tests/ (none present in bundle listing beyond these). Nothing outside the bundle, the build directory and the installed packages was read. Copies of the bundle's data, contract and policy files were made into the build directory (`data/`, `semantic-layer/`, `app/contract/`). `app/prompts/exception_summary_v1.txt` is my own text, not the registry file.

## Ambiguities and decisions
1. **Purpose on record lookup.** Spec does not say how purpose is supplied. Decision: optional `purpose` query parameter (validated as `[a-z_]+`, otherwise 422). Default is the persona's first declared purpose for `shipments`. Policy then denies if the purpose is not declared for the persona.
2. **Who may summarise.** `exception_summary` is declared only for `ai_agent` in access-semantics. So only an `ai_agent` token gets 200 from POST /ai/summarize; human personas get 403. This is a product gap: human reviewers cannot request a summary.
3. **Who may approve.** The approver is the persona with `write` on `shipments` (dispatcher), per ai-context-policy `approver`. The OpenAPI "reviewer role" is not a persona, so I mapped it this way.
4. **Scope narrowing.** Not enforced (IA-6). Scope is not a decision dimension in the brief, so scoped personas are allowed with the audit detail `scope_enforced: false`. This is a real over-exposure risk (for example, warehouse_ops reads all shipments). Recorded, not fixed.
5. **Field decisions.** `allow` returns the value; `mask` returns `"***"`; `deny` omits the field. Sensitive fields with no override default to `mask`. Non-sensitive fields default to `allow`.
6. **Entity denial.** Persona not in the file, entity not declared, access not sufficient, or purpose not declared: all 403, audited with the rule id `access-semantics:<persona>/<entity>/<action>` (or `persona.unknown`).
7. **Audit on failure.** Spec says fail-closed for write actions and "[ASM] logs" for read actions. I chose fail-closed for every audited action: a failed audit write returns 503.
8. **Audit actions and denials.** Action names are `record.read`, `ai.summarize`, `ai.decision`, `auth.denied`, `audit.verify`. A denial keeps the action and sets `policy_decision.decision=deny` and `outcome=denied`, since AC-07 asks for decision and rule id, not a `.denied` suffix.
9. **404 audit.** Not-found is audited with `outcome: error` and `detail.reason: not_found`. The error-handling table says "not logged as error"; I read that as a log-level rule, not an audit rule.
10. **422 vs 401 order.** Pipeline order is auth then shape then policy, per system-spec. A missing token with a bad id gives 401. A valid token with a bad id gives 422 and no audit (per error-handling).
11. **Audit hash.** `hash = sha256(canonical_json(event minus hash) + prev_hash)`, canonical = sorted keys, compact separators, UTF-8. Genesis prev is 64 zeros. `first_bad_index` is 0-based. A corrupt tail at start-up is reported by verify; new writes chain from the last parseable hash or genesis.
12. **Audit tenant.** Taken from the token `tenant` claim (required, non-empty). Anonymous events use `default`.
13. **Token rules.** HS256 only, `exp`/`sub`/`role`/`tenant` required, 60 s leeway. `AUTH_MODE=jwks` is accepted but fails closed (every token rejected). `X-User-Role` is never read.
14. **AUTH_SECRET.** Missing and `APP_ENV=local`: an ephemeral random secret is generated (tokens do not survive restart). Missing and not local: `ConfigError`, so uvicorn does not start. Set and shorter than 32 characters: refused in any environment.
15. **Rate limit.** 30 per minute per token subject (error-handling [ASM]), sliding window, in memory. Exceeded: 429 with `Retry-After: 60`, audited. The limiter lives in the HTTP layer only, so `summarize_case` is not rate-limited (the harness may call it many times).
16. **Suggestion store.** Each generated suggestion (including abstentions) is written to APPROVALS_PATH as a `suggestion` line; decisions as `decision` lines. The approval record has `approval_id`, which also appears in the audit event. Decision is audited before it is stored, under one lock; a second decision returns 409 and is not audited.
17. **Data.** Curated CSVs are read once and cached; a failed load is not cached, so /ready recovers when the file reappears. Lookup is an exact dictionary match on `shipment_id`. Duplicate keys: first row wins (none exist in the fixture). Rows with `data_quality_flags` are returned with a `data_quality_flags` list. `load_id` and `source_row` are not returned.
18. **Out-of-domain values.** Shipment, booking and event values outside the declared domain are returned as-is in the record lookup (the flag is shown). They are never replaced. In the AI context they are dropped, not replaced. Legacy `approved` status is accepted and flagged (status-taxonomy legacy_tolerance).
19. **AI context.** Built only from ai-context-policy `allowed_fields`, minus `forbidden_fields`, and only where the ai_agent field decision is `allow`. Customer, driver and location fields never enter the prompt. Event and booking ids appear only in `sources`. Strings are stripped of control characters, capped at 200 characters, and template syntax (`{{`, `{%`, `${`, `__x__`) is replaced by `[removed]`. `<` and `>` are escaped to `<`/`>` in the data block. Events are sorted by `sequence_no`, the newest 20 kept, and the oldest dropped first if the 8000-token estimate is exceeded (estimate = characters / 4).
20. **Abstention.** Insufficient context (blank shipment_id, status or promised_at; or no events and no bookings) abstains before any provider call. Conflict (more than one active booking, BR-05) abstains with `low_confidence`, because the enum has no conflict reason. The model may also abstain by returning `abstain_reason`.
21. **Model output guardrail.** Model output must parse as one JSON object with exactly summary, recommendation, confidence (optional abstain_reason), match the schema, and pass: no `<`/`>`, no template syntax, no control characters, no "ignore previous instructions", no action-claim words (executed, auto-approved, rebooked, cancelled, dispatched, rerouted), no `CUS-`/`DRI-` identifiers, no raw customer_id. Failure reasons: `schema_violation`, `guardrail_blocked` (guardrail_status `blocked`), `low_confidence` (below 0.5, ASSUMPTION), `provider_unavailable` (ConnectionError), `provider_error` (any other exception).
22. **Fallback and generated_by.** Model success: `generated_by=model`. Any fallback: `generated_by=fallback` with `fallback_reason`, using the deterministic provider. Deterministic default: `generated_by=deterministic`. guardrail_status is `enforced` whenever output is generated and checked, `blocked` when model output was rejected by the guardrail, and `not_applicable` for pre-generation abstention.
23. **Deterministic failure.** The spec says "abstention or 503". I return 200 with `abstain_reason: provider_unavailable` if the deterministic provider itself fails. The HTTP layer returns 500 if the final body fails schema validation (internal fault). No 503 is raised from the AI path; 503 is used for data-layer, audit-write and approval-store failures.
24. **Confidence.** Deterministic: 0.9 minus penalties (0.15 invalid service tier, 0.10 legacy status, 0.05 per invalid event type up to 0.30, 0.05 per legacy booking status up to 0.10). Real provider confidence is used as given.
25. **Token numbers.** `token_estimate` = ceil(chars/4) of prompt plus data. `token_source` is always `estimate` (the provider interface returns text only).
26. **Prompt and config hash.** Prompt text is my own `exception_summary_v1.txt`. Its SHA-256 differs from the registry value (96b454...), and so does `config_hash` (registry value b397c28d... for the deterministic provider is not reproduced). Recorded because the registry file content was not in the bundle.
27. **Summary text.** The deterministic summary uses only validated enum values, ids, timestamps and counts. It states that no action has been taken. The recommendation is a referral to the dispatcher, never an action.
28. **Health and ready.** /health returns only `{"status":"ok"}`. /ready checks data loadability, semantic layer loadability, signing key length, and audit directory writability (it creates the directory if missing). Failure: 503 problem+json.
29. **OpenAPI.** /openapi.json serves the bundle's `openapi.yaml` (copy in `app/contract/`) as JSON. It is equal to the contract by construction, not generated from routes.
30. **Problem bodies.** `type` is `urn:logistics:problem:<slug>`. Unknown routes return problem+json 404.
31. **Request size.** A `Content-Length` above 64 KiB returns 413. Chunked bodies without Content-Length are not size-limited (not handled).
32. **Correlation id.** Incoming `X-Correlation-ID` accepted if 8 to 128 characters of `[A-Za-z0-9._:-]`, else a generated 32-hex id. Echoed on every response and written to the audit event and the JSON request log line.

## Not implemented
- GET /metrics, GET /shipments, GET /shipments/{id}/events, GET /kpis (not in the four-behaviour subset).
- JWKS verifier (fail-closed stub only).
- Real model provider (none called; deterministic default and fallback only).
- Carrier booking saga, ETL/intake and quarantine, thin operations view.
- Runtime validation of audit events against audit-event.schema.json (the schema is copied but not checked at write time).
- Scope enforcement (see decision 4).
- Multi-tenancy (tenant claim is stored, not used for filtering).
- Audit for 422 and 409 (by spec design).
- Log redaction beyond not logging tokens.

## Tests
`tests/` (pytest): 32 tests passing in `python -m pytest` from the build directory. They cover lookup, masking, 401/403/404/422, header forgery, token rules, purpose denial, correlation ids, audit chain and tamper detection, schema-valid summaries, schema-valid fallbacks for each failure mode, injection and template handling, abstention, approval 409, rate limit, and start refusal. A sweep of all 349 curated shipments through `summarize_case` gave schema-valid output for every row (all deterministic, none abstained).
