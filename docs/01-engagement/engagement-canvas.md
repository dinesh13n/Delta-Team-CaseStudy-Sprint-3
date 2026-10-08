# Engagement Canvas

| Field | Value |
|---|---|
| Stage | B: Qualification (Spine 1) |
| Runbook step | B1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-01, OQ-02, OQ-03, OQ-05, OQ-11 (see open-qualification-questions.md) |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Element | Content | Class |
|---|---|---|
| Client context | Fictional logistics operator (shipment, fleet, routing, exception operations) represented by repo `07-logistics-shipment-fleet-routing-ops` | [VF] repo README, domain spec |
| Business problem (provisional) | Operations records cannot be trusted or traced end to end; exceptions lack evidence; cost is not tied to shipments | [INF] from A4 findings |
| Sponsor | Not named in any artifact | [UNK] OQ-05 |
| Business owner / technical owner | Not named | [UNK] OQ-05 |
| Engagement type | Training case study: transform a brownfield repo to production-grade with evidence, scored on 5 rubric criteria (100 marks) | [VF] rubric, challenge guide |
| Audience | Company CTO (task brief) | [VF] brief |
| Urgency / deadline | Not stated | [UNK] OQ-12 |
| Expected outcomes | Execution-ready runbook (done); then executed transformation with evidence | [VF] brief, operator instruction 2026-10-08 |
| Dependencies | Platform (OQ-01), models (OQ-02), egress (OQ-03), approvers (OQ-05), write authorisation (OQ-11) | [VF] runbook 04 |
| Constraints | Evidence contract; baseline frozen until authorisation; synthetic data only | [VF] operating contract |
