# Requirements traceability matrix

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-E-03; EVD-F-04; acceptance-criteria.md |
| Assumptions | See body |
| Unresolved issues | Test files are PLANNED (written in Stage H/J/L); no test result is claimed here |
| Residual risks | See coverage-gap-register.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| FR | Business req | Findings | Intervention | Success criterion | Spec | AC | Planned impl | Planned test file |
|---|---|---|---|---|---|---|---|---|
| FR-01 | BR-1 | F-31,F-32 | I1 | SC-1 | FEAT-01 | AC-01, AC-02 | H5 | tests/unit/test_record_lookup.py |
| FR-02 | BR-2 | F-30 | I1 | SC-2 | FEAT-01 | AC-03 | H5 | tests/unit/test_record_lookup.py |
| FR-03 | BR-3 | F-17,F-19,F-20 | I2 | SC-3 | FEAT-02 | AC-04, AC-05 | H4 | tests/unit/test_identity_policy.py |
| FR-04 | BR-3 | F-18,F-21,F-16 | I2 | SC-3 | FEAT-02 | AC-06 | H4 | tests/unit/test_identity_policy.py |
| FR-05 | BR-3,BR-4 | F-17,F-43 | I2,I6 | SC-3 | FEAT-02 | AC-07 | H4 | tests/unit/test_identity_policy.py |
| FR-06 | BR-5 | F-33..F-38,F-40,F-41 | I3 | SC-5 | FEAT-03 | AC-08, AC-09 | H6 | tests/unit/test_etl_quarantine.py |
| FR-07 | BR-5 | F-54 | I3 | SC-5 | FEAT-03 | AC-10 | H6 | tests/unit/test_etl_quarantine.py |
| FR-08 | BR-5 | F-38 | I4 | SC-5 | FEAT-03 | AC-11 | H6 | tests/unit/test_etl_quarantine.py |
| FR-09 | BR-6 | F-25,F-27,F-28,F-29 | I9 | SC-6 | FEAT-04 | AC-12 | H7 | tests/unit/test_ai_gateway.py |
| FR-10 | BR-6 | F-22,F-23 | I9 | SC-6 | FEAT-04 | AC-13, AC-14 | H7 | tests/unit/test_ai_gateway.py |
| FR-11 | BR-6 | F-24,F-25 | I9 | SC-6 | FEAT-04 | AC-15, AC-16 | H7 | tests/unit/test_ai_gateway.py |
| FR-12 | BR-6 | F-26 | I9 | SC-6 | FEAT-04 | AC-17 | H7 | tests/unit/test_ai_gateway.py |
| FR-13 | BR-4 | F-43,F-44,F-45 | I6 | SC-4 | FEAT-05 | AC-18, AC-19 | H8 | tests/unit/test_audit_chain.py |
| FR-14 | BR-4 | F-42 | I6 | SC-4 | FEAT-05 | AC-20 | H8 | tests/unit/test_audit_chain.py |
| FR-15 | BR-8 | F-46 | I1 | SC-8 | FEAT-06 | AC-21 | H2/H9 | tests/integration/test_contract_ops.py |
| FR-16 | BR-8 | F-50 | all | SC-8 | FEAT-06 | AC-22 | H2/H9 | tests/integration/test_contract_ops.py |
| FR-17 | BR-6 | F-46,F-28 | I9 | SC-6 | FEAT-04 | AC-23 | H7 | tests/unit/test_ai_gateway.py |
| FR-18 | BR-1 | F-05 | I1,I9 | SC-1 | FEAT-01 | AC-26 | H5 | tests/unit/test_record_lookup.py |
| FR-19 | BR-7 | F-09..F-14 | I2 | SC-7 | FEAT-02 | AC-24 | H4 | tests/unit/test_identity_policy.py |
| FR-20 | BR-8 | F-02,F-03,F-04,F-07 | all | SC-8 | FEAT-06 | AC-25 | H2/H9 | tests/integration/test_contract_ops.py |

Backward: each FR traces to a business requirement (BR-n) and a success criterion (SC-n) from Stage B. Forward: spec, acceptance criterion, planned implementation step and planned test file. NFR-1..NFR-10 trace through `nfr-spec.md`.
