# Final API interface baseline

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | `evidence/12-specs/EVD-F-03-openapi.yaml` (sha256 `6016a47d34dccadb44c6f7237cd3077f44edce88f5029801d5d1249272215c87`) |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Method | Path | Auth | Purpose |
|---|---|---|---|
| GET | /health | none | liveness (unchanged behaviour) |
| GET | /ready | none | readiness: data layer loadable, signing key present (503 otherwise) |
| GET | /metrics | ops role | Prometheus text |
| GET | /shipments | token + policy | curated shipments visible to caller |
| GET | /shipments/{id}/events | token + policy | tracking events of one shipment |
| GET | /records/{id} | token + policy | exact-key read; compatibility path; masks customer id |
| POST | /ai/summarize/{id} | token + policy | suggest-only summary; 429 rate limit; 503 when AI off |
| POST | /ai/summaries/{id}/decision | token + policy | approve or reject; 409 on repeat |
| GET | /audit/verify | auditor/ops | hash-chain verification |
| GET | /kpis | token + policy | frozen KPI set K1..K10 |

Errors are RFC 7807-style problem bodies with a correlation id. Contract drift fails `make smoke` and a test. [VF, OpenAPI file hashed above]
