# Timeout and retry policy

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/integration/carrier_saga.py, EVD-J-05 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Call | Timeout | Retries | Backoff | Ceiling | Notes |
|---|---|---|---|---|---|
| Model provider | 5 s (`AI_PROVIDER_TIMEOUT_S`) | **none** (fallback instead) | – | – | a retry against a failing model is a retry storm; the breaker plus fallback replace it |
| Carrier booking | per attempt: carrier-side [UNK] | transient errors only | exponential from 0.2 s, cap 5 s, jitter | `max_attempts` 3 by default, **hard ceiling 5** (BR-13) | permanent errors fail at once |
| Carrier cancel (compensation) | as above | up to `cancel_attempts` 3 | same | 5 | failure leaves `compensation_required` for a person |
| Inbound API calls | platform | none (client decides) | – | – | |
| ETL | none | none (rerun is idempotent) | – | – | |

The data shows what happens without a ceiling: `retry_count` up to 4,995 (F-39). Validation: config rejects `max_attempts` > 5 (`SagaConfig.validate`), simulation max attempts 3.
Retry only what is safe to repeat: bookings are repeatable only because of the idempotency key.
