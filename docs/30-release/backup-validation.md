# Backup validation

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (repo level) / CONDITIONAL (production) |
| Evidence sources | evidence/30-release/EVD-N-03-backup-restore.json (SHA-256 a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e) |
| Assumptions | See body |
| Unresolved issues | storage, schedule, RPO owner |
| Residual risks | N-R-13 no offsite backup |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What was done [VF]
`python -m scripts.backup_restore` created a gzip tar of the published layers (curated, quarantine, reports), the audit log and the approval store, with a manifest of SHA-256 hashes; **deleted the live state**; restored into a fresh directory; started a new application instance on it; and compared. Evidence: `EVD-N-03-backup-restore.json` (SHA-256 `a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e`), run 2026-10-08T11:37:18Z.

| Check | Result |
|---|---|
| 16 files restored; hash of each equals the manifest | PASS |
| Record and list responses byte-identical before and after | PASS |
| `X-Data-Load-Id` unchanged | PASS |
| Audit chain valid after restore; record count preserved | PASS |
| A new event after restore chains onto the restored tip | PASS |
| `/ready` 200 on the restored instance | PASS |
| Edited backup (actor changed in record 0) detected by hash | PASS |
| Edited backup detected by chain verification | PASS |
| Backup 0.02 s, restore to serving 0.17 s (58 KB archive) | measured, fixture only |

**Defect in my first run:** one hash mismatch on `audit.log` appeared because the check ran after the restored instance had already written its own audit event. That was an ordering mistake in the test, not a backup fault. The check now hashes before the new instance starts; the first output is recorded here and not hidden.

## Not proven
- Restore on a platform, from remote storage, or by anyone but the author.
- Encryption, retention and offsite copy of backups: no storage exists.
- RTO/RPO at production volume. RPO is the snapshot interval; no schedule exists. Proposed (not decided): ETL snapshot with every load, audit snapshot hourly.
- Secrets and identity configuration are excluded by design and need their own recovery path.
- The source CSVs are not in the backup: version control is their store.
