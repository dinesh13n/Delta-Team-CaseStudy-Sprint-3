# Logistics: Shipment, Fleet, Routing & Exception Operations

This is an independent brownfield enterprise system repository. It combines modern code, legacy scripts, data-quality issues, security weaknesses, incomplete tests, operational gaps, and AI governance debt.

## Centre of Gravity

Distributed workflows + real-time data + failure engineering + cost

## Quick Start

Requires Python 3.11 or 3.14 and the repository root layout (the `semantic-layer/` folder sits next to this directory).

```bash
make install          # venv + hash-pinned dependencies (pip --require-hashes)
make etl              # builds data/curated and data/quarantine from the immutable fixture
export AUTH_SECRET="$(python3 -c 'import secrets; print(secrets.token_urlsafe(48))')"   # local only, never committed
make test             # unit, contract and characterization tests
make run              # uvicorn apps.api.main:app --reload  (module path uses dots, not slashes)
```

Get a development token (local only) and call the API:

```bash
TOKEN=$(.venv/bin/python -m scripts.issue_dev_token dispatcher)
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:8000/records/SHI-00002
```

### Windows (PowerShell)

GNU `make` is not installed on Windows by default, so use `make.cmd`. It runs `make.ps1`, which has the same targets as the Makefile, creates the venv with `py -3.11`, and uses `.venv\Scripts\python.exe` instead of `.venv/bin/python`.

```powershell
.\make.cmd install          # venv + hash-pinned dependencies
.\make.cmd etl
$env:AUTH_SECRET = .venv\Scripts\python.exe -c "import secrets; print(secrets.token_urlsafe(48))"   # this PowerShell session only, never committed
.\make.cmd test
.\make.cmd run
```

Type `.\make.cmd` in full. PowerShell resolves `.\make` to `make.ps1`, and on machines whose execution policy is `AllSigned` or `Restricted`, Windows blocks unsigned `.ps1` files ("is not digitally signed"). `make.cmd` bypasses the policy for that one call only and changes no system setting. You can also chain targets (`.\make.cmd install etl test`) or run all gates (`.\make.cmd gates`).

Get a token and call the API from PowerShell:

```powershell
$TOKEN = .venv\Scripts\python.exe -m scripts.issue_dev_token dispatcher
curl.exe -H "Authorization: Bearer $TOKEN" http://127.0.0.1:8000/records/SHI-00002
```

If GNU make is installed (for example with `winget install ezwinports.make`), the Makefile detects Windows and uses the same paths, so `make install`, `make test` and the other targets also work. WSL works too, with the Linux commands above.

Gates: `make gates` (or `.\make.cmd gates` on Windows) runs lint, types, secret scan, ETL, tests, semantic-layer tests and the smoke check.

## Using the UI

When the server runs locally, it serves a read-only operations view at **http://127.0.0.1:8000/ops/**. From there you can:

1. **Sign in** by pasting a bearer token. The page keeps it in memory only, so paste it again after a refresh.
2. **Browse shipments**, filtered by status, 10 per page.
3. **Open a record** to see its details and event history.
4. **Ask for an AI summary** of an exception and approve or reject it, with an optional reason. The summary is a suggestion only; a person decides.

The token must be signed with the same `AUTH_SECRET` as the running server, so create the secret, print a token and start the server in the same terminal:

```bash
export AUTH_SECRET="$(python3 -c 'import secrets; print(secrets.token_urlsafe(48))')"
make token                 # prints a token for ROLE (default: dispatcher)
make run
```

On Windows (PowerShell):

```powershell
$env:AUTH_SECRET = .venv\Scripts\python.exe -c "import secrets; print(secrets.token_urlsafe(48))"
.\make.cmd token           # prints a token for $env:ROLE (default: dispatcher)
.\make.cmd run
```

Copy the printed token, open http://127.0.0.1:8000/ops/, paste it and select **Load shipments**.

- **Tokens expire after 1 hour.** Run `make token` (`.\make.cmd token` on Windows) again for a new one. If the server restarts with a new secret, old tokens stop working.
- **Roles:** to see the data as another role, set `ROLE` before generating the token: `make token ROLE=fleet_manager`, or on Windows `$env:ROLE = 'fleet_manager'; .\make.cmd token`. Roles: `dispatcher`, `warehouse_ops`, `fleet_manager`, `driver`, `customs_agent`, `customer_support`, `carrier_partner`. Sensitive fields such as customer ID are masked (`***`) depending on the role. Roles and masking are defined in `../semantic-layer/access-semantics.yaml`.
- **API reference:** http://127.0.0.1:8000/docs lists every endpoint. It has no way to enter a token, so calls that need sign-in fail there; use `/ops/` or `curl` for those.
- `/docs` is available only when `APP_ENV=local` (the default). `/ops/` is always served, but its data still requires a valid token.

The page is plain HTML and JavaScript in `apps/web/public/`, served by the API, with no build step. `apps/web/src/` is a separate small TypeScript scaffold (one service, one component, one Playwright spec). It is not an Angular application: there is no framework dependency, routing or build (finding F-05, open question OQ-06). `npm run lint` checks that the sources parse.

## Synthetic Data

All data is local and synthetic under `data/`. No external services are required.

## Transformation Spine

1. Understand Existing Repo
2. Establish Behavioural Baseline
3. Identity & Least Privilege
4. Secrets & Encryption
5. Infrastructure as Code
6. Policy as Code
7. CI/CD & Supply Chain
8. Observability & Traceability
9. AI Security & Guardrails
10. Performance & Scalability
11. Reliability & Failure Engineering
12. Cost & AI FinOps
13. Automated Security Validation
14. Auditability & Compliance Evidence
15. Production Readiness Gate
16. Production Evidence Pack

