# Evidence-driven delivery backlog

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | docs/13-traceability/* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Every item has an owner role, a test and a named evidence artifact. A person for each owner is UNRESOLVED (OQ-05).

| ID | Story | Increment | Owner (role) | Test | Evidence artifact | DoD evidence |
|---|---|---|---|---|---|---|
| DB-01 | Prompt registry and model configuration | INC-1 | AI lead | test_prompt_registry | EVD-J-01 | registry hash recorded |
| DB-02 | Evaluation datasets (golden/edge/adversarial/failure) committed before evaluation | INC-1 | AI lead | dataset schema test | EVD-J-02 | dataset hash + commit order |
| DB-03 | Evaluation run and intelligence gate | INC-1 | AI lead | eval runner | EVD-J-03 | results JSON |
| DB-04 | Thin operations view; replace vacuous e2e | INC-2 | Dev lead | test_ops_view | EVD-J-04 | test log |
| DB-05 | Carrier saga with idempotency and retry ceiling | INC-2 | Integration lead | test_carrier_saga | EVD-J-05 | test log |
| DB-06 | Autonomy matrix enforced in code | INC-3 | Governance lead | test_human_control | EVD-K-01 | test log |
| DB-07 | Threat model and security tests | INC-3 | Security lead | test_security_suite | EVD-K-02 | test log |
| DB-08 | PIA, model card, system card | INC-3 | Governance lead | document check | EVD-K-04 | files |
| DB-09 | TEVV execution and red team | INC-4 | QA lead | tevv runner | EVD-L-01, EVD-L-02 | results JSON |
| DB-10 | SBOM, provenance, resilience, failure injection | INC-5 | Platform lead | test_resilience | EVD-M-01..03 | files, log |
| DB-11 | SLOs, dashboards/alerts as code, incident reconstruction, release plan | INC-5 | SRE | reconstruction script | EVD-N-01, EVD-N-02 | output |
| DB-12 | After-KPIs, ROI model | INC-6 | Business analyst | kpi tests | EVD-O-01 | json |
| DB-13 | Operating model, handover, drift check | INC-6 | Delivery lead | drift script | EVD-P-01 | output |
| DB-14 | Second-model comparison | INC-7 | AI lead | comparison harness | EVD-Q-* | BLOCKED (no second model) |
| DB-15 | Production readiness decision and evidence pack | INC-7 | Delivery lead | pack index check | EVD-R-01 | index |
