# Production readiness decision

| Field | Value |
|---|---|
| Stage | R |
| Runbook step | R1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Issued by agent; NOT approved by any named person |
| Evidence sources | evidence/15-modernization/EVD-R-01, EVD-R-02; all stage gates; go-no-go-criteria.md |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-01, 02, 03, 04, 05, 07, 20 |
| Residual risks | See residual-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Decision
**NO-GO for production on real data. CONDITIONAL GO for a controlled pilot on synthetic data, local or test environment, with the operator in every role slot.** This is the agent's recommendation, issued under a PROVISIONAL operating contract. It is **not an approval**: no named person has approved anything in this engagement (OQ-05, GOV-01). [VF]

## What is ready (verified, with evidence)
- The delivered defects that mattered most no longer reproduce: 12-attack red team, **10 succeeded on the delivered baseline, 0 succeed on the transformed build** (`evidence/26-tevv/EVD-L-03-redteam-baseline.json` (sha256 `690911c90695c307f620ac56aec88e8d0da9732b4f6405dbf9c381e38df9213f`); `evidence/26-tevv/EVD-L-03-redteam-v2.json` (sha256 `b6f65533d6d71145d1d98da52ee5886590871091c704bc514e07984327d03356`)).
- Quick-start works: baseline `pytest -q` exit 2 (`evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt` (sha256 `74e85bd8cec2ade87fc4ccf8a95b40552928010bfd689e761b21868fdf541581`)); transformed build 176 passed, 1 skipped, 7 expected xfail on Python 3.11 and 3.13, apps+etl coverage 96.9%, ruff, mypy, secret scan clean (`evidence/15-modernization/EVD-R-01-final-verification.txt` (sha256 `510e7971405b8f1f097dc385fcbe5cb700a6ed54d5011e7108a64bc83b7db92f`)).
- **CI ran on GitHub and is green on Python 3.11 and 3.14**, including OPA policy tests. The first run failed on a real coverage-gate defect, which was fixed (D-013) (`evidence/15-modernization/EVD-R-02-ci-run-1-failed.txt` (sha256 `23711892040269c52df2765ce8ae5dfa695369196cf274543ce27f000826a70c`); `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`)).
- Audit is tamper-evident and one business event was reconstructed end to end (`evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`)); five failure drills pass (`evidence/28-resilience/EVD-M-03-drills/summary.json` (sha256 `eec9e4e654674cf439c8ed4a888514c0e2485679fdd7f61bc513294b343f00ac`)); backup restore demonstrated on the fixture (`evidence/30-release/EVD-N-03-backup-restore.json` (sha256 `a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e`)).
- Supply chain: SBOM runtime 21 and dev 58 components, 0 dependency vulnerabilities, 12 static-analysis findings dispositioned (`evidence/27-hardening/EVD-M-01-pip-audit-runtime.json` (sha256 `97b9424c9b9bdb1905993a93f0557a2705afc63f2c4421c46d1079d3e24d756d`)).

## What is not ready
| Area | State | Gate |
|---|---|---|
| Owners, approvers, sponsor | none named; 0 of 12 risk acceptances signed | G8, G9 |
| Platform and identity provider | not chosen; HS256 shared-secret tokens; JWKS verifier is a stub | G10 |
| Independent review | none; one agent built, tested and graded the work | G11 |
| Regulatory scope and real-data rules | unresolved (RA-01, OQ-04, OQ-21) | G12 |
| Real AI model | never called; all AI evidence is the deterministic provider; model portability tested once on a subset with a same-vendor model: access, lookup, guardrail and audit carried over, AI-output fidelity did not (Stage Q) | G2 (partial) |
| Business value | no business KPI is measurable; verified monetary benefit nil; NPV negative at fixture volume | n/a |
| Secrets | removed from the tree, **not revoked**, still in git history of a **public** repository | RA-07, GOV-07 |
| Branch protection | not enabled on `main` (GitHub API: HTTP 404 "Branch not protected") | DEBT-01 |
| Infrastructure | Terraform provisions nothing; container image never built | M-X2, DEBT-06 |
| Tracing, collector, alert recipients | not implemented / never run / none named | G8 |

## Go / no-go criteria (fixed before this decision in `docs/30-release/go-no-go-criteria.md`)
| # | Criterion | Mandatory | State on 2026-10-08 |
|---|---|---|---|
| G1 | Tests pass, coverage at or above floor | yes | **PASS** 176 passed; 96.9% (apps+etl); CI green |
| G2 | Evaluation at thresholds | yes | **PASS (deterministic provider only)**; 192 cases, 0 failures; real model untested |
| G3 | No original defect re-exploitable | yes | **PASS** 0 of 12 |
| G4 | No known critical/high dependency vulnerability | yes | **PASS** |
| G5 | Audit tamper-evident; reconstruction shown | yes | **PASS (author-run)** |
| G6 | Backup restore shown | yes | **PASS (repo level)** |
| G7 | Rollback defined and rehearsed | yes | **PARTIAL** defined; no cutover exists |
| G8 | Alerts routed to named humans | yes | **FAIL** |
| G9 | Named approver and risk owners | yes | **FAIL** |
| G10 | Platform and IdP exist | yes (production) | **FAIL** |
| G11 | Independent evidence review | yes | **FAIL** |
| G12 | Compliance resolved | yes (real data) | **FAIL / UNRESOLVED** |

For a pilot on synthetic data G1-G7 apply and are met at repository level. For production G8-G12 apply and are not met, so the answer cannot be GO.

## Conditions for the pilot (each has a role owner; no person is named)
1. A person accepts the operator-in-every-slot arrangement (sponsor). 2. Repository visibility decided and the H3 credentials revoked or confirmed fake (repository owner). 3. Branch protection and required CI checks turned on. 4. No real personal data and no hosted model until RA-01 and OQ-02 are closed. 5. One independent reviewer reads this pack.

## Risk accepted, and by whom
**None.** A risk is accepted by a named person. The 12 proposed acceptances (RA-01 to RA-12) are all unsigned; this document does not accept them on anyone's behalf.

## Deferred work
See `residual-risks.md` (DEBT-01 to DEBT-14 with current status, TEVV-R, RA, N-R items) and `docs/final-prd/implemented-vs-deferred.md`.
