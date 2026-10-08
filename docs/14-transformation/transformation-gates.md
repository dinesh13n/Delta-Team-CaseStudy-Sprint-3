# Transformation gates

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/14-transformation; characterization tests EVD-C-08 |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Gates apply to every increment and are not negotiable per increment. A failure blocks merge unless a waiver names an owner, a reason and an expiry.
| Gate | Check | Command (indicative) | Waiver possible? |
|---|---|---|---|
| TG-1 | Characterization suite green, or each difference explained as APPROVED CHANGE (cites spec/AC) or reverted | pytest tests/characterization | Only as APPROVED CHANGE |
| TG-2 | Unit and integration tests green | pytest | No |
| TG-3 | ruff and mypy clean | ruff check; mypy | Yes, with owner |
| TG-4 | Secret scan clean | gitleaks-equivalent / pre-commit | No |
| TG-5 | Semantic-layer tests green | pytest semantic-layer/tests | No |
| TG-6 | Fixture untouched | sha256sum -c EVD-A-01 manifest | No |
| TG-7 | Coverage >= 80% (from H11) | pytest --cov | Yes until H11 |
| TG-8 | Evidence produced and registered in MANIFEST.md | manifest check | No |
| TG-9 | Contract route diff clean (from H9) | route-diff script | No |
