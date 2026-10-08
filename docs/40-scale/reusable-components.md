# Reusable components

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (evidence-backed list) |
| Evidence sources | docs/16-repo-validation/remaining-debt-register.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Only components with demonstrated evidence are listed. "Evidence" = what was actually shown; "Do not carry" = registered debt or first-use assumptions.

| Component | Evidence of fitness | Do not carry |
|---|---|---|
| Policy-from-YAML with generated Rego and parity test | allow/deny matrix, parity test | the role names and entity list are logistics-specific |
| AI gateway pattern (sanitiser, enum allow-list, schema validation, leak check, prompt/model lock, timeout, breaker) | 192-case evaluation, 12-attack red team (0 succeed), 5 drills | prompt text; the `[unrecognised]` enum noise workaround (DEBT-15) |
| Hash-chained audit + reconstruction script | tamper test, reconstruction, restore | single-file store (DEBT-04, single replica) |
| Approval record (suggestion → decision) | tests, reconstruction | self-approval allowed (HC-R-01), no expiry (HC-R-03) |
| ETL with contract, quarantine, atomic publish, row-shape rule | drills 5, tests | the BR-04/F-59 rulings; enum noise |
| Observability as code and validator | 31 rules validated against live exposition | thresholds (untuned); no collector ever run |
| Backup/restore verifier | corrupt-backup detection | fixture-scale timings |
| Drift check + thresholds | clean and drifted runs | thresholds untuned |
| Operator exercises harness | 5 exercises from a clean copy | author-run only |
| Evidence contract and manifests | used throughout | manifests are not yet registered for all files (end-of-run chore) |
