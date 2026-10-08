# Adapter map

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

DataRepository -> CsvRepository; AuditSink -> JsonlAuditSink; ModelProvider -> DeterministicProvider / UnconfiguredModelProvider; TokenVerifier -> Hs256Verifier / JwksVerifier(stub); CarrierPort -> SimulatedCarrier. Each is swappable without touching callers (`main.Services` is the composition root).
