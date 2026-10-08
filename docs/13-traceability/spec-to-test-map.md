# Spec to test map

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

| Spec artefact | Acceptance criteria | Planned tests |
|---|---|---|
| FEAT-01 | AC-01, AC-02, AC-03, AC-26 | tests/unit/test_record_lookup.py |
| FEAT-02 | AC-04, AC-05, AC-06, AC-07, AC-24 | tests/unit/test_identity_policy.py |
| FEAT-03 | AC-08, AC-09, AC-10, AC-11 | tests/unit/test_etl_quarantine.py |
| FEAT-04 | AC-12, AC-13, AC-14, AC-15, AC-16, AC-17, AC-23 | tests/unit/test_ai_gateway.py |
| FEAT-05 | AC-18, AC-19, AC-20 | tests/unit/test_audit_chain.py |
| FEAT-06 | AC-21, AC-22, AC-25 | tests/integration/test_contract_ops.py |
| openapi.yaml | AC-22 | tests/integration/test_contract_ops.py (route diff, schema validation) |
| audit-event.schema.json | AC-18, AC-19 | tests/unit/test_audit_chain.py |
| ai-summary-output.schema.json | AC-12, AC-15, AC-16 | tests/unit/test_ai_gateway.py |
| nfr-spec.md | see nfr-spec | Stage L TEVV (performance, availability), CI (coverage, secrets) |
