# Threat model (STRIDE + MAESTRO)

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | docs/architecture/known-gaps.md, security/threat-model.md, test list |
| Assumptions | See body |
| Unresolved issues | stale_gps (no timestamp), ETL BR-04 override, BR-06 override |
| Residual risks | see residual-security-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Model of the system **as built** (after H4, H7, H8): modular monolith, FastAPI, HS256 bearer tokens, policy engine, curated and quarantine data, AI gateway (suggest-only), hash-chained audit, static operations view.

## Part 1. The six declared brownfield gaps
| Gap | Rule | STRIDE | MAESTRO layer | Threat | Control as built | Test / evidence | Residual |
|---|---|---|---|---|---|---|---|
| duplicate_tracking_events | BR-01, BR-02 | T, R | L2 Data operations | the same scan recorded twice inflates counts and hides the real last event | ETL de-duplication; second copy to quarantine with reason | `test_etl_quarantine.py`, EVD-D-05 | duplicates with different ids but same content are only caught if `sequence_no` collides |
| stale_gps | BR-03 | T, I | L2 | an old vehicle position drives an assignment | none possible: the dataset has **no position timestamp**, so staleness cannot be computed; position is never given to the AI | BR-03 recorded; no assignment code exists | UNRESOLVED, needs a `position_time` field (owner ruling) |
| timezone_mismatch | BR-04 | T | L2 | events in mixed zones order incorrectly, SLAs mis-computed | ETL validates a declared zone and normalises to UTC; ETL BR-04 override: UNRESOLVED | ETL tests | owner ruling on zone override outstanding |
| duplicate_carrier_booking | BR-05 | R, D (cost) | L7 Agent ecosystem / integration | a retry books the same shipment twice | saga idempotency key, bounded retries (ceiling 5), compensation | `test_carrier_saga.py` (15), EVD-J-05: 1000 requests, 631 duplicates suppressed, 0 multi-bookings | saga is a simulation; real carrier idempotency semantics unknown |
| route_ignores_restrictions | BR-06 | E, T (safety) | L3 Agent frameworks | an automated tool assigns a route through a restricted zone | no route-assigning code exists (NEV); ETL flags restricted routes; AI cannot act | `test_no_endpoint_lets_the_system_change…` | no override record exists; a human can still dispatch outside the system |
| location_data_overexposure | BR-07 | I | L2, L6 Security & compliance | driver identity or position seen by a persona or sent to a model | policy field masking; `ai-context-policy` forbidden fields; gateway output leak check; logs exclude location; `LOG_LEVEL` default INFO | eval leak rate 0.0; `test_ai_output_never_contains…`; PIA | purpose defaulting (RL-02); real log sinks not reviewed |

## Part 2. Attack surface threats
| ID | STRIDE | Threat | Control | Test |
|---|---|---|---|---|
| T-01 | S | forged or unsigned token (alg none, tampered payload, missing claims) | PyJWT with fixed `algorithms=[HS256]`, required `exp` and `sub`, 60 s leeway; non-string/empty role rejected | `test_alg_none…`, `test_tampered_payload…`, `test_token_without…` |
| T-02 | S | self-asserted identity headers (F-17) | headers other than the bearer token ignored | `test_identity_headers_other_than_the_token_are_ignored` |
| T-03 | T | injection or traversal in identifiers | strict key patterns, exact match | `test_hostile_identifiers…` |
| T-04 | T | audit log edited after the fact | SHA-256 hash chain, `/audit/verify` | `test_audit_chain.py` |
| T-05 | R | action without a trace | audit for allow and deny, actor, correlation id | `test_unauthenticated_and_forged_attempts_are_audited` |
| T-06 | I | unexpected exception leaks internals | generic problem+json with correlation id | `test_unexpected_errors_do_not_leak_internals` |
| T-07 | I | secrets in code or history (F-09..F-14) | env-only secrets; secret scan; H3 rotation plan | `test_secret_scan.py`, secrets-hardening.md |
| T-08 | D | AI endpoint flood (F-46) | per-subject rate limit, 429 + Retry-After | `test_ai_rate_limit_returns_429…` |
| T-09 | D | oversized body | 64 KiB cap via Content-Length (chunked bodies not covered) | `test_oversized_request_body…` |
| T-10 | D | slow or failing model | timeout, circuit breaker, fallback | `test_resilience.py` |
| T-11 | E | persona escalation, AI persona approving | policy deny by default; AI persona denied on write | `test_ai_persona_cannot_approve…` |
| T-12 | E | CORS abuse from foreign origins | no CORS headers | `test_no_cors_headers_for_foreign_origins` |

## Part 3. AI-specific threats (OWASP LLM / MAESTRO L1, L3, L5)
| ID | Threat | Control | Evidence |
|---|---|---|---|
| A-01 | direct prompt injection in a field value | sanitiser (NFKC, Cf strip, `<>` escape), data delimited, enum allow-list | eval adversarial 43 cases, leak 0.0 |
| A-02 | indirect injection via stored data (F-22 class) | same; categorical fields only through `clean_enum` | RT-07, RT-08 |
| A-03 | data exfiltration through the output | forbidden-value scan; fallback `output_policy_violation` | eval, DEF-L-01 |
| A-04 | insecure output handling (XSS in the operations view) | `textContent` only, CSP, no innerHTML | `test_ops_view.py` |
| A-05 | excessive agency | no tool use, no write endpoint | K1 D-09 |
| A-06 | prompt tampering | `prompts.lock.json` | `test_prompt_lock.py` |
| A-07 | model supply chain | no model is configured; a real model needs its own review | OPEN (OQ-02) |
| A-08 | poisoned retrieval | not applicable: no retrieval | J1 |
| A-09 | cost exhaustion | rate limit, token cap | T-08 |

## Part 4. Supply chain
Dependencies are pinned in `requirements.txt`; SBOM and scans in Stage M (M1).
