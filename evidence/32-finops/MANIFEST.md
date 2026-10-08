# Evidence manifest: evidence/32-finops

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-N-04-finops-model | `EVD-N-04-finops-model.json` | 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac | N4 | LATE REGISTRATION at R2: file produced earlier in step N4; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step N4 |
