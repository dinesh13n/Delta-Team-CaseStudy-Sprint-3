# Evidence manifest: evidence/42-executive

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-Q-03-demo-rehearsal | `EVD-Q-03-demo-rehearsal.txt` | 4d74a7e8920cbe67c5729cea0654984e84e1980bb9cf95ac3ed6c0f00f2d0be2 | Q3 | scratchpad/q3_rehearsal.sh (author-run, 28 s) | 2026-10-08T12:12:28Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | demo-day-script.md |
| EVD-Q-03-rehearsal-script | `EVD-Q-03-rehearsal-script.sh` | 0b5366ba424272f5f658e48bd9bf195e0a523b5989067c1d24c2278c9606866b | Q3 | script that produced EVD-Q-03-demo-rehearsal.txt | 2026-10-08T12:12:28Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | demo-day-script.md |
