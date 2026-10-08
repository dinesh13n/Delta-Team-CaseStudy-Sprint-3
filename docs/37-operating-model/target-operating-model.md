# Target operating model

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (design; no named owners) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | P-R-01 no owners |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Shape
A small product team runs one modular-monolith service with a daily data pipeline and a suggest-only AI component. Steady state needs these standing responsibilities; **no person is named for any of them** (OQ-05). The operator, Dinesh, holds every role slot provisionally (ASM-3; decision-log D-001 to D-004).

| Responsibility | Standing role (not a person) | Today |
|---|---|---|
| Value and priorities | Business Sponsor / Product Owner | UNRESOLVED |
| Architecture and change | Architect / Dev lead | provisional: operator |
| Access, secrets, vulnerabilities | Security Owner | UNRESOLVED |
| Prompts, models, evaluation | AI Governance Owner | UNRESOLVED |
| Data contract, enum and rule rulings | Data Owner | UNRESOLVED |
| Regulatory obligations | Compliance Owner | UNRESOLVED |
| Run, alerts, SLOs, incidents | SRE / Operations Owner | UNRESOLVED |
| Releases | Release Manager | UNRESOLVED |
| Independent check of evidence | Reviewer | **empty** |

## Operating cadence (proposed)
Daily: ETL load and freshness; alert review. Weekly: drift check, AI decision review. Monthly: SLO and error budget review, dependency audit. Quarterly: evaluation with fresh cases, red-team refresh, access review, risk register review.

## Not designed
Staffing levels, shift cover, vendor management, training plan: no information on the organisation.
