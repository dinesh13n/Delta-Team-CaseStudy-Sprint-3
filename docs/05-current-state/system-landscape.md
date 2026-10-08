# System Landscape (current state)

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

Refines docs/00-preflight/discovery/system-landscape.md with Stage C evidence.
- [VF] Runtime components: 1 FastAPI app, 2 batch scripts. No datastore server, queue or cache.
- [VF] Executed in C3: API tests pass (3), ETL and smoke exit 0.
- [VF] Declared-but-absent: Angular portal, carrier integrations, OT vendor integration (`OT_VENDOR_TOKEN` in .env.example, no code).
- [UNK] External systems of record.
