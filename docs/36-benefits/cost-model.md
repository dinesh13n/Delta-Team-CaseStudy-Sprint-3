# Cost model

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | evidence/36-benefits/EVD-O-03-benefit-model.json (SHA-256 2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52); docs/32-finops/tco-model.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Cost side in analyst-hours: build/governance (B), monthly operations (R), review time (inside "minutes saved", which is net of the added review). Tokens: omitted as immaterial (271 tokens per request; below 0.001 analyst-hours at any plausible wage). Platform, IdP, licences: [UNK], excluded and listed in `docs/32-finops/tco-model.md`. Because platform cost is excluded, every net figure here **overstates** value.
