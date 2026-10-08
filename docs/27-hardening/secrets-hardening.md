# Secrets hardening: inventory, history disposition, rotation plan

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft; history values treated as COMPROMISED until rotated |
| Evidence sources | EVD-H-03 |
| Assumptions | See body |
| Unresolved issues | Owners for rotation UNRESOLVED |
| Residual risks | TR-01 (public-history exposure) |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## 1. Inventory of secret-shaped literals found at baseline
| Where | Kind | Finding | Action taken |
|---|---|---|---|
| `legacy/reconcile_legacy.py` | hardcoded DB password | F-09 | removed; reads env |
| `.env.example` | DSN with embedded password | F-10 | replaced with placeholders |
| `.env.example` | key-shaped AI gateway value | F-11 | placeholder |
| `.env.example` | shared OT vendor token | F-12 | placeholder; comment removed |
| `.env.example` | LOG_LEVEL=DEBUG | F-13 | default INFO |
| `infra/terraform/main.tf` | `local_file` emitting a credential artefact | F-15 | resource removed |

## 2. Scan results
[VF] Working tree: 0 findings (EVD-H-03-secret-scan.json). Git history: 10 findings, all in commit `7ba349e` (the as-delivered commit) (EVD-H-03-secret-scan-history.json).

## 3. History disposition
[ASM] The values are workshop placeholders, but they are indistinguishable from real credentials and sit in the repository (dinesh13n/Delta-Team-CaseStudy-Sprint-3), which was public until 2026-10-08 and is now private (D-016); earlier clones and forks are outside our control. Policy: treat as compromised. History is **not** rewritten (rewriting would break the immutable baseline tags and the evidence hash chain). Disposition: rotate if any value was ever real; otherwise record as "never real" with the owner's attestation.

## 4. Rotation plan
| Secret | Owner | Action | Target date [ASM] |
|---|---|---|---|
| DB password (legacy) | UNRESOLVED | confirm never used, else rotate | before any deployment |
| AI gateway key | UNRESOLVED | revoke the pattern, issue per-environment key from a secret store | before OQ-02 model use |
| OT vendor token | UNRESOLVED | revoke "shared" token, issue per-consumer | before integration |
| AUTH_SECRET | new | generate >= 32 random chars per environment; never in repo | at deploy |

## 5. Sensitive-field checklist (ties to semantic-layer/access-semantics.yaml)
customer_id (masked for non-owner personas), driver and vehicle location (restricted, see K3 PIA), carrier identifiers, free text (never sent to a model outside `ai-context-policy.yaml`).

## 6. Controls now in place
Pre-commit + CI secret scan (`scripts/secret_scan.py`, test `test_secret_scan`), config validation that refuses weak secrets outside local, `.env.example` placeholders only.
