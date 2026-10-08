# Evidence manifest: evidence/14-transformation

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-G-01-backlog-finding-coverage | `EVD-G-01-backlog-finding-coverage.txt` | f64b2b4c088a555f2f8092bff98371c1073f4215504b19a776bae50aeadcbc95 | G1/G4 | python gen_g1.py / gen_g3.py | 2026-10-08T10:04:56Z | Claude agent for Dinesh | stage-g-gate.md |
| EVD-G-04-authorisation-record | `EVD-G-04-authorisation-record.txt` | 88f1b4321b2f75114ce9c1a23866a289757ac3f81358180c55b323d15d2e4679 | G1/G4 | python gen_g1.py / gen_g3.py | 2026-10-08T10:04:56Z | Claude agent for Dinesh | stage-g-gate.md |
| EVD-G-05-stage-g-exit-checks | `EVD-G-05-stage-g-exit-checks.txt` | 2821273226c7a28d49e897479703bdf974cf8c160f04beb8dc6055d8c55397ad | G5 | sha256sum -c; git diff --quiet | 2026-10-08T10:05:18Z | Claude agent for Dinesh | stage-g-gate.md |
