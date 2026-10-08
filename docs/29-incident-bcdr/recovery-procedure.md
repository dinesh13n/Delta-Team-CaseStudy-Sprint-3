# Recovery procedure

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | docs/28-resilience/* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| After | Do | Verify |
|---|---|---|
| process crash | restart; stores re-open (audit tail hash re-read, approvals replayed) | `/ready`, `/audit/verify` |
| bad ETL run | previous publication still served; fix the cause; rerun | report, `X-Data-Load-Id` changes |
| leaking model | keep AI off or deterministic; TEVV re-run before model returns | eval 0 failures |
| bad release | redeploy previous image/commit (tag `repo/v2-validated`); config is environment-only | smoke: health, ready, one record |
| lost audit log | restore from backup; if the gap cannot be closed, record the gap in the incident and **do not fabricate** missing events | tip hash vs external record |
| secret exposed | rotate `AUTH_SECRET`; all tokens die; re-issue | login tests |
Smoke test after any recovery: `/health` 200, `/ready` 200, one authenticated record read, one AI summary, `/audit/verify` valid.
