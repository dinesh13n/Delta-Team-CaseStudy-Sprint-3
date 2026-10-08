# Accountability map (RACI)

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | governance-model.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | no independent reviewer |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

R = responsible, A = accountable, C = consulted, I = informed. Roles only (OQ-05).

| Activity | Sponsor | Product | Arch | Security | AI gov | Data | Compliance | Release | Reviewer |
|---|---|---|---|---|---|---|---|---|---|
| Access rule change | I | C | C | **A/R** | I | C | C | I | I |
| Prompt/model change | I | C | C | C | **A/R** | I | C | I | C |
| Enum/rule rulings (BR-04, BR-06, enum vocab) | I | C | I | I | I | **A/R** | C | I | I |
| Risk acceptance (security) | C | I | C | **A** | I | I | C | R | C |
| Risk acceptance (regulatory) | **A** | I | I | C | C | C | **R** | I | C |
| Release decision | **A** | C | C | C | C | C | C | **R** | C |
| Evidence integrity / re-run | I | I | I | C | C | I | I | I | **A/R** |
| Incident command | I | I | C | R | C | C | C | **A** | I |

Rule: the person who builds a change must not be the only reviewer of it. At present the **builder, tester and author of every gate document is the same agent**; the Reviewer column is empty. This is the single largest governance gap and is carried to R1.
