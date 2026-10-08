# Evidence manifest: evidence/39-continuous-improvement

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-P-03-drift-check-clean | `EVD-P-03-drift-check-clean.json` | 68b946cf2f1147b84059905b7a80e23bdaeea3e6bc06eca8a3492b7a59d8258f | P3 | LATE REGISTRATION at R2: file produced earlier in step P3; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step P3 |
| EVD-P-03-drift-check-drifted | `EVD-P-03-drift-check-drifted.json` | 702f90ca3f04232249f31c3dc207c67aee97f3e3afa0b9914b9f6df54adc29a4 | P3 | LATE REGISTRATION at R2: file produced earlier in step P3; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step P3 |
