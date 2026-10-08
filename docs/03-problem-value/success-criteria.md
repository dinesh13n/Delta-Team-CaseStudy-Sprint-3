# Success Criteria

| Field | Value |
|---|---|
| Stage | B: Qualification, Stakeholders and Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/ (A4, A5, A6 packs); runbook/04-OPEN-QUESTIONS-REGISTER.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Criterion | Measure | Business requirement | Owner (role) |
|---|---|---|---|---|
| SC-1 | Lookup correctness | wrong or fallback record returned = 0 in tests | BR-1 | Data Owner UNRESOLVED |
| SC-2 | Identifier integrity | duplicate/cross-entity keys accepted = 0 | BR-2 | Data Owner UNRESOLVED |
| SC-3 | Access control | unauthorised requests denied in 100% of test cases | BR-3 | Security Owner UNRESOLVED |
| SC-4 | Traceability | 100% new events carry correlation id and actor | BR-4 | Compliance Owner UNRESOLVED |
| SC-5 | Data intake | malformed rows quarantined and counted, none dropped silently | BR-5 | Data Owner UNRESOLVED |
| SC-6 | Automation governance | every recommendation has source, version, cost and approval record | BR-6 | AI Governance Owner UNRESOLVED |
| SC-7 | Secrets | 0 hardcoded credentials | BR-7 | Security Owner UNRESOLVED |
| SC-8 | Rebuild | clean-checkout tests pass | BR-8 | Repository Owner UNRESOLVED |
Failure criteria: any of the above unmet at the release gate; any real credential or personal data found.
