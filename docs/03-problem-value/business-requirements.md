# Business Requirements

| Field | Value |
|---|---|
| Stage | B: Qualification, Stakeholders and Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | runbook/01-BASELINE-ASSESSMENT.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Requirement | Persona | Finding link |
|---|---|---|---|
| BR-1 | Return exactly the requested record or a clear not-found, never a different one | dispatcher, support | F-30, F-33 |
| BR-2 | Each business record has a unique, validated identifier | all | F-30..F-38 |
| BR-3 | Access depends on who the person is and what they are doing | all | F-17..F-20 |
| BR-4 | Every decision is recorded with actor, time, request and basis | compliance | F-42..F-46 |
| BR-5 | Invalid or duplicate incoming data is held aside, counted and reported | data owner | F-35, F-36 |
| BR-6 | Any automated recommendation is bounded, explainable, reviewable and costed | sponsor, AI governance | F-25..F-29 |
| BR-7 | Secrets are never stored in source | security | F-09..F-12 |
| BR-8 | The system can be rebuilt and tested from a clean checkout | engineering | F-02, F-03 |
