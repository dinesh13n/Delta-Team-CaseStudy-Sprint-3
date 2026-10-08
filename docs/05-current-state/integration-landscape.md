# Integration Landscape

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

| Interface | Direction | Implemented |
|---|---|---|
| HTTP API (3 routes) | inbound | yes |
| Web scaffold to `/api/...` | inbound | proxy undefined |
| Carrier partners | outbound | no (data columns only) |
| OT vendor | outbound | no (token in env template) |
| AI model provider | outbound | no (simulated) |
| Database | outbound | no (DSN in env template; app reads CSV) |
