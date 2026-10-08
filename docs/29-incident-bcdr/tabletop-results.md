# Tabletop results

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (author-run; no human participants) |
| Evidence sources | evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | INC-C1 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Evidence: `evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json` (run 2026-10-08, 15 s).

| Phase | Result | Observation |
|---|---|---|
| Inject | OK | guardrail replaced the output: `fallback`/`output_policy_violation`; customer id absent from the response |
| Detect | OK **with a correction** | the metric that moves is `ai_fallback_total{reason="output_policy_violation"}`; `ai_guardrail_blocked_total` does **not** move on this path. An alert built on the latter would have missed the event. N1 alert rules use the first |
| Triage | OK | one correlation id gave actor, role, record, policy rule, AI route taken, guardrail status, prompt version and **data load id**, from the audit alone |
| Severity | OK | SEV-3: 2 captured responses checked, no forbidden value |
| Who saw it | OK | approvals record: requested by alice, no decision |
| Contain | OK | AI off: 503; core 200/200 |
| Preserve | OK | audit and approvals hashed; chain valid (3 records); tip hash recorded |
| Eradicate | OK | prompt-lock and remediation tests passed; evaluation 0 failures |
| Recover | OK | deterministic provider only; no leak |
| Communicate | OK | template filled entirely from audit facts |

## Defects the exercise found
| ID | Finding | Action |
|---|---|---|
| TT-F1 | the audit event for an AI summary did not record `generated_by`, `fallback_reason`, `guardrail_status`, `prompt_version` or the data load | **fixed**: added to the audit detail; test `test_ai_audit_event_records_what_the_ai_did…` |
| TT-F2 | the planned alert metric would not fire for the leak path | alert rule corrected (N1) |
| TT-F3 | no per-token revocation | recorded (containment-procedures; R-SEC-01) |
| TT-F4 | tip hash must live outside the app to mean anything | procedure written; no external store exists |

## What this does not show
Nobody else took part, so response times, hand-offs, disagreement, fatigue and unclear ownership are untested. M-X6 asks for "a tabletop has been run with results": a simulation was run; a human tabletop is an open condition (INC-C1).
