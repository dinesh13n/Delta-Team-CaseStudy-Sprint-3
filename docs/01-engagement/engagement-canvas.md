# Engagement Canvas

| Field | Value |
|---|---|
| Stage | B: Qualification, Stakeholders and Problem Framing (Spine 1) |
| Runbook step | B1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/ (A4, A5, A6 packs); runbook/04-OPEN-QUESTIONS-REGISTER.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Element | Content | Class |
|---|---|---|
| Client context | Training engagement (Birlasoft FDE programme, Sprint 3, team Delta-Team); delivered brownfield repository `07-logistics-shipment-fleet-routing-ops` | [VF] README root |
| Business problem (as stated by the repo) | Logistics shipment, fleet, routing and exception operations with weak access control, weak audit, data defects and ungoverned AI | [VF] README, docs/domain-specific-spec.md |
| Sponsor | not named | [UNK] OQ-05 |
| Business owner | not named | [UNK] |
| Technical owner | not named; operator Dinesh acts as Transformation Lead only | [VF] A5 |
| Urgency | Not stated; training schedule only | [UNK] OQ-12 |
| Expected outcomes | A production-grade repository with evidence scored on five rubric criteria (100 marks) | [VF] Evaluation Rubrics.jpeg |
| Dependencies | Platform (OQ-01), two models (OQ-02), egress (OQ-03), approvers (OQ-05) | [VF] runbook 04 |
| Delivery constraints | Read-only until authorisation (D-004, D-009); evidence-first; no real data | [VF] operating contract |
| Why it could be premature | No named sponsor, no platform, no models; declared capabilities unimplemented | [VF] A4 |

Stakeholder claims versus validated evidence: the repo documents claim "audit evidence exists" (`docs/transformation-roadmap.md`); validated: audit has no actor or correlation id (`apps/api/services/audit.py`). The runbook claimed 66.4% uncorrelated events; validated: 66.4% (983 null + 1,009 empty, D-012).
