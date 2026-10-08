# Human-control test results

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/23-human-control/EVD-K-01-human-control-tests.txt |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Evidence: `evidence/23-human-control/EVD-K-01-human-control-tests.txt`.

| Test | What it proves |
|---|---|
| `test_no_endpoint_lets_the_system_change_a_shipment_route_or_booking` | only two mutating routes exist; D-09 |
| `test_every_suggestion_requires_human_approval_even_when_abstained` | flag always true |
| `test_ai_persona_cannot_approve_its_own_suggestion` | 403 |
| `test_read_only_personas_cannot_decide` | 403 for customer_support, driver, customs_agent, carrier_partner |
| `test_only_one_decision_per_suggestion_and_it_is_final` | 409 |
| `test_decision_input_is_validated` | 422 for bad decision, missing field, over-long reason; 404 unknown id |
| `test_decision_is_audited_with_actor_and_approval_id_and_chain_stays_valid` | audit link |
| `test_denied_decision_attempts_are_audited` | denial recorded |
| `test_low_confidence_model_output_becomes_an_abstention` | confidence handling |

[VF] All 9 pass in the full suite run (158 passed, 7 xfailed, Python 3.14.7).
[VF] Not tested: separation of duties (not implemented), approval expiry (not implemented).
