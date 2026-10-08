# Transformation authorisation record (G4)

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-G-04-authorisation-record.txt; decision-log D-009 |
| Assumptions | See body |
| Unresolved issues | OQ-05, OQ-11 |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Scope requested
Write access to `07-logistics-shipment-fleet-routing-ops/` application code, tests, configuration, docs and IaC, limited to the backlog TB-01..TB-12 (Stage H), the data-derived directories `data/curated` and `data/quarantine`, and new documents under `docs/` and `evidence/`. The fixture `data/synthetic/*` and the do-not-change register are excluded.
## Authorisation actually obtained
- Source: the operator (Dinesh, Senior GenAI Solution Architect, acting Transformation Lead) instructed on 2026-10-08: "Complete the 02-TRANSFORMATION-RUNBOOK runbook your own, and push the code in repository". This is recorded as decision D-009.
- Repository Owner: UNRESOLVED. Business Sponsor: UNRESOLVED. CTO: not named. No signature exists.
## Status
**CONDITIONAL.** The operator's instruction authorises the work inside the training engagement, but the runbook requires written authorisation from the Repository Owner and Business Sponsor (OQ-05, OQ-11). This record is NOT a signed authorisation and `EVD-G-04` is therefore an unsigned record, not the signed PDF the runbook names. Stage H work is carried out under D-009 and flagged in every later report; its evidence admissibility at Stage R depends on ratification.
## Ratification block (to be completed by a human)
| Role | Name | Decision | Date | Signature |
|---|---|---|---|---|
| Repository Owner | UNRESOLVED | | | |
| Business Sponsor | UNRESOLVED | | | |
