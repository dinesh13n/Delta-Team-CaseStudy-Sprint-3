# Communications plan

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (no named contacts) |
| Evidence sources | evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Audience | When | Channel [UNK] | Owner |
|---|---|---|---|
| Incident team | on SEV-1/2 immediately; SEV-3 next day | team chat/pager | incident commander |
| Business owner | SEV-1/2 within 1 h; SEV-3 summary | email | incident commander |
| Compliance owner | any incident touching personal data | email + call | security owner |
| Users (dispatchers) | when AI is switched off or degraded | notice in the operations view / chat | product owner |
| Regulators/customers | only if the compliance owner decides an obligation exists (RA-01: obligations unknown) | per counsel | compliance owner |

## Template (filled from the simulation)
```
Subject: AI summary guardrail blocked a model output (SEV-3)
What happened: <time UTC> a model summary for <record> contained a customer identifier. The output guardrail replaced it with a deterministic summary.
Impact: no customer identifier left the system; <n> suggestion record(s) exist; no shipment, route or booking was changed.
Action taken: AI switched off, evidence preserved (tip hash <prefix>...), evaluation re-run (0 failures), AI re-enabled with the deterministic provider only.
Next: owner to decide whether the model may be re-enabled after a TEVV re-run.
```
Rules: facts only, UTC times, no speculation about cause until confirmed, no personal data in the message, one named owner for updates.
