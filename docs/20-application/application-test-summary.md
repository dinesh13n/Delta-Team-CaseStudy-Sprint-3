# Application test summary

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-J-04, EVD-H-11 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Full suite on Python 3.14.7: **112 passed, 7 xfailed** (the 7 are approved behaviour changes). Browser end-to-end (Chromium via Playwright, run from the cloud workspace against the live API on the real curated data): **10/10 checks passed** (EVD-J-04). Checks: view served with CSP; list of 349 shipments paged; status filter; record with `customer_id` masked; AI suggestion shown as suggestion only; approval recorded and buttons disabled; bad token shows an error and no rows; no console errors.
**F-05/F-52 closed.** The old Playwright spec asserted only that `<body>` exists; it is replaced by a spec that drives the real workflow (`tests/playwright/operations.spec.ts`, skips without `E2E_TOKEN`) and by Python tests (`tests/test_ops_view.py`). The Playwright spec itself was **not run through `npx playwright test`** in this environment; the equivalent flow was run with the Playwright Python API (script kept as evidence).
Defects the browser run found and fixed: favicon 404, password input outside a form.
Finding recorded: on the fixture, `event_type`, `service_tier`, `source_system` hold workflow words (F-37), so summaries show `[unrecognised]` for them (DEBT-15).
