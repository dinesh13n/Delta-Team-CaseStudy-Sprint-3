# Requirement disposition matrix

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | evidence/ (cited per row) |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Every original requirement from the Initial PRD (FR, BR, NFR, success criteria) plus the scope items the delivery or the Challenge Guide implied is classified **Delivered / Changed / Deferred / Rejected / Superseded**. No row is unclassified. "Delivered" carries its limit in the rationale; it never means "proven in production".

Counts: Changed 2, Deferred 7, Delivered 34, Rejected 3, Superseded 2 (total 48 rows).

| ID | Requirement | Disposition | Rationale / limit | Evidence |
|---|---|---|---|---|
| FR-01 | Exact record by key or 404 | **Delivered** | tests/test_record_lookup.py; RT-05; EVD-H-10 P3 | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`) |
| FR-02 | Reject non-key and cross-entity identifiers (REC-0001) | **Delivered** | key patterns; 422; RT-06; owner intent OQ-15 unconfirmed | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`) |
| FR-03 | Verified identity on every endpoint but liveness/readiness | **Changed** | signed HS256 token, not IdP-backed (change-log #14); JWKS verifier fail-closed stub | `evidence/15-modernization/EVD-H-04-negative-access-tests.txt` (sha256 `c724516d79f2e15cce8017516c2a82a30c2eb663c4fe08b5cc83b181213eb2eb`) |
| FR-04 | Per persona, entity, field, purpose access decision | **Delivered** | policy engine from access-semantics; scope narrowing by hub/fleet not enforceable (DEBT-05) | `evidence/15-modernization/EVD-H-04-policy-allow-deny-matrix.csv` (sha256 `f838baffa93da9043a972b23f70f36a84f9442848d2805d4a2d029f4a96ad25a`) |
| FR-05 | 401/403 problem body, denial audited | **Delivered** | error handlers; audited denials | `evidence/15-modernization/EVD-H-04-negative-access-tests.txt` (sha256 `c724516d79f2e15cce8017516c2a82a30c2eb663c4fe08b5cc83b181213eb2eb`) |
| FR-06 | Validate, quarantine with reasons, report, non-zero exit above threshold | **Delivered** | ETL quarantine; ratio ceiling 5% | `evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`) |
| FR-07 | Versioned curated layer from immutable fixture | **Delivered** | data/curated, load_id; fixture byte-identical | `evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`) |
| FR-08 | Detect multiple active bookings per shipment at intake | **Delivered** | rule flag/quarantine | `evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`) |
| FR-09 | Exception summary with sources, confidence, model, prompt version, tokens, cost | **Delivered** | deterministic provider only; tokens are estimates; no real model | `evidence/15-modernization/EVD-H-07-ai-gateway-results.json` (sha256 `38fe45eb845bc0d5c3aebbc45d155f9d0a2997ee758cf39c497312d245b1aec6`) |
| FR-10 | Prompts from allow-listed fields; free text as data | **Delivered** | sanitize.py; no str.format on data | `evidence/19-intelligence/EVD-J-03-eval-run2-after-remediation.json` (sha256 `3f729728c7e621fc037ceb2cbe9c829882f019fa74ba8119302bc8bc46bd5f3d`) |
| FR-11 | Schema-validated output, abstention, deterministic fallback | **Delivered** | gateway; 0 schema failures in 192 cases | `evidence/26-tevv/EVD-L-02-final-eval-run.json` (sha256 `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e`) |
| FR-12 | Human approve/reject with approval id before action | **Delivered** | self-approval possible (HC-R-01); approvals never expire (HC-R-03) | `evidence/23-human-control/EVD-K-01-human-control-tests.txt` (sha256 `ebd91a777fa2223e03d14f0f9a949ecafa3b80e17a0da4cf179519ccde821828`) |
| FR-13 | Audit with actor, correlation id, tenant, resource, policy decision, model/prompt version, hash chain | **Delivered** | audit v2; local file sink | `evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`) |
| FR-14 | Correlation id per request carried everywhere | **Delivered** | new events only; history unchanged | `evidence/15-modernization/EVD-H-08-trace-sample.json` (sha256 `5b79ef4cf9cc76f6b5d6e39dd9300d709b0e7633f933e1c21029adc4b07a1e88`) |
| FR-15 | Liveness and readiness reflecting data layer | **Delivered** | /health unchanged, /ready dependency check | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`) |
| FR-16 | Complete OpenAPI for every endpoint | **Delivered** | 10 operations; drift test fails on mismatch | `evidence/12-specs/EVD-F-03-openapi.yaml` (sha256 `6016a47d34dccadb44c6f7237cd3077f44edce88f5029801d5d1249272215c87`) |
| FR-17 | Operational and AI metrics | **Delivered** | /metrics, 53 series; token metrics are estimates | `evidence/32-finops/EVD-N-04-finops-model.json` (sha256 `207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac`) |
| FR-18 | Thin read-only operations view (OQ-06) | **Delivered** | static view in apps/web/public; Chromium run 10/10 (scripted) | `evidence/20-application/EVD-J-04-browser-e2e.json` (sha256 `79064bd7b6b0df59ac517e1d2bed3e32087836a44e8bdecb781b8b2fbb3c49bd`) |
| FR-19 | Config and secrets from environment; refuse to start without secrets outside local | **Delivered** | tests/test_config.py | `evidence/15-modernization/EVD-H-03-secret-scan.json` (sha256 `9be399823ccf9be244917852a3f19b4ee67b5e5d2c813fae5b7f4c4fd20c4dab`) |
| FR-20 | Installable and testable from a clean checkout with locked dependencies | **Delivered** | hash-pinned locks; npm lock; CI green | `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`) |
| BR-1 | Exactly the requested record or clear not-found | **Delivered** | see FR-01 | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`) |
| BR-2 | Unique validated identifiers | **Delivered** | see FR-02, FR-06 | `evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`) |
| BR-3 | Access depends on who and what | **Delivered** | see FR-03..FR-05; IdP deferred | `evidence/15-modernization/EVD-H-04-negative-access-tests.txt` (sha256 `c724516d79f2e15cce8017516c2a82a30c2eb663c4fe08b5cc83b181213eb2eb`) |
| BR-4 | Every decision recorded | **Delivered** | see FR-13 | `evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`) |
| BR-5 | Invalid or duplicate data held aside, counted, reported | **Delivered** | see FR-06 | `evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`) |
| BR-6 | Recommendations bounded, explainable, reviewable, costed | **Delivered** | costed with estimates only; explainability via recorded facts | `evidence/26-tevv/EVD-L-02-final-eval-run.json` (sha256 `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e`) |
| BR-7 | No secrets in source | **Delivered** | working tree clean; history not rewritten or revoked (RA-07) | `evidence/15-modernization/EVD-H-03-secret-scan.json` (sha256 `9be399823ccf9be244917852a3f19b4ee67b5e5d2c813fae5b7f4c4fd20c4dab`) |
| BR-8 | Rebuild and test from clean checkout | **Delivered** | CI green on 3.11 and 3.14 | `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`) |
| NFR-1 | Read p95 <= 500 ms | **Delivered** | in-process/loopback only; p95 6-34 ms; no deployment measure | `evidence/28-resilience/EVD-M-02-load-probe.json` (sha256 `fe069284369b402e6ad264b65bcec643eafb054804d6877036f375ae34d212af`) |
| NFR-2 | Availability >= 99.5% test window | **Deferred** | no deployment to probe | `evidence/28-resilience/EVD-M-02-load-probe.json` (sha256 `fe069284369b402e6ad264b65bcec643eafb054804d6877036f375ae34d212af`) |
| NFR-3 | 100% of new events carry a correlation id | **Delivered** | new events | `evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`) |
| NFR-4 | 100% audit records with actor and request id | **Delivered** | field coverage 10/10 | `evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`) |
| NFR-5 | 0 duplicate/blank mandatory in trusted store | **Delivered** | quarantine ratio 1.41% | `evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`) |
| NFR-6 | Coverage >= 80% | **Changed** | 96.9% on apps+etl; scripts/legacy removed from gate scope (D-013) | `evidence/15-modernization/EVD-R-01-final-verification.txt` (sha256 `510e7971405b8f1f097dc385fcbe5cb700a6ed54d5011e7108a64bc83b7db92f`) |
| NFR-7 | 0 credential matches in source | **Delivered** | working tree 0; history 10 | `evidence/15-modernization/EVD-H-03-secret-scan.json` (sha256 `9be399823ccf9be244917852a3f19b4ee67b5e5d2c813fae5b7f4c4fd20c4dab`) |
| NFR-8 | Clean-checkout pass | **Delivered** | CI | `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`) |
| NFR-9 | AI p95 <= 3,000 ms | **Deferred** | deterministic 0.95 ms; real model unmeasured | `evidence/26-tevv/EVD-L-02-final-eval-run.json` (sha256 `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e`) |
| NFR-10 | AI cost <= 2.25 cost units/request | **Deferred** | no real model; estimates only | `evidence/32-finops/EVD-N-04-finops-model.json` (sha256 `207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac`) |
| SC-1..SC-8 | Success criteria mapped to BR-1..BR-8 | **Delivered** | see matching BR rows; SC-4, SC-6 for new events and deterministic provider | `evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv` (sha256 `24dc4df12754670d842a7f1d8fb2d8dfa03eb8214dd35758a7e26577a6e774d1`) |
| ADR-0001 | Keep legacy batch beside FastAPI | **Superseded** | ADR-0002 | `evidence/10-architecture/EVD-F-01-adr-index.txt` (sha256 `4cae717c359d65180ef203aeda719971c6f37e405a160e033495cc8bcf5d450d`) |
| K4 def. | Non-null correlation share | **Superseded** | usable = non-null and non-empty (D-012) | `evidence/00-preflight/EVD-A-04c-correlation-recount.txt` (sha256 `c2600111796cca839e726d805f30ac37f26904872fdff92ceaebd1663716707c`) |
| FF-06 | Audit v1 feature flag | **Rejected** | would double audit write paths | `evidence/13-traceability/EVD-F-05-stage-f-exit-checks.txt` (sha256 `1df22f4e7472cff0bdb6e7bf8948a79ac0ffb468ca210b1d70278c32fa003f4e`) |
| Portal | Angular operator portal (delivered README claim) | **Rejected** | never existed; thin view replaces it (F-05) | `evidence/20-application/EVD-J-04-browser-e2e.json` (sha256 `79064bd7b6b0df59ac517e1d2bed3e32087836a44e8bdecb781b8b2fbb3c49bd`) |
| AI-1..3 | ETA Prediction, Route Optimization, Exception Copilot (delivered docs) | **Deferred** | not implemented; no model | `evidence/08-ai-qualification/EVD-E-04-stage-e-checks.txt` (sha256 `56b7058b10ff961bc3091af9007b241a45b7f3ccc649790a6345f1f640e069c6`) |
| Agents | Agentic AI | **Rejected** | J6 not applicable; OQ-18 unresolved | `evidence/19-intelligence/EVD-J-03-eval-run1.json` (sha256 `831889be4bda61a9bdd8ed338a22318145df97be03376e7d7587985c4126e937`) |
| Portability | Semantic layer reproduces system under a second model (Challenge Guide) | **Changed** | run once on a four-behaviour subset with `claude-haiku-5-5`: safety behaviours carried over, AI-output fidelity did not (2 of 8 gates fail); eight specification gaps logged | `evidence/40-scale/EVD-Q-06-comparison.csv`; `evidence/40-scale/EVD-Q-01-preregistration.json` (sha256 `d050b98fe3a419f360f48be9edb646e952ccd3d08488cd5639d41556da875014`) |
| IaC | Real infrastructure as code | **Deferred** | OQ-01 unresolved | `evidence/15-modernization/EVD-R-01-final-verification.txt` (sha256 `510e7971405b8f1f097dc385fcbe5cb700a6ed54d5011e7108a64bc83b7db92f`) |
| Tracing | Distributed traces | **Deferred** | correlation id only | `evidence/31-observability/EVD-N-01-observability-validation.json` (sha256 `b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485`) |

Findings (62) are dispositioned separately in `evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv` (sha256 `24dc4df12754670d842a7f1d8fb2d8dfa03eb8214dd35758a7e26577a6e774d1`).
