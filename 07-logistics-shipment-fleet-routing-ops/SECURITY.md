# Security policy

- Report a suspected vulnerability privately to the repository owner (GitHub private vulnerability reporting). Do not open a public issue with exploit details.
- Supported: the `main` branch. This is a training repository with synthetic data; no production system is attached.
- Secrets: none belong in the repository. Values that appeared in early history (see `docs/27-hardening/secrets-hardening.md`) are treated as compromised and must never be reused.
- Controls: bearer-token identity, policy-as-code, allow-listed AI context, hash-chained audit log, secret scanning in pre-commit and CI.
