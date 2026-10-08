# Compliance control matrix

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | compliance-obligations.md |
| Assumptions | See body |
| Unresolved issues | OQ-04, OQ-05 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Maps each candidate obligation to the control that exists, the evidence, the owner (role) and the approval point.

| Obligation | Control in the system | Evidence | Owner (role) | Approval point | Gap |
|---|---|---|---|---|---|
| CO-01, CO-02 minimisation, security | masking, forbidden fields, TLS (platform), audit | PIA, EVD-K-02 | Compliance Owner [UNK] | R1 | retention, subject rights |
| CO-03 worker monitoring | location restricted to fleet roles with purpose; never in AI or logs | policy tests | HR / Labour counsel [UNK] | before any live GPS | notice and consultation not addressed |
| CO-04 customs records | audit chain, record lookup | audit tests | Customs lead [UNK] | n/a | record content rules unknown |
| CO-05 cold chain | field present; no rule enforced | – | Quality owner [UNK] | – | no control (not in scope of pilot) |
| CO-06 safety | restricted-zone flag; no assignment code | BR-06 | Operations safety [UNK] | – | override record missing |
| CO-07 AI duties | human approval, transparency fields, model/system card, register | K1, cards | AI governance owner [UNK] | R1 | classification not done |
| CO-08 transfer | none (no hosted model) | – | Compliance Owner [UNK] | before OQ-02 closes | open |
| CO-09 record keeping | evidence retention policy (proposal) | policy | Records owner [UNK] | R1 | periods unknown |

[VF] Every row names a *role*. No row names a person because no person was provided (OQ-05).
