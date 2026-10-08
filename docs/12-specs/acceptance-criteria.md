# Acceptance criteria

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | functional-requirements.md |
| Assumptions | See body |
| Unresolved issues | none specific |
| Residual risks | Criteria assume rulings on OQ-06 and OQ-14 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Requirement | Criterion (Given/When/Then) | Verifiable by |
|---|---|---|---|
| AC-01 | FR-01 | Given a shipment key SHI-00002 exists, when GET /records/SHI-00002 with a valid token, then 200 and shipment_id equals SHI-00002 | automated test (Stage H/L) |
| AC-02 | FR-01 | Given SHI-99999 is well-formed but absent, when requested, then 404 problem body and no other record is returned | automated test (Stage H/L) |
| AC-03 | FR-02 | Given id REC-0001, when requested, then 422 | automated test (Stage H/L) |
| AC-04 | FR-03 | Given no Authorization header, when GET /records/SHI-00002, then 401 | automated test (Stage H/L) |
| AC-05 | FR-03 | Given a forged X-User-Role: admin header and no token, then 401 (header ignored) | automated test (Stage H/L) |
| AC-06 | FR-04 | Given persona customer_support, when reading a shipment, then fields not allowed by access-semantics are masked or absent | automated test (Stage H/L) |
| AC-07 | FR-05 | Given a denied request, then 403 problem+json and an audit event with decision deny and the rule id | automated test (Stage H/L) |
| AC-08 | FR-06 | Given the fixture, when ETL runs, then every row with a rule violation of severity block is in quarantine with its rule id and none is in curated | automated test (Stage H/L) |
| AC-09 | FR-06 | Given quarantine ratio above 5%, then ETL exits non-zero | automated test (Stage H/L) |
| AC-10 | FR-07 | Given ETL runs twice on the same fixture, then curated output hashes are identical and the fixture hash manifest still verifies | automated test (Stage H/L) |
| AC-11 | FR-08 | Given a shipment with two active carrier bookings, then ETL reports it in multiple_active_bookings | automated test (Stage H/L) |
| AC-12 | FR-09 | Given a valid shipment, when POST /ai/summarize, then the body validates against ai-summary-output.schema.json and includes model_version, prompt_version, token_estimate, source_count | automated test (Stage H/L) |
| AC-13 | FR-10 | Given a shipment field containing the text "ignore previous instructions", then it appears only inside the data block and the output is unchanged in kind (no action, no leak) | automated test (Stage H/L) |
| AC-14 | FR-10 | Given a field value containing braces such as {x.__class__}, then no template evaluation occurs | automated test (Stage H/L) |
| AC-15 | FR-11 | Given the provider returns invalid JSON, then the deterministic fallback is used and generated_by is fallback with fallback_reason set | automated test (Stage H/L) |
| AC-16 | FR-11 | Given context is insufficient, then abstained is true, summary and recommendation are null, abstain_reason is set | automated test (Stage H/L) |
| AC-17 | FR-12 | Given a suggestion, when approved twice, then the second call returns 409; the first creates an approval_id that appears in the audit event | automated test (Stage H/L) |
| AC-18 | FR-13 | Given any protected request, then the audit event contains actor, correlation_id, tenant, resource, policy_decision and the chain verifies | automated test (Stage H/L) |
| AC-19 | FR-13 | Given one audit line is altered, then /audit/verify returns valid false with first_bad_index | automated test (Stage H/L) |
| AC-20 | FR-14 | Given a request with X-Correlation-ID, then the same id is in the response header, the audit event and the log line; given none, a generated id is used | automated test (Stage H/L) |
| AC-21 | FR-15 | Given the curated layer is missing, then /ready returns 503 and /health returns 200 | automated test (Stage H/L) |
| AC-22 | FR-16 | Given the running app, then the set of paths and methods in /openapi.json equals openapi.yaml | automated test (Stage H/L) |
| AC-23 | FR-17 | Given AI calls, then /metrics shows ai_requests_total, ai_tokens_total and ai_cost_units_total increased | automated test (Stage H/L) |
| AC-24 | FR-19 | Given APP_ENV not local and AUTH_SECRET unset, then the app refuses to start | automated test (Stage H/L) |
| AC-25 | FR-20 | Given a clean checkout, when the documented install and test commands are run, then all tests pass | automated test (Stage H/L) |
| AC-26 | FR-18 | Given a user opens the operations view, then record lookup and exception summary work with the same policy as the API | automated test (Stage H/L) |

Every FR-01..FR-20 has at least one criterion. Each criterion is binary and automatable. Thresholds for NFRs are in nfr-spec.md.
