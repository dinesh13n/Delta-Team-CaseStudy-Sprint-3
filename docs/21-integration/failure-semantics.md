# Failure semantics

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-J-05 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Failure | Behaviour | Test |
|---|---|---|
| Carrier timeout/5xx | retry with capped exponential backoff + jitter, at most `max_attempts` (<= 5 hard) | test_transient_failures..., test_retry_ceiling... |
| Carrier rejects | fail at once, no retry | test_permanent_error... |
| Duplicate request | stored outcome returned, carrier not called | test_duplicate_request... |
| Concurrent duplicates | exactly one booking; others get in-flight or the stored result | test_concurrent_duplicates... |
| Failure after confirmation | cancel at carrier (bounded); if cancel fails -> COMPENSATION_FAILED + flag | test_failure_after_confirmation..., test_failed_compensation... |
| Process restart | outcomes reloaded from the JSONL log | test_state_survives_a_restart |
| Model provider down | deterministic fallback, `fallback_reason` | eval failure set |
| Stale data / timeouts | timeouts are a deployment concern [UNK]; no outbound HTTP exists yet | n/a |
