# Brownfield → Production-Grade Transformation Runbook

## Document 01 — As-Is Baseline Assessment & Findings Register

| Field | Value |
|---|---|
| **Stage** | Runbook preparation (pre-execution) |
| **Document** | 01 — As-Is Baseline Assessment & Findings Register |
| **Version** | v1.0 |
| **Date** | 2026-10-08 |
| **Author / Agent** | AI-FDE Transformation Team — Delta-Team |
| **Status** | Draft for CTO review |
| **Method** | Static read of every file in the delivered repository; read-only statistical profiling of all seven datasets executed 2026-10-08. No repository file was created, modified or executed. |
| **Evidence classification** | Every finding below is a **Verified Fact** unless explicitly labelled Inference, Assumption or Unknown. |

---

## 1. Why this document exists

A runbook whose steps are not traceable to observed defects is a template, not a plan.
Every step in Document 02 cites one or more finding IDs from this register. If an executing
engineer cannot reproduce a finding, the step that depends on it should be challenged before
it is executed.

---

## 2. System under assessment

**Repository:** `07-logistics-shipment-fleet-routing-ops`
**Declared centre of gravity** (`README.md`, `docs/architecture/current-state.md`):
*Distributed workflows + real-time data + failure engineering + cost.*

**Three coexisting engineering generations** (`docs/architecture/current-state.md`):

| Generation | Location | Observed state |
|---|---|---|
| Legacy batch / file scripts | `legacy/`, `etl/` | Hardcoded shared DB credential; no quarantine; no idempotency |
| Modernising services | `apps/api/` | FastAPI; header-based authorisation; file-based audit |
| New AI capability | `apps/api/services/ai_gateway.py` | Unguarded, unvalidated, unauthenticated, simulated |
| Operator portal | `apps/web/` | Two TypeScript classes; no framework present despite README claim |

**Declared business flows** (`docs/domain-specific-spec.md`): booking→pickup; hub scan→route
assignment; carrier booking saga; exception investigation→delivery evidence.

**Declared personas:** `dispatcher`, `warehouse_ops`, `fleet_manager`, `driver`,
`customs_agent`, `customer_support`, `carrier_partner`, `ai_agent`.

**Declared AI capabilities** (`docs/architecture/current-state.md`): ETA Prediction, Route
Optimization, Exception Copilot. **Inference:** none of these three is implemented. The only
AI code path is a generic record summariser. The gap between declared and implemented AI
capability is itself a finding (F-29).

**Data estate** (`data/manifest.json`, verified by profiling):
six CSV datasets at 354 rows each (2,124 rows total) plus `events.jsonl` at 3,000 events.

---

## 3. Severity scale

| Severity | Definition |
|---|---|
| **S1 — Critical** | Would cause unauthorised access, unsafe automated action, data loss or an undefendable audit position if deployed as-is |
| **S2 — High** | Materially blocks a rubric criterion or a Delivery Spine completion gate |
| **S3 — Medium** | Creates maintenance, reproducibility or review friction; defensible to defer with an owner |
| **S4 — Low** | Hygiene; should be fixed opportunistically |

---

## 4. Findings register

### 4.1 Repository & engineering hygiene

| ID | Finding | Evidence | Sev | Rubric |
|---|---|---|---|---|
| **F-01** | **The repository is not under version control.** `git rev-parse --is-inside-work-tree` returns *"fatal: not a git repository"*. There is no `.gitignore`, `LICENSE`, `CODEOWNERS` or `SECURITY.md`. | Repository root listing; git probe 2026-10-08 | S1 | 1, 3 |
| **F-02** | **The documented test command cannot run.** `tests/test_api_contract.py` imports `fastapi.testclient`, which requires `httpx`. `httpx` is absent from `requirements.txt`. A clean `pip install -r requirements.txt && pytest -q` — the exact sequence in both `README.md` and `.github/workflows/ci.yml` — fails at collection. | `requirements.txt`; `tests/test_api_contract.py:1`; `import httpx` → `ModuleNotFoundError` | S2 | 1, 4 |
| **F-03** | **The documented run command is wrong.** `README.md` says `uvicorn apps/api.main:app`; the module path separator must be a dot (`apps.api.main:app`). | `README.md` Quick Start | S3 | 1 |
| **F-04** | No dependency lockfile for either stack. `requirements.txt` pins versions but there is no hash-pinned lock; `apps/web/package.json` declares empty `dependencies` and ships no lockfile. | `requirements.txt`; `apps/web/package.json` | S2 | 2 |
| **F-05** | **Documentation claims a portal that does not exist.** `README.md` describes an Angular portal "with components, services, route definitions, forms, and Playwright tests". `apps/web/` contains two plain TypeScript classes. There is no `angular.json`, no `main.ts`, no `index.html`, and `angular` appears nowhere except in `README.md`. | `README.md`; `apps/web/` tree; repository-wide grep for `angular` | S2 | 1, 4 |
| **F-06** | The frontend lint gate is `"lint": "echo scaffold"` — a no-op that reports success. | `apps/web/package.json` | S3 | 2 |
| **F-07** | No containerisation or environment definition: no `Dockerfile`, no compose file, no devcontainer. Reproducibility depends on an undocumented local Python installation. | Repository root listing | S2 | 2 |
| **F-08** | No change-control surface: no `CONTRIBUTING.md`, no PR template, no `CODEOWNERS`, no branch-protection evidence. | Repository root listing | S2 | 3 |

### 4.2 Secrets, configuration & cryptography

| ID | Finding | Evidence | Sev | Rubric |
|---|---|---|---|---|
| **F-09** | **A database password is hardcoded in source.** `SHARED_DB_PASSWORD = "Welcome123"` sits as a module-level constant in a file that is executable as `__main__`. | `legacy/reconcile_legacy.py:6` | S1 | 3 |
| **F-10** | `.env.example` ships a complete DSN with embedded credentials: `postgresql://app_shared:Welcome123@localhost:5432/workshop` — the same credential as F-09, confirming a shared privileged service account across generations. | `.env.example:1` | S1 | 3 |
| **F-11** | `.env.example` ships `AI_GATEWAY_KEY=sk-workshop-hardcoded-example` — a key-shaped literal in a committed file, teaching the pattern it should prevent. | `.env.example:2` | S2 | 3 |
| **F-12** | `.env.example` ships `OT_VENDOR_TOKEN=replace-me-but-currently-shared` — the comment itself documents an active shared-vendor-token practice. | `.env.example:4` | S1 | 3 |
| **F-13** | `.env.example` sets `LOG_LEVEL=DEBUG` as the default, meaning verbose logging of operational payloads is the out-of-the-box behaviour — material given the declared `location_data_overexposure` concern. | `.env.example:5`; `security/threat-model.md` | S2 | 3 |
| **F-14** | No secret detection anywhere: no scanner in CI, no pre-commit hooks, no rotation policy. Combined with F-01 (no `.gitignore`), a real `.env` file is committable. | `.github/workflows/ci.yml`; repository root | S1 | 3 |
| **F-15** | **The IaC emits a credential artifact.** `infra/terraform/main.tf` writes `shared_user=app_shared` into `generated-env.txt` on the local filesystem. | `infra/terraform/main.tf` | S2 | 3 |
| **F-16** | No encryption posture exists: no TLS configuration, no at-rest statement, no key management, no field-level handling for location data despite `location_data_overexposure` being a declared brownfield concern. | `security/threat-model.md`; repository-wide | S2 | 3 |

### 4.3 Identity, authorisation & policy

| ID | Finding | Evidence | Sev | Rubric |
|---|---|---|---|---|
| **F-17** | **Authorisation is a client-supplied HTTP header.** `x_user_role: str = Header(default="operator")` — there is no authentication at all; a caller self-asserts their role, and when the header is omitted the system defaults them to `operator`, which is on the allow-list. | `apps/api/main.py:9-10` | S1 | 3 |
| **F-18** | The role check is a flat five-element allow-list with no resource, tenant, facility, purpose or risk scoping. The repository's own comment concedes this: *"role check is broad and facility/tenant context is ignored"*. | `apps/api/main.py:11-12` | S1 | 3 |
| **F-19** | **The allow-list contains a persona from another domain.** `clinician` is in the permitted-roles list but is not one of the eight personas in `docs/domain-specific-spec.md`. This is unreviewed copy-paste sitting in the authorisation decision path. | `apps/api/main.py:12`; `docs/domain-specific-spec.md` | S1 | 1, 3 |
| **F-20** | **The AI endpoint has no authorisation check whatsoever.** `POST /ai/summarize/{record_id}` loads the record and invokes the model with no role test — it is strictly less protected than the read endpoint whose data it consumes. | `apps/api/main.py:19-24` | S1 | 3 |
| **F-21** | `policy/opa/access.rego` is role-only (`admin` → all, `operator` → read). It has no resource, purpose, scope or risk input; it has no tests; and **it is not referenced by any application code** — the policy engine is decorative. | `policy/opa/access.rego`; repository-wide grep | S1 | 3 |

### 4.4 AI trust boundary & governance

| ID | Finding | Evidence | Sev | Rubric |
|---|---|---|---|---|
| **F-22** | **Prompt injection surface.** The entire untrusted record is interpolated into the prompt: `PROMPT_TEMPLATE.format(record=record)`. `data/README.md` confirms the datasets deliberately contain "untrusted text payloads suitable for prompt-injection testing". | `apps/api/services/ai_gateway.py:5,9`; `data/README.md` | S1 | 3 |
| **F-23** | Using `str.format()` on attacker-influenceable content is additionally a **format-string injection** surface: brace sequences present in the data are evaluated by the formatter rather than treated as literal text. | `apps/api/services/ai_gateway.py:9` | S2 | 3 |
| **F-24** | **The system self-reports that no guardrail exists**: the response literal is `"guardrail_status": "not_enforced"`. | `apps/api/services/ai_gateway.py:18` | S1 | 3 |
| **F-25** | No output schema validation. The response is a hand-constructed dict; no Pydantic model, no JSON Schema, no refusal/abstention path, no unsafe-output handling. | `apps/api/services/ai_gateway.py:11-19` | S1 | 3 |
| **F-26** | **No human approval gate.** `"recommendation": "Review and approve before action"` is advisory prose returned in a payload; nothing in the system enforces a state transition requiring approval. The Challenge Guide's acceptance standard — *"AI recommendations must not silently become operational decisions"* — is not met. | `apps/api/services/ai_gateway.py:16` | S1 | 3 |
| **F-27** | Model provenance is a module constant (`MODEL_VERSION = "local-sim-v1"`). There is no prompt registry, no prompt version, no configuration hash, no input hash, no retrieval provenance. | `apps/api/services/ai_gateway.py:3` | S1 | 3 |
| **F-28** | Token accounting is fabricated: `token_estimate = len(prompt.split()) * 2`. No cost attribution, no per-request budget, no ceiling, no linkage to a business outcome. | `apps/api/services/ai_gateway.py:10` | S2 | 2, 3 |
| **F-29** | **The AI output is not derived from the record's meaning.** `"summary": "Synthetic summary for " + str(next(iter(record.values()), "unknown"))` returns the *first column value* of the row. Separately, the three AI capabilities declared in `docs/architecture/current-state.md` (ETA Prediction, Route Optimization, Exception Copilot) have no implementation anywhere in the repository. Any present claim about AI quality is unsupportable. | `apps/api/services/ai_gateway.py:14`; `docs/architecture/current-state.md` | S1 | 1, 4 |

### 4.5 Data quality, identity & semantics

All quantitative findings in this section were produced by read-only profiling on 2026-10-08
and are reproducible by Step C5.

| ID | Finding | Evidence | Sev | Rubric |
|---|---|---|---|---|
| **F-30** | **Cross-entity primary-key collision.** The identifier `REC-0001` is simultaneously the first-row primary key of *all six* datasets — it is a `shipment_id`, an `event_id`, a `vehicle_id`, a `route_id`, a `booking_id` and an `ai_call_id`. | Profiling 2026-10-08, first-row PK per file | S1 | 1, 2 |
| **F-31** | **Record lookup scans every column, not the key.** `load_record` tests `if record_id in row.values()` — a value-membership scan across all columns. An identifier can therefore match on a non-key field. Combined with F-30, record identity is non-deterministic. | `apps/api/services/domain_service.py:11-13` | S1 | 2 |
| **F-32** | **A missed lookup silently returns the wrong record.** `load_record` falls through to `return rows[0]`. The repository's own comment calls this out: *"silently returns first row, masking data defects"*. `tests/test_characterization.py` then asserts this behaviour is acceptable. | `apps/api/services/domain_service.py:15-16`; `tests/test_characterization.py` | S1 | 1, 2 |
| **F-33** | Three duplicate business keys in **every** dataset, at a consistent `*-00004`, `*-00013`, `*-00019` pattern (e.g. `SHI-00004`, `EVE-00013`, `BOO-00019`). | Profiling 2026-10-08 | S2 | 1 |
| **F-34** | One fully-blank mandatory row in **every** dataset — every non-key column empty (10 blank columns in `shipments.csv`, 9 in `tracking_events.csv`, 8 in `vehicles.csv` and `routes.csv`, 7 in `carrier_bookings.csv`, 8 in `ai_invocations.csv`). | Profiling 2026-10-08 | S2 | 1 |
| **F-35** | One impossible timestamp per timestamped dataset: `1900-01-01T00:00:00` in `shipments.promised_at`, `tracking_events.event_time` and `carrier_bookings.created_at`. | Profiling 2026-10-08 | S2 | 1 |
| **F-36** | `tracking_events.confidence` spans 0.001–1.42. One value lies outside the valid [0, 1] domain — a confidence score above certainty, consumed downstream with no bounds check. | Profiling 2026-10-08 | S2 | 1, 2 |
| **F-37** | **No semantic layer: categorical columns are polluted with workflow-status vocabulary.** `shipments.service_tier` takes the value `not_enforced`; `ai_invocations.model` takes `approved`; `tracking_events.timezone` takes `rejected`, `legacy`, `pending`; `routes.weather_risk` takes `internal`. Fourteen status-like tokens appear interchangeably across unrelated columns. No enum domain, no status taxonomy and no glossary exist anywhere in the repository. | Profiling 2026-10-08; absence of `semantic-layer/` | S1 | 1, 2 |
| **F-38** | Referential integrity is unenforced. One `tracking_events` row and one `carrier_bookings` row reference a `shipment_id` that does not exist in `shipments.csv`. Three shipments carry duplicate carrier bookings — the `duplicate_carrier_booking` saga defect named in `docs/architecture/known-gaps.md`, present and uncontrolled. | Profiling 2026-10-08; `docs/architecture/known-gaps.md` | S2 | 1, 2 |
| **F-39** | **A retry storm is already visible in the data.** `carrier_bookings.retry_count` ranges from 51 to **4,995**. There is no retry ceiling, no backoff, no circuit breaker and no idempotency key anywhere in the codebase. | Profiling 2026-10-08; repository-wide | S1 | 2 |
| **F-40** | **ETL counts defects and discards them.** `run_daily_batch.py` increments `bad` then `continue`s. No quarantine, no dead-letter, no threshold, no non-zero exit code. Its own comment admits: *"malformed records counted but not quarantined"*. | `etl/run_daily_batch.py:14-18` | S2 | 2 |
| **F-41** | The ETL has no run identifier, watermark or idempotency key. Re-execution reprocesses the full dataset with no way to distinguish runs in any downstream evidence. | `etl/run_daily_batch.py` | S2 | 2 |

### 4.6 Observability, audit & traceability

| ID | Finding | Evidence | Sev | Rubric |
|---|---|---|---|---|
| **F-42** | **About two thirds of the event stream cannot be correlated.** 1,992 of 3,000 events in `events.jsonl` (66.4%) carry no usable `correlation_id`: 983 are `null` and 1,009 are the empty string (re-counted 2026-10-08, decision-log D-012; an earlier null-only count of 983 was incomplete). End-to-end reconstruction of a business event — the Challenge 8 acceptance standard — is impossible for that share of traffic. | Profiling 2026-10-08 | S1 | 1, 3 |
| **F-43** | The audit event records only `ts`, `action` and `details`. No actor, no correlation ID, no tenant, no model or prompt version, no policy decision, no approval ID. `observability/otel-notes.md` independently confirms this list of omissions. | `apps/api/services/audit.py:8-12`; `observability/otel-notes.md` | S1 | 3 |
| **F-44** | **The audit sink is a local file written by the application itself** — `<repo>/logs/audit.log`, appended in-process. It is tamperable by the audited process, non-durable, never shipped, has no retention classification, and (per F-01, no `.gitignore`) is committable into source control. | `apps/api/services/audit.py:6,11-13` | S1 | 3 |
| **F-45** | `datetime.utcnow()` yields a naive timestamp with no timezone marker. Correlating it against `tracking_events.timezone` — itself polluted (F-37) — is unsafe, and `timezone_mismatch` is a declared brownfield concern. | `apps/api/services/audit.py:10`; `docs/architecture/known-gaps.md` | S2 | 3 |
| **F-46** | No tracing, no metrics, no SLOs, no dashboards-as-code, no alerting, no error budget. `/health` is the only operational signal and it returns a **static literal** — it checks no dependency, so it will report `ok` while the data layer is unavailable. | `apps/api/main.py:6-8`; `observability/otel-notes.md` | S1 | 3 |

### 4.7 Delivery, supply chain, infrastructure & contracts

| ID | Finding | Evidence | Sev | Rubric |
|---|---|---|---|---|
| **F-47** | **CI executes commands but produces no evidence.** The pipeline runs `pip install` then `pytest -q`. There is no lint, no type check, no coverage, no SAST, no dependency scan, no secret scan, no SBOM, no artifact publication and no evidence retention. Per F-02 it also fails. The Challenge 7 acceptance standard — *"the pipeline must generate evidence, not only execute commands"* — is not met. | `.github/workflows/ci.yml` | S2 | 2, 3 |
| **F-48** | The Terraform is a `local_file` resource with no provider, no backend, no state management and no infrastructure. The Challenge 5 acceptance standard — *"a new team can reproduce the intended local environment"* — is not met. | `infra/terraform/main.tf` | S2 | 2 |
| **F-49** | `supply-chain/dependency-risk-register.md` correctly names "no SBOM" and "no provenance" as targets, but no SBOM, checksum manifest or provenance attestation exists. The register is aspiration without artifact. | `supply-chain/dependency-risk-register.md` | S2 | 2, 3 |
| **F-50** | **The API contract omits both business endpoints.** `data/contracts/openapi-fragment.yaml` documents only `GET /health`. `/records/{record_id}` and `/ai/summarize/{record_id}` are absent, so contract testing cannot detect drift in the two paths that carry risk. | `data/contracts/openapi-fragment.yaml`; `apps/api/main.py` | S2 | 2, 4 |
| **F-51** | The characterization test characterises nothing. `test_characterization.py` asserts only `isinstance(row, dict)` and truthiness — it passes when the wrong record is returned, which is precisely the behaviour it purports to pin. | `tests/test_characterization.py` | S2 | 1 |
| **F-52** | `tests/playwright/operations.spec.ts` asserts that `body` is visible against an application that does not exist (F-05). It is a test engineered to pass without proving anything. | `tests/playwright/operations.spec.ts`; `apps/web/` | S2 | 4 |
| **F-53** | **A known architectural divergence is documented and unmanaged.** `ADR-0001` is marked *"Accepted, but never revisited"*, with the recorded consequence that "business rules and audit behavior now differ across code paths". No reconciliation, no owner, no review date. | `docs/ADR/0001-partial-modernization.md` | S2 | 1, 2 |
| **F-54** | **Data remediation will break the repository's own contract test.** `scripts/sanity_check.py` hard-asserts exactly 354 rows per CSV and exactly 3,000 JSONL events against `data/manifest.json`, exiting non-zero on mismatch. Quarantining the blank or duplicate rows found in F-33/F-34 therefore fails `make smoke`. Remediation must occur in a derived layer, or the manifest and its contract must be versioned deliberately (see OQ-14). | `scripts/sanity_check.py:24-33`; `data/manifest.json` | S2 | 1, 2 |
| **F-55** | `scripts/sanity_check.py` hard-requires the paths `docs/transformation-roadmap.md`, `docs/domain-specific-spec.md`, `PRODUCTION_EVIDENCE_PACK_TEMPLATE.md` and `apps/api/main.py`. Any Stage H restructuring must preserve or deliberately update these, or the smoke gate breaks. | `scripts/sanity_check.py:6-13` | S3 | 2 |
| **F-56** | The incident runbook declares itself *"intentionally incomplete"*. There is no severity model, no triage procedure, no rollback or degraded-mode procedure, no communications template and no evidence-capture step. | `docs/runbooks/incident-response.md` | S2 | 3 |
| **F-57** | **No business KPI data exists.** There is no cycle time, cost per shipment, exception rate, on-time rate, rework rate or adoption figure anywhere in the repository. Delivery Spine Stage 4 requires a *frozen before-state KPI baseline*; it can only be constructed from proxies derived from `events.jsonl` (`latency_ms`, `cost_units`, `severity`) and from `ai_invocations.token_count`. These must be declared as proxies with their limitations stated, never presented as business measurements. | Repository-wide; `data/synthetic/events.jsonl` | S2 | 1, 4 |

---

## 5. Severity distribution

| Severity | Count | Finding IDs |
|---|---|---|
| **S1 — Critical** | 25 | F-01, F-09, F-10, F-12, F-14, F-17, F-18, F-19, F-20, F-21, F-22, F-24, F-25, F-26, F-27, F-29, F-30, F-31, F-32, F-37, F-39, F-42, F-43, F-44, F-46 |
| **S2 — High** | 29 | F-02, F-04, F-05, F-07, F-08, F-11, F-13, F-15, F-16, F-23, F-28, F-33, F-34, F-35, F-36, F-38, F-40, F-41, F-45, F-47, F-48, F-49, F-50, F-51, F-52, F-53, F-54, F-56, F-57 |
| **S3 — Medium** | 3 | F-03, F-06, F-55 |
| | **57** | |

Nearly half the register is critical, and the critical findings cluster: five in identity and
authorisation, eight in AI governance, four in audit and observability. These are not
independent defects to be triaged individually — they are three broken subsystems, which is
why the runbook sequences them as subsystems (Steps H4, H7, H8) rather than as a finding list.

---

## 6. The three findings that most shape the runbook

**6.1 — Nothing is provable yet (F-01, F-42, F-43, F-44, F-47).**
The system's deficiency is not primarily code quality; it is that the repository has no
version control, no correlation across about two thirds of its events, an audit record without an
actor, a tamperable local audit sink, and a pipeline that produces no evidence. Four of the
five rubric criteria are scored on demonstrable proof. **Evidence infrastructure is therefore
not a late-stage activity in this runbook — it is Stage A.**

**6.2 — Identity is broken at three layers simultaneously (F-17/F-19/F-20, F-30/F-31/F-32).**
*Who* is calling is a self-asserted header that defaults to a permitted role and includes a
persona from an unrelated domain. *What* is being acted upon is resolved by scanning every
column for a value that collides across all six entity types, and silently returns the first
row on miss. These compound: an unauthenticated caller can obtain a record they did not ask
for, and the audit log will record neither who they were nor which record it actually was.

**6.3 — The AI boundary is open in both directions (F-22, F-24, F-25, F-26, F-20).**
Untrusted record content flows into the prompt with no sanitisation; model output flows back
with no schema validation, no guardrail (self-declared `not_enforced`), no approval gate and
no authorisation on the endpoint. The Challenge Guide's standard — *AI recommendations must
not silently become operational decisions* — is currently violated by construction, and the
data deliberately contains injection payloads with which to prove it.

---

## 7. What is genuinely sound and must be preserved

A credible transformation preserves working behaviour. The following are assets, not debt,
and Stage H must not discard them:

| Asset | Why it matters |
|---|---|
| `scripts/sanity_check.py` | A real, executable repository contract with a non-zero exit code. It is the only automated gate in the repository that asserts something true. Extend it; do not delete it. |
| `data/manifest.json` + `data/quality_issues.json` | Declared expected row counts and seeded defect classes — a usable oracle for data-quality regression testing. |
| `docs/domain-specific-spec.md` | A complete, coherent domain model (six entities with named fields, eight personas, four business flows). This is the correct seed for the Stage D semantic layer. |
| `docs/architecture/known-gaps.md`, `security/threat-model.md` | Six named brownfield defect classes. These are the starting backlog for Stage K threat modelling and Stage L red teaming. |
| `docs/runbooks/failure-injection-drills.md` | Five concrete, well-chosen failure scenarios. These map directly onto the Stage M failure-injection plan. |
| `observability/otel-notes.md` | An accurate self-assessment of the observability gap and a correct target-state list, including the AI telemetry fields. |
| `PRODUCTION_EVIDENCE_PACK_TEMPLATE.md` | A fifteen-section evidence structure that aligns with the Challenge Guide's sixteen challenges. This is the Stage R deliverable skeleton. |
| `docs/architecture/target-state-principles.md` | Six target-state principles, including *"generate evidence as a by-product of delivery"* — the principle this entire runbook operationalises. |

---

## 8. Assumptions and unknowns arising from this assessment

| Classification | Statement |
|---|---|
| **Assumption** | The synthetic datasets are a faithful stand-in for production data shapes. *Invalidation trigger:* production schema evidence that contradicts `docs/domain-specific-spec.md`. |
| **Assumption** | The seeded defects in `data/quality_issues.json` are intended to be discovered and remediated, not preserved as fixtures. *Invalidation trigger:* a ruling under OQ-14. |
| **Unknown** | Whether `REC-0001` appearing as the first-row key in all six datasets (F-30) is a deliberately seeded defect or an artifact of the data generator. This changes whether the fix is in the data or only in the lookup logic. → **OQ-15** |
| **Unknown** | The target runtime platform. `infra/terraform/main.tf` names no provider. IaC, identity, secrets management and release design all depend on this. → **OQ-01** |
| **Unknown** | Which real model replaces `local-sim-v1`, and which second model is used for the mandated comparison. → **OQ-02** |
| **Unknown** | The applicable regulatory regime. The domain involves customs agents, cross-border routes and vehicle/driver location data, which plausibly implicates data-protection and trade-compliance obligations, but no artifact states any. → **OQ-04** |
| **Unknown** | Whether any real stakeholder exists, or whether all governance must remain `PROVISIONAL` per Delivery Spine Stage 0B. → **OQ-05** |

All open questions are consolidated, with owners and blocked steps, in **Document 04**.
