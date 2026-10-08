# Enum Violations (Step D2)

| Field | Value |
|---|---|
| Stage | D: Semantic Layer Extraction |
| Runbook step | D2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-C-05; EVD-D-02 |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Observed violations of the declared domains in `status-taxonomy.yaml`, measured on the baseline fixture. Full values and counts: `evidence/11-data-context/EVD-D-02-enum-violations.csv`.

The fourteen interchangeable tokens (not_enforced, approved, rejected, pending, legacy, internal, standard, degraded, manual, normal, vendor, high_risk, requires_review, ai_assisted) appear across many unrelated fields (F-37). Blank values are counted as illegal rows.

| Entity | Field | Domain | Illegal rows | Remedy | Note |
|---|---|---|---|---|---|
| shipments | origin | ref:location | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| shipments | destination | ref:location | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| shipments | service_tier | service_tier | 333 | schema_fix | domain is a PROPOSAL (assumption); observed tokens are workflow words, not values of this field; Data Owner to confirm domain then data fix |
| shipments | status | shipment_status | 47 | legacy_tolerance | 'approved' is not a lifecycle state; accept-and-flag until the Data Owner rules (UNRESOLVED) |
| shipments | customs_required | boolean | 1 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| shipments | temperature_controlled | boolean | 1 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| tracking_events | event_type | tracking_event_type | 354 | schema_fix | domain is a PROPOSAL (assumption); observed tokens are workflow words, not values of this field; Data Owner to confirm domain then data fix |
| tracking_events | source_system | source_system | 232 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| tracking_events | location | ref:location | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| tracking_events | duplicate_flag | boolean | 1 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| tracking_events | timezone | ref:timezone | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| vehicles | vehicle_type | vehicle_type | 323 | schema_fix | domain is a PROPOSAL (assumption); observed tokens are workflow words, not values of this field; Data Owner to confirm domain then data fix |
| vehicles | current_location | ref:location | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| vehicles | maintenance_status | maintenance_status | 244 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| vehicles | cold_chain_capable | boolean | 1 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| vehicles | region | region | 1 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| routes | origin | ref:location | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| routes | destination | ref:location | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| routes | restricted_zone_flag | boolean | 1 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| routes | weather_risk | risk_level | 268 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source; numeric 1.42 present in a categorical field (F-61) |
| routes | border_risk | risk_level | 269 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| carrier_bookings | carrier | ref:carrier | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| carrier_bookings | status | shipment_status | 37 | legacy_tolerance | 'approved' is not a lifecycle state; accept-and-flag until the Data Owner rules (UNRESOLVED) |
| carrier_bookings | compensation_required | boolean | 1 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| ai_invocations | use_case | ai_use_case | 354 | schema_fix | domain is a PROPOSAL (assumption); observed tokens are workflow words, not values of this field; Data Owner to confirm domain then data fix |
| ai_invocations | model | ref:model | 354 | data_fix | field holds placeholder workflow tokens, not a valid reference; schema fix adds reference type, data fix supplies real references |
| ai_invocations | constraint_violations | constraint_class | 166 | schema_fix | meaning of alpha/beta/gamma unknown [UNK]; owner decision before enforcement |
| ai_invocations | recommendation | recommendation | 249 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |
| ai_invocations | human_override | human_decision | 250 | data_fix | illegal tokens are cross-field pollution; quarantine and correct at source |

Remedy key: **data_fix** correct at source or quarantine; **schema_fix** declare or correct the domain; **legacy_tolerance** accept with a flag until an owner rules.
Domains marked PROPOSED are assumptions, not facts, pending the Data Owner (UNRESOLVED).
