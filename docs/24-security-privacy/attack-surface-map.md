# Attack surface map

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/main.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Surface | Entry | Auth | Notes |
|---|---|---|---|---|
| AS-01 | `GET /health`, `/ready` | HTTP | none | no data; `/ready` reports checks only |
| AS-02 | `GET /metrics` | HTTP | platform role `ops` | no per-user labels |
| AS-03 | `GET /audit/verify` | HTTP | platform role `auditor` | roles do not imply each other |
| AS-04 | `GET /shipments`, `/shipments/{id}/events` | HTTP | token + policy | page size ≤ 100 |
| AS-05 | `GET /records/{id}` | HTTP | token + policy | exact match on key, pattern checked |
| AS-06 | `POST /ai/summarize/{id}` | HTTP | token + policy + rate limit | calls gateway; only mutating AI route |
| AS-07 | `POST /ai/summaries/{id}/decision` | HTTP | token + `shipments:write` | the only state change |
| AS-08 | `GET /kpis` | HTTP | token + policy | aggregates |
| AS-09 | `/ops/*` static | HTTP | none for the shell; data needs a token typed by the user | CSP, nosniff, no-referrer |
| AS-10 | `/openapi.json`, `/docs`, `/redoc` | HTTP | none | local mode only; switched off when `APP_ENV` is not `local` (M1, tested); contains no secrets (tested) |
| AS-11 | data files and quarantine | filesystem | OS | contain synthetic personal-style identifiers |
| AS-12 | AI provider boundary | outbound (future) | n/a | not connected |
| AS-13 | JWKS verifier | outbound (future) | n/a | fail-closed stub |
| AS-14 | CI/CD and repo | GitHub | n/a | branch protection never ran; documented |

[VF] Six data and AI routes (AS-04..AS-08) need a token and a policy decision. Two operational routes (AS-02, AS-03) need a platform role. Health and ready are public by design; the OpenAPI document and docs pages exist only in local mode. One static shell is served.
[INF] Largest residual surface: the token issuer. HS256 with a shared secret means anything that can mint tokens can be any persona. The IdP (OQ-07) is the real fix.
