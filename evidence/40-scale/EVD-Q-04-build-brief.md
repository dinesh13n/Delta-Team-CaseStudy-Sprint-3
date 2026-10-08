# Build brief (Stage Q1 portability test)

You are Model B. Build a working subset of a logistics shipment-operations service **from the specification only**.
Everything you may use is in this directory: `semantic-layer/` (the shared meaning of the domain), `docs/17-implementation-prd/`,
`docs/12-specs/` (system, API, security, NFR, error-handling specs, feature specs, JSON schemas, OpenAPI) and `docs/19-intelligence/prompt-registry.md`.
Sample curated data is in `data/curated/*.csv`. Do not read anything outside this directory except the Python standard library
and the installed packages. Do not look for any existing implementation of this system anywhere on the machine.

## Subset to build (four behaviours)
1. **Record lookup by exact key** (`GET /records/{id}`; also `GET /health`, `GET /ready`).
2. **Identity and policy decision**: bearer HS256 token (claims `sub`, `role`, `tenant`, `exp`), persona/entity/field/purpose decisions driven by
   `semantic-layer/access-semantics.yaml`, deny by default, no trust in `X-User-Role`.
3. **AI summary with guardrail** (`POST /ai/summarize/{id}`, `POST /ai/summaries/{id}/decision`): suggest-only exception summary, output validated against
   `docs/12-specs/schemas/ai-summary-output.schema.json`, abstention path, human approval record, rate limit, deterministic provider as default and as fallback.
   No real model is called.
4. **Audit v2 with hash chain** (`GET /audit/verify`, every request that touches data or AI is audited per FEAT-05).

## Delivery contract (fixed by the test harness, not negotiable)
Create everything under the build directory you are given (`<BUILD>`), Python 3.11, only packages already installed in the interpreter you are given
(fastapi, starlette, uvicorn, pydantic, jsonschema, PyYAML, PyJWT, httpx, pytest). No network.

* `<BUILD>/app/main.py` exposes an ASGI object named `app`. The harness starts it with `uvicorn app.main:app` from `<BUILD>`.
* Configuration is read from environment variables only:
  `APP_ENV` (`local`), `AUTH_SECRET` (HS256 secret, at least 32 characters), `DATA_DIR` (directory that contains `curated/shipments.csv`,
  `curated/tracking_events.csv`, `curated/carrier_bookings.csv`), `SEMANTIC_LAYER_DIR` (a copy of `semantic-layer/`), `AUDIT_PATH` (audit log file, JSON Lines, one event per line),
  `APPROVALS_PATH` (approval records, JSON Lines), `AI_RATE_PER_MINUTE` (default per the specs).
* `<BUILD>/app/adapter.py` defines `summarize_case(case: dict, provider=None) -> dict`, used by the harness to evaluate the AI behaviour without HTTP.
  `case` has keys `shipment` (dict of strings, one row shaped like `curated/shipments.csv`), `events` (list of dicts shaped like `tracking_events.csv`),
  `bookings` (list of dicts shaped like `carrier_bookings.csv`); all values are strings exactly as read from CSV.
  It must run the **same** guardrail/gateway code path that `POST /ai/summarize/{id}` uses and return the same JSON object that endpoint returns in its body.
  `provider=None` means your built-in deterministic provider. Otherwise `provider` is a callable `provider(system_prompt: str, data_json: str) -> str` returning the raw text a model
  produced; it may raise `ConnectionError` (provider unavailable) or any other exception (provider error). Your gateway must treat its output as untrusted.
* `<BUILD>/tests/` holds your own tests (pytest). Keep them passing.
* `<BUILD>/NOTES.md`: list every place where the specification was silent, contradictory or ambiguous and what you decided (this is a primary output of the test),
  list the files and directories you read, and state what you did not implement.

## Rules of the test
One attempt. Work from the documents; when they are silent, choose the most defensible reading and record it in NOTES.md, do not ask questions.
You will not be shown the acceptance harness. Your build will be judged by an unchanged harness that was fixed before you started.
