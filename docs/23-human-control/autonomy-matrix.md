# Autonomy matrix

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/main.py, apps/api/ai/gateway.py, tests listed |
| Assumptions | See body |
| Unresolved issues | D-11 override ownership |
| Residual risks | HC-R-01 no separation of duties between requester and approver (see approval-gates.md) |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Levels: **DET** deterministic code, no AI; **REC** AI recommends; **EXE** AI executes after validation; **HUM** requires explicit human approval; **NEV** never delegated to the system.

| # | Decision | Level | Enforcement (code, not prose) | Test |
|---|---|---|---|---|
| D-01 | Accept or quarantine an input row | DET | `etl/validation.py` rules BR-01..BR-13; rejects go to `data/quarantine` with a reason | `tests/test_etl_quarantine.py` |
| D-02 | Collapse duplicate tracking events | DET | ETL de-duplication (BR-01, BR-02) | `tests/test_etl_quarantine.py` |
| D-03 | Allow or deny a read | DET | `PolicyEngine.decide(role, entity, action, purpose)` from `access-semantics.yaml`, deny by default | `tests/test_identity_policy.py`, `semantic-layer/tests/test_semantic_layer.py` (full-grid parity with generated Rego) |
| D-04 | Mask a field for a persona | DET | policy field overrides (`customer_id` = `***` for dispatcher) | `test_security_suite.py::test_masked_fields…` |
| D-05 | Compute KPIs | DET | `apps/api/kpis.py` | `tests/test_contract_ops.py` |
| D-06 | Summarise an exception shipment | REC | `AiGateway.summarize`; deterministic provider by default, model optional; output schema-validated; `requires_human_approval` is always `true` | `tests/test_ai_gateway.py`, eval `approval_flag_true_rate = 1.0` |
| D-07 | Choose the recommendation class | DET (rule table) / REC (model text) | gateway recommendation class from status; a model cannot change the class check | eval `recommendation_class_correct_rate = 1.0` |
| D-08 | Accept or reject an AI suggestion | **HUM** | `POST /ai/summaries/{id}/decision`; needs `shipments:write` (dispatcher with purpose `dispatch` only); one decision per suggestion (409); actor taken from the token, never the body | `07-logistics-shipment-fleet-routing-ops/tests/test_human_control.py` (9 tests) |
| D-09 | Change a shipment, route, vehicle assignment or carrier booking | **NEV** | no endpoint exists; the OpenAPI test asserts the only mutating routes are the AI request and the decision record | `test_human_control.py::test_no_endpoint_lets_the_system_change…` |
| D-10 | Retry or compensate a carrier booking | DET, bounded | `carrier_saga.py`: idempotency key, `HARD_RETRY_CEILING = 5`, compensation on failure, JSONL store. Real carrier calls are not enabled (simulated carrier only) | `tests/test_carrier_saga.py` (15) |
| D-11 | Assign a restricted-zone route without an override (BR-06) | **NEV** | no override field in the data; there is no code path that assigns routes. The rule is recorded; the dataset cannot express an override (UNRESOLVED, owner ruling) | rule `BR-06` in ETL flags only |
| D-12 | Expose driver identity or location | DET + **NEV** for AI | `ai-context-policy.yaml` forbidden fields; gateway `_forbidden_values`, `_leaks` | eval `forbidden_field_leak_rate = 0.0` |
| D-13 | Change a prompt | **HUM** | `prompts.lock.json`; mismatch raises `PromptIntegrityError` at load, so a change needs a deliberate `scripts/lock_prompts.py` run reviewed in a pull request | `tests/test_prompt_lock.py` |
| D-14 | Switch AI on/off or select a real model | **HUM** | environment settings `AI_ENABLED`, `AI_PROVIDER`; `UnconfiguredModelProvider` always falls back | `test_resilience.py::test_ai_disabled…`, `::test_model_provider_unconfigured…` |
| D-15 | Change access rules | **HUM** | edit `access-semantics.yaml`; generated Rego and the parity test must pass | policy parity test |
| D-16 | Delete or purge evidence/audit | **NEV** (system) | hash-chained append-only audit; `GET /audit/verify` detects edits | `tests/test_audit_chain.py` |

[VF] 16 of 16 decisions have an enforcement mechanism. Two (D-09, D-11) are enforced by *absence* of a code path; that is stated rather than disguised as a control.
[INF] D-08 records a human decision about a *suggestion*. Nothing downstream acts on it yet. Until an action integration exists, "approval" has no operational effect; this is intentional for the pilot and must be revisited at the first write integration.
