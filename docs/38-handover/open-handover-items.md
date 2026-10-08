# Open handover items

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (list) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. Name owners for every RACI row (OQ-05).
2. Revoke credentials found in history (5 distinct, 10 findings).
3. Choose platform (OQ-01), IdP (OQ-07), model (OQ-02/03); build and scan the image; first CI run; apply branch protection.
4. Collector scraping a deployed instance; route alerts to named people.
5. Scheduler for ETL, drift check, backups.
6. Data Owner rulings: BR-04, F-59, enum vocabulary (DEBT-15), event correlation id and shipment id.
7. Four-eyes on approvals and approval expiry (HC-R-01, HC-R-03).
8. Independent review of tests, evaluation and red team (TEVV-R-01).
9. Compliance obligations (RA-01) and sign the 12 risk acceptances.
10. Audit growth, rotation and a shared audit store before more than one replica.
11. Tracing (OpenTelemetry) once a provider call exists.
12. Business baseline (CA-01) and a case identifier.
13. Accessibility audit and the Playwright spec run through `npx` (only a Python equivalent was run).
14. CTO ratification of D-009.
