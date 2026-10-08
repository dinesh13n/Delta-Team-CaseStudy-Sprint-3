# Dependency Hotspots

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

- shipments.csv is read by the API, the ETL and the legacy script: one file, three readers, no shared rules [VF].
- `domain_service.load_record` is the single data-access function used by both endpoints [VF].
- `audit.write_event` writes to a path derived from the file location (`parents[3]/logs`) [VF].
- `scripts/sanity_check.py` couples the repo to exact fixture counts and doc paths (F-54, F-55) [VF].
