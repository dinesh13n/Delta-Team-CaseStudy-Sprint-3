# Acceptance test plan

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Level | Command | Gate |
|---|---|---|
| Unit/integration | `pytest` | TG-2 |
| Characterization | `pytest tests/characterization` | TG-1 |
| Contract | `pytest tests/test_contract_ops.py` + route diff | TG-9 |
| Policy parity | `pytest tests/test_identity_policy.py` + `opa test` | AC-06 |
| Data | `python -m etl.run_daily_batch` + `test_etl_quarantine` | AC-08..11 |
| AI | `pytest tests/test_ai_gateway.py` + `evaluation/run_eval.py` | AC-12..17 |
| End-to-end | `pytest tests/test_ops_view.py` (HTTP workflow) | AC-26 |
| Saga | `pytest tests/test_carrier_saga.py` | AC-27 |
| Smoke | `make smoke` | H-X10 |
