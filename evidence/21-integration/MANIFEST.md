# Evidence manifest: evidence/21-integration

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-J-05-saga-simulation | `EVD-J-05-saga-simulation.json` | 66c0a6ef457835fb26ed61804acde5eff5cc78e3e9272c0beeb9e183ef863fe7 | J5 | LATE REGISTRATION at R2: file produced earlier in step J5; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step J5 |
| EVD-J-05-saga-tests | `EVD-J-05-saga-tests.txt` | cd8eadbda2dd4ee54ccf1325e3fdd59fc09ec71d6c1b15a27534027975beab06 | J5 | LATE REGISTRATION at R2: file produced earlier in step J5; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step J5 |
