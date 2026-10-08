# Residual risks and risk-owner table

| Field | Value |
|---|---|
| Stage | R |
| Runbook step | R1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft; owners UNRESOLVED |
| Evidence sources | docs/16-repo-validation/remaining-debt-register.md; docs/25-governance/risk-acceptance-register.md; docs/26-tevv/residual-tevv-risks.md; docs/31-observability/ |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Owners are **roles**. No person is named anywhere in this engagement; none was invented. "Acceptance" below means *proposed*. [VF]

## Risk-owner table
| ID | Risk | Severity (agent view) | Owner role | Accepted by | Cancelled if / due |
|---|---|---|---|---|---|
| RA-07 / DEBT-11 | Credential-shaped values (`Welcome123` and four others) remain in git history of a **public** repository; nothing revoked | High | Repository owner + Security | nobody | before any deployment; decide visibility now (GOV-07) |
| RA-01 | Regulatory scope unresolved | High for real data | Sponsor + Compliance | nobody | before any real data |
| RA-06 / TEVV-R-01 | Builder and grader are the same agent; no independent review | High | Release approver | nobody | blocks unconditional GO |
| RA-02 | HS256 shared-secret identity; JWKS stub | High if networked | Security | nobody | before any networked deployment |
| RA-09 / TEVV-R-02 | Real model untested; zero-tolerance thresholds only valid for the deterministic provider | High before a model | AI governance | nobody | before enabling a model |
| (Q) | Model portability **partly demonstrated** (one same-vendor subset run: safety behaviour yes, AI-output fidelity no; eight specification gaps) | Medium | AI governance | nobody | close IMP-Q04..IMP-Q10, repeat with another vendor family, three runs (IMP-Q12) |
| RA-04 / HC-R-01 | No four-eyes: the requester can approve their own suggestion | Medium | Product | nobody | before any action integration |
| RA-12 / DEBT-01 | CI now runs and is green; **branch protection still off** | Medium | Repository owner | nobody | now |
| DEBT-06, F-48 | Terraform provisions nothing; image never built | Medium | Platform | nobody | with OQ-01 |
| N-R | No tracing; collector and alerts never run; no recipients | Medium | SRE | nobody | before deployment |
| DEBT-04 | Audit sink is a local file; hash chain detects edits, cannot prevent deletion of the tip | Medium | Platform | nobody | M2 / platform |
| DEBT-08, DEBT-09 | Business rule BR-04 violated by 354 of 354 rows; actual>declared weight on 171 rows; meaning unknown | Medium | Business owner | nobody | before production |
| F-42 | Historical event stream still 1,992 of 3,000 events without a usable correlation id | Low (history) | Data owner | nobody | n/a |
| (value) | No business KPI measurable; NPV negative at fixture volume | Medium | Sponsor | nobody | measure review time first |
| RA-03, RA-05, RA-08, RA-10, RA-11 | purpose defaulting; approvals never expire; stale_gps undetectable; retention undefined; in-memory rate limit | Low-Medium | see register | nobody | see `risk-acceptance-register.md` |
| TEVV-R-04..08 | constructed datasets; usefulness on real vocabulary; Playwright spec not run via npx; no accessibility audit | Low-Medium | see register | TEVV-R-04 "ACCEPTED for pilot" by the Delta-Team lead role only | |

## Debt register status (from H11, updated 2026-10-08)
DEBT-01 **partly closed** (CI ran, green; protection off). DEBT-02..14 unchanged. DEBT-12 legacy shims remain (`services/audit.py`, `domain_service.py`; the latter is still imported by one legacy comparison path in `main.py`).

## Evidence of the open items
`evidence/16-repo-validation/EVD-H-11-dependency-audit.json` (sha256 `97b9424c9b9bdb1905993a93f0557a2705afc63f2c4421c46d1079d3e24d756d`); `evidence/15-modernization/EVD-H-03-secret-scan-history.json` (sha256 `473b47bb982b7ab65985c869a7f35068253b7c3719d610e9ad90ed8f85849a4c`) (10 history findings).
