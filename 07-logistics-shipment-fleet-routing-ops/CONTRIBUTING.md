# Contributing

1. Work on a branch; `main` is protected (see `docs/15-modernization/branch-protection.md`).
2. Install: `make install` (hash-pinned lock; Python 3.11 or 3.14).
3. Before pushing: `make gates` (lint, types, secret scan, tests, smoke, Rego checks).
4. Commit messages carry finding IDs, for example `fix(H5): exact-key lookup (F-30, F-31, F-32)`.
5. A change that alters behaviour needs: an entry in `docs/15-modernization/approved-behavior-changes.md`, a feature flag or a revert path, and an updated characterization expectation.
6. Never edit `data/synthetic/*` (immutable fixture). Derived data goes to `data/curated` and `data/quarantine` through `make etl`.
7. Never commit secrets. `.env` is git-ignored; `.env.example` holds placeholders only.
