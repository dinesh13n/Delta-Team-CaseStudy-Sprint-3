# AI incident playbook

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (tested by simulation) / CONDITIONAL (no human exercise) |
| Evidence sources | evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json, docs/24-security-privacy/threat-model.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Replaces the self-declared incomplete `docs/runbooks/incident-response.md` (F-56). Generic phases for every incident: **Detect → Triage → Contain → Preserve → Eradicate → Recover → Communicate → Learn.** Tools that exist today: `/metrics`, `/audit/verify`, `scripts/reconstruct.py`, `AI_ENABLED`, `scripts/lock_prompts.py`, `evaluation/run_eval.py`, `scripts/red_team.py`.

## Class table
| Class | Detect | Triage question | Contain | Evidence | Eradicate / recover |
|---|---|---|---|---|---|
| A. Prompt injection (direct/indirect) | `ai_fallback_total{reason="output_policy_violation"}`, `[unrecognised]` spike, injection marker in an audit `signals` list | did the injected text change any output or reach a person? | `AI_ENABLED=false` | audit by correlation id, input hash, source record | fix sanitiser/enum, add case to adversarial set, eval, red team |
| B. Data leakage in AI output | same; any forbidden value in a response/log | did a forbidden value leave the system? (SEV-3 vs 2/1) | AI off; if leaked, also revoke affected tokens | audit + preserved responses | leak scan fix, eval, notify per comms plan |
| C. Unsafe action | **cannot occur by design** (no write path); detect any new mutating route via the OpenAPI test | which route/commit introduced it? | roll back the release | git history, test failure | remove path, extend K1 matrix |
| D. Compromised tool / dependency | pip-audit/SBOM diff; unexpected outbound traffic (platform) | which package, which version, since when? | pin back, rebuild | SBOM, lock diff | upgrade/pin, re-scan |
| E. Bad retrieval / poisoned data | quarantine ratio jump; `ROW-SHAPE`/BR-* spike; `X-Data-Load-Id` change | which load, which source file? | stop ETL publish, keep previous load | ETL report, input hash | fix source, rerun idempotent ETL |
| F. Model/provider failure | `ai_fallback_total` reasons `provider_timeout/provider_error/circuit_open` | provider outage or our fault? | breaker handles; AI off if prolonged | metrics | provider recovery, breaker half-open |
| G. Cost runaway | `ai_tokens_total` growth, rate-limit 429 counts | which subject/route? | lower `AI_RATE_PER_MINUTE`, AI off | audit by subject | quotas; platform budget alerts (N5) |
| H. Identity compromise | repeated `auth.denied`, token use from unexpected subject | which subject/secret? | rotate `AUTH_SECRET` (invalidates all tokens), disable persona | audit by subject | issue new secret, review R-SEC-01 |
| I. Audit tampering | `/audit/verify` invalid | first bad index | preserve file untouched | copy + hash, restore from last good backup | compare tip hash with external record |

## Step detail (worked in the simulation `TT-1`, class B near miss)
1. **Detect**: alert on the fallback reason. 2. **Triage**: `python -m scripts.reconstruct --audit <log> --correlation-id <id>` shows actor, record, AI route taken, guardrail, prompt version and data load, from the audit alone. Check all captured responses for the forbidden value to set severity. 3. **Contain**: set `AI_ENABLED=false`, restart; core stays up. 4. **Preserve**: copy audit and approvals, hash them, run `/audit/verify`, write the tip hash somewhere the application cannot write. 5. **Eradicate**: lock/remediation tests and the full evaluation must pass. 6. **Recover**: re-enable with the deterministic provider only; the offending model stays off until TEVV is repeated. 7. **Communicate**: template in `communications-plan.md`. 8. **Learn**: blameless review within 5 working days; update datasets (never thresholds).
Evidence of execution: `evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json`.
