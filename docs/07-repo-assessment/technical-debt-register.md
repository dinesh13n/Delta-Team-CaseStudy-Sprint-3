# Technical Debt Register

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 7 repository assessment) |
| Runbook step | C7 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | C2-C6 documents; runbook/01-BASELINE-ASSESSMENT.md findings register; direct reading of the subtree; evidence/07-repo-assessment/EVD-C-07-findings-index.json |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Cross-reference to every finding (F-01 to F-57 from Document 01; F-58 to F-60 added during Stage C; D-010).

| ID | Severity | Summary | Rubric |
|---|---|---|---|
| F-01 | S1 | The repository is not under version control | R1, 3 |
| F-02 | S2 | The documented test command cannot run | R1, 4 |
| F-03 | S3 | The documented run command is wrong | R1 |
| F-04 | S2 | No dependency lockfile for either stack | R2 |
| F-05 | S2 | Documentation claims a portal that does not exist | R1, 4 |
| F-06 | S3 | The frontend lint gate is "lint": "echo scaffold" — a no-op that reports success. | R2 |
| F-07 | S2 | No containerisation or environment definition: no Dockerfile, no compose file, no devcontainer | R2 |
| F-08 | S2 | No change-control surface: no CONTRIBUTING.md, no PR template, no CODEOWNERS, no branch-protection evidence. | R3 |
| F-09 | S1 | A database password is hardcoded in source | R3 |
| F-10 | S1 | .env.example ships a complete DSN with embedded credentials: postgresql://app_shared:Welcome123@localhost:5432 | R3 |
| F-11 | S2 | .env.example ships AI_GATEWAY_KEY=sk-workshop-hardcoded-example — a key-shaped literal in a committed file, te | R3 |
| F-12 | S1 | .env.example ships OT_VENDOR_TOKEN=replace-me-but-currently-shared — the comment itself documents an active sh | R3 |
| F-13 | S2 | .env.example sets LOG_LEVEL=DEBUG as the default, meaning verbose logging of operational payloads is the out-o | R3 |
| F-14 | S1 | No secret detection anywhere: no scanner in CI, no pre-commit hooks, no rotation policy | R3 |
| F-15 | S2 | The IaC emits a credential artifact | R3 |
| F-16 | S2 | No encryption posture exists: no TLS configuration, no at-rest statement, no key management, no field-level ha | R3 |
| F-17 | S1 | Authorisation is a client-supplied HTTP header | R3 |
| F-18 | S1 | The role check is a flat five-element allow-list with no resource, tenant, facility, purpose or risk scoping | R3 |
| F-19 | S1 | The allow-list contains a persona from another domain | R1, 3 |
| F-20 | S1 | The AI endpoint has no authorisation check whatsoever | R3 |
| F-21 | S1 | policy/opa/access.rego is role-only (admin → all, operator → read) | R3 |
| F-22 | S1 | Prompt injection surface | R3 |
| F-23 | S2 | Using str.format() on attacker-influenceable content is additionally a format-string injection surface: brace  | R3 |
| F-24 | S1 | The system self-reports that no guardrail exists: the response literal is "guardrail_status": "not_enforced". | R3 |
| F-25 | S1 | No output schema validation | R3 |
| F-26 | S1 | No human approval gate | R3 |
| F-27 | S1 | Model provenance is a module constant (MODEL_VERSION = "local-sim-v1") | R3 |
| F-28 | S2 | Token accounting is fabricated: token_estimate = len(prompt.split()) * 2 | R2, 3 |
| F-29 | S1 | The AI output is not derived from the record's meaning | R1, 4 |
| F-30 | S1 | Cross-entity primary-key collision | R1, 2 |
| F-31 | S1 | Record lookup scans every column, not the key | R2 |
| F-32 | S1 | A missed lookup silently returns the wrong record | R1, 2 |
| F-33 | S2 | Three duplicate business keys in every dataset, at a consistent *-00004, *-00013, *-00019 pattern (e.g | R1 |
| F-34 | S2 | One fully-blank mandatory row in every dataset — every non-key column empty (10 blank columns in shipments.csv | R1 |
| F-35 | S2 | One impossible timestamp per timestamped dataset: 1900-01-01T00:00:00 in shipments.promised_at, tracking_event | R1 |
| F-36 | S2 | tracking_events.confidence spans 0.001–1.42 | R1, 2 |
| F-37 | S1 | No semantic layer: categorical columns are polluted with workflow-status vocabulary | R1, 2 |
| F-38 | S2 | Referential integrity is unenforced | R1, 2 |
| F-39 | S1 | A retry storm is already visible in the data | R2 |
| F-40 | S2 | ETL counts defects and discards them | R2 |
| F-41 | S2 | The ETL has no run identifier, watermark or idempotency key | R2 |
| F-42 | S1 | About one third of the event stream cannot be correlated | R1, 3 |
| F-43 | S1 | The audit event records only ts, action and details | R3 |
| F-44 | S1 | The audit sink is a local file written by the application itself — <repo>/logs/audit.log, appended in-process | R3 |
| F-45 | S2 | datetime.utcnow() yields a naive timestamp with no timezone marker | R3 |
| F-46 | S1 | No tracing, no metrics, no SLOs, no dashboards-as-code, no alerting, no error budget | R3 |
| F-47 | S2 | CI executes commands but produces no evidence | R2, 3 |
| F-48 | S2 | The Terraform is a local_file resource with no provider, no backend, no state management and no infrastructure | R2 |
| F-49 | S2 | supply-chain/dependency-risk-register.md correctly names "no SBOM" and "no provenance" as targets, but no SBOM | R2, 3 |
| F-50 | S2 | The API contract omits both business endpoints | R2, 4 |
| F-51 | S2 | The characterization test characterises nothing | R1 |
| F-52 | S2 | tests/playwright/operations.spec.ts asserts that body is visible against an application that does not exist (F | R4 |
| F-53 | S2 | A known architectural divergence is documented and unmanaged | R1, 2 |
| F-54 | S2 | Data remediation will break the repository's own contract test | R1, 2 |
| F-55 | S3 | scripts/sanity_check.py hard-requires the paths docs/transformation-roadmap.md, docs/domain-specific-spec.md,  | R2 |
| F-56 | S2 | The incident runbook declares itself *"intentionally incomplete"* | R3 |
| F-57 | S2 | No business KPI data exists | R1, 4 |
| F-58 | S3 | ai_invocations.csv also has an orphan shipment reference (REC-0001 row); not in the original register | R1 |
| F-59 | S3 | 171 of 351 shipments have actual weight above declared weight (meaning unknown) | R1 |
| F-60 | S2 | data/README.md claims untrusted text payloads for prompt-injection testing; no free-text field exists (max length 19), so injection test data must be authored | R1,3 |
| F-61 | S3 | routes.weather_risk holds numeric 1.42 in a categorical field | R1, 2 |
| F-62 | S3 | Every dataset has one malformed key *-BAD1 | R1, 2 |
