# Evidence manifest: evidence/23-human-control

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-K-01-human-control-tests | `EVD-K-01-human-control-tests.txt` | ebd91a777fa2223e03d14f0f9a949ecafa3b80e17a0da4cf179519ccde821828 | K1 | LATE REGISTRATION at R2: file produced earlier in step K1; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step K1 |
