# Confounder analysis

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (limits stated) |
| Evidence sources | evidence/34-after-kpis/EVD-O-01-after-kpis.json (SHA-256 3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | O-R-05 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

O-X3: improvement must not be wholly attributed to the intervention. Here there is **no improvement in any operational measure**, so the question is reversed: could the *absence* of change hide a real effect?

| Confounder / limit | Effect |
|---|---|
| Static synthetic fixture | operational KPIs cannot respond to anything; a real effect, if any, is invisible, not absent |
| No measurement window | before and after cannot be separated in time |
| Proxy KPIs (F-57) | none measures a business outcome; K3 is an artefact of uniform random severities |
| Test effort vs system change | K9/K10 changes come from writing tests, not from the code improving operations |
| Author-run evaluation | the agent that built the system also graded it (TEVV-R-01); a defect the author could not imagine is not tested |
| No control group | no unit runs without the intervention |
| Seeded vs observed defects | K7/K8 are planted; quarantine rates are properties of the seed |

Causal reading allowed: control properties (identity, policy, AI containment, audit) changed **because the code changed**, shown by deterministic tests and attacks on the baseline and v2 builds. Nothing beyond that is claimed.
