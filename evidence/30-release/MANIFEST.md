# Evidence manifest: evidence/30-release

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-N-03-backup-restore | `EVD-N-03-backup-restore.json` | a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e | N3 | LATE REGISTRATION at R2: file produced earlier in step N3; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step N3 |
