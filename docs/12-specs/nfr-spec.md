# NFR specification

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | openapi.yaml; schemas/; docs/09-initial-prd; docs/10-architecture; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; open items in docs/12-specs/spec-readiness.md |
| Residual risks | Specs are PROVISIONAL until OQ-01/02/03/05/11 are ruled |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Binding form of NFR-1..NFR-10 from `docs/09-initial-prd/nfrs.md`, each with the measurement method named there.
| NFR | Target | Verified in |
|---|---|---|
| NFR-1 read p95 | <= 500 ms | Stage L performance test |
| NFR-2 availability | >= 99.5% test window | Stage L |
| NFR-3 correlation | 100% new events | Stage H test, event scan |
| NFR-4 audit completeness | 100% records have actor and correlation id | Stage H test |
| NFR-5 data quality | 0 duplicate or blank-mandatory in curated | Stage H ETL test |
| NFR-6 coverage | >= 80% lines | CI gate |
| NFR-7 secrets | 0 matches | secret scan |
| NFR-8 reproducibility | clean checkout passes | CI + H gate |
| NFR-9 AI p95 | <= 3,000 ms | Stage J benchmark |
| NFR-10 AI cost | <= 2.25 cost units | Stage J (baseline mean 6735.29/3000 events = 2.245 per event [VF/INF]) |
