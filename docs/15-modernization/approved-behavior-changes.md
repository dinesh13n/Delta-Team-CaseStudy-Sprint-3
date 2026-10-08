# Approved behaviour changes (register)

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H10 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (authority: D-009 operator instruction; CTO ratification pending) |
| Evidence sources | EVD-H-04, EVD-H-10 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Change | Findings | Spec | Flag / rollback | Test |
|---|---|---|---|---|---|
| AB-01 | Secrets removed from tree; config validated at start (AUTH_SECRET >= 32 chars outside `local`) | F-09..F-15 | security-spec | no flag by design; revert R1 | test_config, secret scan |
| AB-02 | Exact business-key lookup; pattern validation; 404 for a missing well-formed id; no first-row fallback | F-30, F-31, F-32 | FR-01, AC-01..03 | FF-02 LOOKUP_MODE (legacy only when `APP_ENV=local`) | test_record_lookup |
| AB-03 | Verified bearer token replaces client role header | F-17 | FR-03 | FF-01 AUTH_MODE (legacy only when local) | test_identity_policy |
| AB-04 | Foreign-domain persona removed | F-19 | FR-04 | follows AB-03 | test_identity_policy |
| AB-05 | Denials are 401/403 problem+json | F-18 | FR-05, AC-07 | follows AB-03 | test_contract_ops |
| AB-06 | AI endpoint requires token and policy | F-20 | FR-03 | FF-04 AI_ENABLED | test_ai_gateway |
| AB-07 | Guardrail status evaluated | F-24 | FR-11 | none (FF-05 has no off switch by design) | test_ai_gateway |
| AB-08 | Summary derived from allow-listed facts via gateway | F-22, F-23, F-25..F-29 | FR-09, FR-10 | FF-03 AI_PROVIDER | test_ai_gateway |
| AB-09 | Audit v2 (actor, correlation, decision, hash chain) | F-43..F-45 | FR-13 | revert R2 (FF-06 not implemented, see D-013) | test_audit_chain |
| AB-10 | Field-level masking by persona | F-18 | access-semantics.yaml | FF-01 | test_identity_policy |
| AB-11 | ETL quarantine, run id, report, non-zero exit past 5% | F-33..F-36, F-40, F-41, F-54, F-58, F-61, F-62 | FR-06, FR-07 | FF-07 DATA_LAYER | test_etl_quarantine |
| AB-12 | New read endpoints (/ready, /metrics, /shipments, /events, /audit/verify, /kpis, approval decision) are additive | F-46, F-50 | FR-15, FR-16 | n/a | test_contract_ops |

[ASM] Authorisation source is the operator instruction in D-009. G-X6 stays CONDITIONAL until the Repository Owner and Business Sponsor sign (OQ-05).
