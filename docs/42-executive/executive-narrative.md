# Executive narrative

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | production-evidence-pack.md; stage gates A-Q |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## In one paragraph
A logistics operations repository arrived that could not run its own quick-start, trusted a client-supplied role header, answered AI requests with no authorisation or guardrail, returned the wrong record when a lookup missed, and could not reconstruct what happened. We froze its behaviour, found and ranked 62 problems, replaced the unsafe paths with tested controls, and proved the change with a red team that succeeded 10 times out of 12 against the original and 0 out of 12 against the result. What we did **not** achieve: any measurable business benefit, any test with a real AI model, any deployment, any named owner, any independent review. The honest status is a controlled pilot on synthetic data, not production.

## The path (claim → evidence)
| Step | Claim | Evidence |
|---|---|---|
| Baseline | Delivered quick-start fails (exit 2, missing `httpx`; wrong module path) | `evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt` (sha256 `74e85bd8cec2ade87fc4ccf8a95b40552928010bfd689e761b21868fdf541581`) |
| Root causes | Five root causes; four confirmed with high confidence, one (partial modernisation ownership) plausible pending an owner interview | `docs/06-root-cause/confirmed-root-causes.md` (sha256 `43562287b1b5a1823ac88bfec961b7d015d084c4ae29f94d125e4b018511ac66`) |
| Intervention choice | One of ten interventions keeps GenAI (suggest-only); seven are deterministic; two deferred | `docs/08-ai-qualification/qualification-decision.md` (sha256 `10efdef410e047bffe50a85c53e29258d0ed66749e1193ac36ee2cf27e55af69`) |
| Architecture | Modular monolith with ports; ADR-0001 superseded | `docs/10-architecture/architecture-decision-summary.md` (sha256 `5086514f77705cb72310e397f890123eb4507251c2797808568b4cf4cba9256e`) |
| Control change | Red team 10/12 → 0/12 | `evidence/26-tevv/EVD-L-03-redteam-baseline.json` (sha256 `690911c90695c307f620ac56aec88e8d0da9732b4f6405dbf9c381e38df9213f`); `evidence/26-tevv/EVD-L-03-redteam-v2.json` (sha256 `b6f65533d6d71145d1d98da52ee5886590871091c704bc514e07984327d03356`) |
| Verification | 176 tests, 96.9% coverage on apps+etl, CI green on Python 3.11 and 3.14 | `evidence/15-modernization/EVD-R-01-final-verification.txt` (sha256 `510e7971405b8f1f097dc385fcbe5cb700a6ed54d5011e7108a64bc83b7db92f`); `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`) |
| Economics | Verified monetary benefit nil; NPV negative at fixture volume | `evidence/36-benefits/EVD-O-03-benefit-model.json` (sha256 `2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52`) |
| Decision | NO-GO production; CONDITIONAL GO synthetic-data pilot | `docs/42-executive/production-readiness-decision.md` (sha256 `acce0feb3526d2c29dc6eb76026e6c5fd5791fa0bf77016cdb72d38f79d23e78`) |

## Failures and corrections made along the way (see `lessons-learned.md`)
The runbook's own correlation-id figure was "corrected" wrongly and later restored (D-007 → D-012); the first red-team campaign was invalid because of a stale key; a doc claim of "12 of 12 attacks" was corrected to 10 of 12; CI had never run and its coverage gate failed on first execution (D-013); 58 evidence files had never been hash-registered.

## What we ask of the CTO
Name a sponsor and owners; decide repository visibility and rotate the credentials in its history; provide a platform, identity provider and a model of another vendor family if portability matters (a same-vendor subset test is done); assign one independent reviewer. Without those, nothing here can move past a local pilot.
