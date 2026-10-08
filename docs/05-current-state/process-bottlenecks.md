# Process Bottlenecks

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 5 current state) |
| Runbook step | C4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/discovery/; evidence/05-current-state/EVD-C-04-flow-to-code-trace.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- [VF] Lookup reads the whole CSV on every request (domain_service.py), O(n) per call.
- [VF] The simulated AI call sleeps 10 ms; real model latency is unknown (fixture p95 13.7 s).
- [VF] ETL discards defects and cannot hand them to a human queue.
- [UNK] Real throughput; not measurable until a baseline load test (Stage N).
