# RACI

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (P-X1: gaps listed, not accepted by anyone) |
| Evidence sources | docs/25-governance/accountability-map.md |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | P-R-01 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Asset-level. R responsible, A accountable, C consulted, I informed. **Names: none.** Each cell is a role. P-X1 requires a named owner *or an explicitly accepted unresolved gap*; the gap is explicit below, but acceptance needs the sponsor, who is also unnamed.

| Asset | Sponsor | Product | Dev lead | Security | AI gov | Data | Compliance | SRE/Ops | Release | Reviewer |
|---|---|---|---|---|---|---|---|---|---|---|
| Application code | I | C | **A/R** | C | I | I | I | C | I | C |
| Access policy (`access-semantics.yaml`) | I | C | C | **A/R** | I | C | C | I | I | C |
| Prompts and `prompts.lock.json` | I | C | R | C | **A** | I | C | I | I | C |
| Model selection and `models.lock.json` | C | I | R | C | **A** | I | C | I | I | C |
| Evaluation sets and thresholds | I | C | R | C | **A** | C | I | I | I | C |
| Data contract, ETL, enum rulings | I | C | R | I | I | **A** | C | C | I | I |
| Audit log and evidence | I | I | R | C | C | I | **A** | C | I | C |
| Observability, alerts, SLOs | I | C | R | C | C | I | I | **A/R** | I | I |
| Cost and token budgets | **A** | C | C | I | R | I | I | C | I | I |
| Vendors and contracts | **A** | C | C | R | C | I | C | C | I | I |
| Releases and rollback | **A** | C | C | C | C | C | C | C | **R** | C |
| Incidents | I | I | C | R | C | C | C | **A** | I | I |
| Secrets and key revocation | I | I | C | **A/R** | I | I | C | R | C | C |
| Retirement and archive | **A** | C | R | C | C | C | **R** | C | C | I |
| Independent evidence review | I | I | I | C | C | I | I | I | I | **A/R** |

**Gap statement.** Every row has an unnamed A. Proposed acceptance: the project runs as a controlled pilot on synthetic data with the operator in all slots until the sponsor names owners; nothing here is approved for production on real data. *No one has accepted this gap.*
