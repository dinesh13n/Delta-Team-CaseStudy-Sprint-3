# Evidence manifest: evidence/04-baseline-kpis

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-C-05-data-profile | `EVD-C-05-data-profile.json` | 6314f00faa1df6c781714c3be2e946cae1b323858f1b435868989a8f4dced202 | C1/C5 | python -I EVD-C-05-profile.py data/synthetic data/manifest.json | 2026-10-08T09:45:53Z | Claude agent for Dinesh | docs/04-baseline-kpis/ |
| EVD-C-05-profile | `EVD-C-05-profile.py` | 7c6f7f2b4fd3b69f6dc6b980a65d2f530219d69e9e53a2657e9d70ff34f0247a | C1/C5 | python -I EVD-C-05-profile.py data/synthetic data/manifest.json | 2026-10-08T09:45:54Z | Claude agent for Dinesh | docs/04-baseline-kpis/ |
