# Evidence manifest: evidence/38-handover

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-P-02-operator-exercises | `EVD-P-02-operator-exercises.json` | 0482bd0cf4b1edf59e04ea08f2b7ab4a6ba2d2d45fc2e423b430b1e3be6780ab | P2 | LATE REGISTRATION at R2: file produced earlier in step P2; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step P2 |
