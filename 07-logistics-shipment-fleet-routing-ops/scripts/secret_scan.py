"""Offline secret scanner (F-09..F-14; NFR-7). Scans the working tree, or full git history with --history.

Exit 1 when a finding exists. Line-level opt-out: append the marker `secret-scan: allow` with a reason.
This is a pattern scanner, not a substitute for a maintained tool (gitleaks); CI runs both when available.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".mypy_cache", ".ruff_cache", ".pytest_cache", "logs"}
SKIP_FILES = {"secret_scan.py", "test_secret_scan.py"}  # the scanner and its own tests contain the patterns
SKIP_SUFFIX = {".csv", ".jsonl", ".lock", ".png", ".jpg", ".pdf", ".docx"}
ALLOW = "secret-scan: allow"

PATTERNS: dict[str, re.Pattern[str]] = {
    "dsn-with-password": re.compile(r"[a-z][a-z0-9+.-]*://[^\s:/@]+:[^\s@]{3,}@"),
    "api-key-literal": re.compile(r"\bsk-[A-Za-z0-9_\-]{8,}"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private-key-block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "assigned-secret": re.compile(
        r"""(?ix)\b[\w.-]*(password|passwd|secret|api[_-]?key|apikey|token|credential)["']?\s*[:=]\s*["']?(?!\s|["']|\$\{|<|os\.environ|getenv)([^\s"'#,)]{8,})"""
    ),
    "known-weak-value": re.compile(r"Welcome123|legacy-batch-password|replace-me-but-currently-shared|workshop-hardcoded"),
}
ASSIGN_OK = re.compile(r"(?i)(environ|getenv|settings\.|issue_dev_token|token_urlsafe|\bsecret\b\s*[:=]\s*(self|st|svc|s)\b)")


def scan_text(name: str, text: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for n, line in enumerate(text.splitlines(), 1):
        if ALLOW in line:
            continue
        for rule, pat in PATTERNS.items():
            m = pat.search(line)
            if not m:
                continue
            if rule == "assigned-secret" and ASSIGN_OK.search(line):
                continue
            out.append({"file": name, "line": n, "rule": rule, "excerpt": line.strip()[:20] + "..."})
    return out


def scan_tree(root: Path) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or set(p.relative_to(root).parts) & SKIP_DIRS:
            continue
        if p.name in SKIP_FILES or p.suffix in SKIP_SUFFIX or p.stat().st_size > 1_000_000:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        found += scan_text(str(p.relative_to(root)), text)
    return found


def scan_history(root: Path) -> list[dict[str, Any]]:
    log = subprocess.run(
        ["git", "-C", str(root), "log", "--all", "-p", "--no-color", "--format=commit %H", "--", "."],
        capture_output=True,
        text=True,
        check=False,
    ).stdout
    found: list[dict[str, Any]] = []
    commit = ""
    for line in log.splitlines():
        if line.startswith("commit "):
            commit = line[7:19]
        elif line.startswith("+") and not line.startswith("+++"):
            for f in scan_text(f"history:{commit}", line[1:]):
                found.append({**f, "line": 0})
    seen, uniq = set(), []
    for f in found:
        k = (f["file"], f["rule"], f["excerpt"])
        if k not in seen:
            seen.add(k)
            uniq.append(f)
    return uniq


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--history", action="store_true")
    ap.add_argument("--json", type=Path, default=None, help="write the report here")
    ap.add_argument("--root", type=Path, default=ROOT)
    a = ap.parse_args(argv)
    findings = scan_history(a.root) if a.history else scan_tree(a.root)
    report = {"mode": "history" if a.history else "working-tree", "findings": len(findings), "items": findings}
    if a.json:
        a.json.write_text(json.dumps(report, indent=1), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("mode", "findings")}))
    for f in findings[:50]:
        print(f"  {f['file']}:{f['line']} {f['rule']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
