# Adapter strategy

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/10-architecture; docs/11-data-context; docs/12-specs |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; platform OQ-01 |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Each port in `docs/12-specs/interface-contracts.md` has a default adapter and a swap path: CsvRepository -> database repository; JsonlAuditSink -> external store; DeterministicProvider -> vendor provider; Hs256Verifier -> JwksVerifier; SystemClock -> FixedClock for tests. The legacy services become thin wrappers calling the new use cases until retired. Contract tests run against every adapter. No adapter may import the API layer.
