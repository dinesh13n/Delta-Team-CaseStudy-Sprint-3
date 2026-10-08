# Integration test results

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

`tests/test_carrier_saga.py`: **15 passed**. Simulation (`scripts/saga_simulation.py`, seeded, flaky carrier at 35% transient failure): 1,000 requests over 400 shipments -> 962 CONFIRMED, 38 FAILED at the ceiling, **631 duplicate requests suppressed**, 533 carrier calls, 355 live bookings, **0 shipments with more than one live booking**, **max attempts per booking 3** (configured 3; hard ceiling 5), versus the fixture's retry_count max 4,995 and 3 duplicate booking ids.
Honest limit [VF]: the carrier is simulated; this proves the saga logic, not a real carrier's behaviour. [UNK] Real carrier idempotency-key support is required for the "exactly once" guarantee at the partner side.
