# Control Points

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

| Control | Present? | Evidence |
|---|---|---|
| Authentication | no | role header |
| Authorisation | weak allow-list | main.py:13 |
| Input validation | none | no models |
| Data validation | counting only | etl |
| Audit | local file, no actor | audit.py |
| Approval gate | none (advisory text) | ai_gateway.py |
| Rate limit / quota | none | |
| Change control | none | F-08 |
