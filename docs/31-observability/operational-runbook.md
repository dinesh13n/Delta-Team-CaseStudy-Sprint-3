# Operational runbook

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (written) / CONDITIONAL (author-run only) |
| Evidence sources | evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | N-R-07 procedures untested by a second person |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

One section per alert. Anchors `a-01` etc. are referenced from `alerts.yaml`. Every first step uses evidence the system really produces. [VF] for the commands; the procedures have only been exercised for the AI leak case (tabletop M4, author-run).

<a id="a-01"></a>
### A-01 ApiHighErrorRate
1. `GET /ready` (checks data present, fresh if configured, audit writable). If 503, the message names the failing check.
2. Find a failing request: `python -m scripts.reconstruct --audit <audit> --subject <sub>` or by correlation id from the log line.
3. If caused by the last deployment: rollback-plan.md. If by data: fall back to the previous load (atomic publish keeps the last good one).

<a id="a-02"></a>
### A-02 ApiLatencyP95High
Check the 8-worker baseline (≈ 45 ms). Look for a runaway client (`http_requests_total` by route), an oversized audit (the `/metrics` verify cost, DEBT-N1-01), or host contention.

<a id="a-03"></a>
### A-03 AuthDeniedSpike
Inspect `auth_denied_total` by `reason`. Expired tokens at one client = client clock or TTL; many reasons = probing. Rotate the signing secret only if a token leak is suspected (secrets-hardening.md); all sessions end.

<a id="a-04"></a>
### A-04 PolicyDeniedSpike
By `entity`. A role mapping change in the IdP that was not mirrored in `access-semantics.yaml` looks like this. Do not widen policy to silence the alert; change it through the policy change process (K4) with the parity test.

<a id="a-05"></a>
### A-05 AiRateLimitHits
The limit is per subject per minute. Identify the subject from audit (`ai.summary.rate_limited` events). A loop in a client is the usual cause.

<a id="a-07"></a>
### A-07 AiSchemaViolations
Model output does not match the schema. Switch the model off (`AI_ENABLED=false`, restart) if the rate is sustained; the deterministic provider is the fallback anyway. Re-run the evaluation before re-enabling.

<a id="a-08"></a>
### A-08 AiFallbackRateHigh
Group by `reason`. `provider_error` / `provider_timeout`: provider health. `invalid_output`: model drift. `circuit_open`: see A-09.

### A-09 AiCircuitOpen
The breaker opens after repeated failures and probes after a cool-down (circuit-breaker-policy). While open, users get deterministic summaries; no action is needed except to find the provider fault.

<a id="a-10"></a>
### A-10 AiLatencyP95High
Provider slowness. Timeout is enforced in the gateway; confirm timeouts show in `ai_fallback_total{reason="provider_timeout"}`.

<a id="a-11"></a>
### A-11 AiSuggestionsRejectedHigh
Reviewers reject most suggestions. Treat as a quality signal: sample rejected suggestions with the reviewers, compare against the J2 evaluation, consider disabling.

### AiOutputLeakBlocked (page)
Follow `docs/29-incident-bcdr/ai-incident-playbook.md`. The playbook's detection step names `ai_guardrail_blocked_total`; the correct series is `ai_fallback_total{reason="output_policy_violation"}` (corrected here; playbook to be aligned in the final pass).

### AuditChainBroken (page)
Preserve the file first (copy, hash). Run `python -m scripts.reconstruct --audit <copy>`; the output names the first bad index. Do not repair in place. See incident-response-plan.md.

<a id="a-13"></a>
### A-13 DataStale / A-14 DataLoadMissing
Re-run the ETL (`python -m etl.run_daily_batch`). It publishes atomically; a failed run leaves the previous load untouched.

<a id="a-15"></a>
### A-15 MetricsAbsent
Service down or the scrape token invalid (a 401/403 from `/metrics` is itself counted only if the service is up). Check `GET /health`.

## Limits
Nobody other than the author has run these steps. Pager, escalation and communication channels are undefined (OQ-05).
