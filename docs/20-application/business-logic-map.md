# Business logic map

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Rule family | Where enforced | Test |
|---|---|---|
| Key patterns (BR-P-*) | `repository` + `check_key` | test_record_lookup |
| Validation and quarantine (BR rules, severity override BR-04 -> flag) | `etl/validation.py` | test_etl_quarantine |
| Access (access-semantics.yaml) | `PolicyEngine` | test_identity_policy, Rego parity |
| Exception signal (status in exception/failed/manual_hold or an exception event) | `DeterministicProvider` | test_ai_gateway, eval golden |
| Retry ceiling 5 | provider advice + saga hard ceiling | eval edge, test_carrier_saga |
| KPI formulas | `kpis.py` | test_contract_ops / O1 |
