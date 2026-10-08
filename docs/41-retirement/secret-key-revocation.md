# Secret and key revocation

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | OPEN (P-X5 met on paper, not in fact: nothing has been revoked) |
| Evidence sources | evidence/15-modernization/EVD-H-03-secret-scan-history.json; docs/27-hardening/secrets-hardening.md |
| Assumptions | See body |
| Unresolved issues | credential owners |
| Residual risks | P-R-04 public repository, unrevoked history |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

P-X5: revocation must cover **every credential found in step H3, including in history**. The history scan (EVD-H-03-secret-scan-history.json) reports 10 findings in commit `7ba349e` (the as-delivered commit). They are **five distinct credentials**; the earlier rotation table in `secrets-hardening.md` named three of them, so the table is **superseded by this one**.

| # | Credential (variable) | Where found | Scan rules | Treat as | Action | Owner | Done? |
|---|---|---|---|---|---|---|---|
| 1 | `DATABASE_URL` (DSN with embedded password) | `.env.example` line 1 in history | dsn-with-password, known-weak-value | compromised | revoke the account/password if it was ever real; otherwise record "never real" with who confirmed | UNRESOLVED | **no** |
| 2 | `AI_GATEWAY_KEY` (key-shaped) | `.env.example` line 2 in history | api-key-literal, known-weak-value | compromised | revoke at the issuer; issue per-environment keys from a secret store | UNRESOLVED | **no** |
| 3 | `LEGACY_BATCH_PASSWORD` | `.env.example` line 3 in history | assigned-secret, known-weak-value | compromised | rotate or confirm never real | UNRESOLVED | **no** |
| 4 | `OT_VENDOR_TOKEN` (shared) | `.env.example` line 4 in history | assigned-secret, known-weak-value | compromised | revoke the shared token with the vendor; per-consumer tokens | UNRESOLVED | **no** |
| 5 | `SHARED_DB_PASSWORD` | `legacy/reconcile_legacy.py` line 6 in history | assigned-secret, known-weak-value | compromised | rotate; check reuse across systems | UNRESOLVED | **no** |
| 6 | Any `AUTH_SECRET` used outside tests | not in history (scan clean) | n/a | new per environment | generate ≥ 32 random chars per environment; rotate on suspicion | Security | n/a |

## Facts and limits
- The repository is **public** (dinesh13n/Delta-Team-CaseStudy-Sprint-3) and history is not rewritten (it would break the baseline tags and evidence hashes). Anyone can read the values; deleting them from the working tree does not help.
- The values may be workshop placeholders, but they cannot be told apart from real ones from the repository alone. Only the issuers can say.
- **Nothing has been revoked by this work.** It needs the credential owners, who are not named.
- Working tree scan: 0 findings at 2026-10-08 (EVD-H-03-secret-scan.json). CI and pre-commit keep it at zero.
- The local sandbox credentials used for pushing are not in the repository.
