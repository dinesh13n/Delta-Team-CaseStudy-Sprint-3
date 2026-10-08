# Escalation model

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (no contacts) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Severity per `docs/29-incident-bcdr/incident-severity-matrix.md`. Path: detector (alert or user) → on-call SRE → Dev lead (code) or Data Owner (data) → Security Owner (any leak/auth/audit issue) → Sponsor (SEV-1, or any customer-impacting exposure) → Compliance (any personal-data exposure). **No names, numbers or channels exist**; the path is a role chain only.
