# Stakeholder Needs Matrix

| Field | Value |
|---|---|
| Stage | B: Qualification, Stakeholders and Problem Framing (Spine 2) |
| Runbook step | B2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/ (A4, A5, A6 packs); runbook/04-OPEN-QUESTIONS-REGISTER.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Stakeholder | Need | Concern | Source class |
|---|---|---|---|
| CTO | Clear verdict with proof | Hidden risk, unverifiable claims | [ASM] |
| Business Sponsor | Measurable value | AI cost without outcome | [INF] from `transformation-roadmap.md` |
| Security Owner | Least privilege, audit, secrets | Role header trust, planted credentials | [VF] code |
| Data Owner | Trusted keys and quality | Duplicate keys, REC-0001 collision | [VF] A4 |
| SRE Owner | Telemetry, SLOs | No metrics, no correlation | [VF] otel-notes |
| Compliance Owner | Reconstructable decisions | Audit lacks actor | [VF] audit.py |
| Dispatcher / fleet manager | Right record, right status | Silent first-row fallback | [VF] domain_service.py |
| Carrier partner | Idempotent bookings | Duplicate bookings | [VF] data |
Needs are inferred from artifacts; no stakeholder was interviewed [UNK].
