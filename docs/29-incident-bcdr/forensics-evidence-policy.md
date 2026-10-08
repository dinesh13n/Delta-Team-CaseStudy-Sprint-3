# Forensics and evidence policy

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/audit_chain.py, scripts/reconstruct.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. **Preserve before fixing.** Copy `logs/audit-v2.log`, `logs/approvals.jsonl`, the ETL report, the quarantine files and the application log to a separate location *before* restarting or editing.
2. **Hash everything** (SHA-256) and record the hashes in the incident record and, for the audit chain, the **tip hash** in a place the application cannot write (ticket, signed message). The chain proves internal consistency only: someone with file access could rewrite and re-chain the whole file, so the externally recorded tip hash is what makes tampering detectable.
3. **Verify** with `GET /audit/verify` (platform auditor) and `scripts.reconstruct` (read-only).
4. **Chain of custody**: who copied, when (UTC), from where, hash.
5. **Do not log secrets or personal data into the incident record**: use identifiers and hashes; AI traces store an input hash, not the prompt text.
6. **Retention**: incident evidence is kept at least as long as the audit class (evidence-retention-policy), longer if a legal hold applies.
7. **Reproduce, do not guess**: use the correlation id and the data load id to select the exact input (`X-Data-Load-Id`, audit `data_load_id`).
Limit: logs outside the audit chain (application stdout) are not tamper-evident.
