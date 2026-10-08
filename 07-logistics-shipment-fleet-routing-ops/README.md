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
TOKEN=$(.venv/bin/python -c "import os; from apps.api.security.tokens import issue_dev_token as t; print(t(os.environ['AUTH_SECRET'], 'me', 'dispatcher'))")
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:8000/records/SHI-00002
```

Gates: `make gates` runs lint, types, secret scan, ETL, tests, semantic-layer tests and the smoke check.

`apps/web/` is a small TypeScript scaffold (one service, one component, one Playwright spec). It is not an Angular application: there is no framework dependency, routing or build (finding F-05, open question OQ-06). `npm run lint` checks that the sources parse. The operational view for the MVP is the OpenAPI UI at `/docs`.

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

