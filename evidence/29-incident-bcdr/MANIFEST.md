# Evidence manifest: evidence/29-incident-bcdr

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-M-04-tabletop-simulation | `EVD-M-04-tabletop-simulation.json` | 4b0a559a37a34090a95c38774c364d70c4b012dc734a41a55a2171aaaba8cb10 | M4 | LATE REGISTRATION at R2: file produced earlier in step M4; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step M4 |
