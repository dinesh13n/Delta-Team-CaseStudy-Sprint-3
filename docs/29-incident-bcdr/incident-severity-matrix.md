# Incident severity matrix

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (proposal; owners UNRESOLVED) |
| Evidence sources | docs/24-security-privacy/threat-model.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Severity | Definition for this system | Examples | Response target [ASM] | Who is paged (role) |
|---|---|---|---|---|
| SEV-1 | forbidden or personal data reached an unauthorised person or system; unauthorised state change; audit chain compromised; credentials in use by an attacker | driver identifier or location shown to a non-entitled persona; forged tokens accepted; audit chain invalid | acknowledge 15 min, contain 1 h | incident commander, security owner, compliance owner |
| SEV-2 | core workflow down for all users, or an AI output with forbidden content **reached a response**; data corruption published | `/ready` failing for > 15 min; curated layer corrupted | acknowledge 30 min, contain 4 h | incident commander, platform on-call |
| SEV-3 | control worked but the event matters: guardrail replaced a leaking output; breaker open; stale data > limit; repeated auth failures | tabletop TT-1 | next business day | AI governance owner, platform on-call |
| SEV-4 | degraded convenience, no risk | AI off by choice, slow responses | backlog | – |

Escalation rule: a SEV-3 becomes SEV-2/1 the moment any evidence shows the control did not hold (forbidden value found in any response body or log).
Time targets are assumptions: no SLA, on-call roster or business impact figure exists (OQ-05, E2).
