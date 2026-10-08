# Tabletop scenario TT-1

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Title.** A model's summary contains a customer identifier.
**Premise.** A model was enabled for a pilot. During a busy shift a manipulated or confused model includes the customer id of the shipment into its suggestion. The output guardrail should catch it.
**Injects (as executed).** 1. Model returns a summary with `CUS-00027`. 2. On-call asks: did anything leave the system? 3. Who saw it, was it approved? 4. Business asks: can dispatchers keep working? 5. Security asks for preserved evidence. 6. Owner asks: when can the model return?
**Objectives.** Test: detection signal, ability to reconstruct from audit alone, severity decision, containment without losing the core workflow, evidence preservation, recovery gate, communication.
**Format.** Scripted simulation against the real application (`scripts/tabletop_sim.py`), author-run. A real tabletop with at least an incident commander, an operator, a security owner and a business owner has **not** been held.
