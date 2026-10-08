# Cache effectiveness

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT APPLICABLE today (no cache) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

No prompt cache, response cache or retrieval cache exists. Cache hit rate: **n/a**. [VF]

## Opportunity (designed, not built)
- A suggestion is a pure function of (record id, data load id, prompt version, provider config hash). A response cache keyed on those four would return the same suggestion until the next ETL load. Saving: one model call per repeated request.
- **Constraint:** every request still needs its own audit event and approval registration, so a cache saves tokens, not audit writes. A cached suggestion must carry the original `summary_id` or get a new one — an owner/auditor decision.
- Provider-side prompt caching (stable system prompt) applies only once a provider with that feature is chosen.

Repeat-request share in production is unknown; in the fixture every shipment was requested once, so no cache hit could be measured.
