# Evidence manifest: evidence/40-scale

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-Q-01-preregistration | `EVD-Q-01-preregistration.json` | d050b98fe3a419f360f48be9edb646e952ccd3d08488cd5639d41556da875014 | Q1 | sha256sum of semantic-layer/ and 07-*/evaluation/ at commit following 4c84af1 | 2026-10-08T12:12:28Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | semantic-layer-portability-test.md |
| EVD-Q-02-comparison | `EVD-Q-02-comparison.csv` | 25b4aaddc9c676a3d13545292d79e791d6b3296d750047d7eae28ed004b32656 | Q2 | hand-assembled scorecard; Model B column NOT RUN | 2026-10-08T12:12:28Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | model-comparison.md |
