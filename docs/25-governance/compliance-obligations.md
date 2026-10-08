# Compliance obligations (candidate set, UNVALIDATED)

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (regulatory scope UNRESOLVED, OQ-04) |
| Evidence sources | docs/24-security-privacy/privacy-impact-assessment.md, semantic-layer/* |
| Assumptions | See body |
| Unresolved issues | OQ-04, OQ-21 |
| Residual risks | RA-01 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Statement of scope.** No artifact in the engagement names a jurisdiction, regime, contract or regulator. This document therefore does **not** determine which laws apply. It lists *categories of obligation suggested by the data and functions actually present*, so a Compliance Owner can validate or discard each one. Nothing here is a legal conclusion. This is the K-X6 route "formally recorded as an accepted unresolved risk" (RA-01 in `risk-acceptance-register.md`).

| ID | Trigger in the system | Candidate obligation category | Applicability | Validation needed |
|---|---|---|---|---|
| CO-01 | `driver_id`, `current_location` are about identifiable workers | personal-data protection (lawfulness, minimisation, retention, subject rights, security) | [UNK] | jurisdiction of drivers and operator |
| CO-02 | `customer_id` in shipments | personal-data protection (as above) | [UNK] | as above |
| CO-03 | tracking drivers' live location | employment and worker-monitoring rules (notice, proportionality, consultation) | [UNK] | labour counsel |
| CO-04 | `customs_agent` persona, `customs_required`, `border_risk`, cross-border routes | customs and trade compliance (record keeping, declarations) | [UNK] | customs broker / trade compliance |
| CO-05 | `temperature_controlled` shipments | sector rules for cold-chain goods (food, pharma) | [UNK] | depends on cargo types |
| CO-06 | route/restriction data, driver assignment | transport safety and driver hours rules | [UNK] | depends on mode and region |
| CO-07 | an AI system produces suggestions | AI-specific regimes with risk classification, transparency and human-oversight duties | [UNK] | classification by legal review. **Note [INF]:** current use (summarising shipment status, suggest-only, no decision about people) is the low-risk end; extending AI to allocate tasks to or evaluate drivers would change the class and must trigger re-review. |
| CO-08 | hosted model, cloud platform (future) | cross-border transfer, processor contracts, data residency | [UNK] | after OQ-01/OQ-02 |
| CO-09 | audit and evidence | record-keeping duty for decisions | [UNK] | retention periods unknown |
| CO-10 | open-source dependencies | licence obligations | verified in M1 (SBOM) | – |

## What was **not** done
No legal research was performed, no regulator was contacted, no article of any law is cited, because citing unvalidated law would look more authoritative than the evidence supports.

## Validation plan
1. Compliance Owner named (OQ-05). 2. Confirm operating jurisdictions and data-subject locations. 3. Walk CO-01..CO-09, mark each Applies / Does not apply / Needs counsel. 4. Update `compliance-control-matrix.md` owners and evidence. 5. Re-open R1 if any "Applies" has no control.
