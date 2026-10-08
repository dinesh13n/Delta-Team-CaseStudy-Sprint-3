"""Issue a short-lived development bearer token (local use only).

    AUTH_SECRET=<>=32 chars> python -m scripts.issue_dev_token dispatcher [subject] [ttl_seconds]

Refuses to run unless APP_ENV is local. Tokens are HS256 with the same secret the API verifies (apps/api/security/tokens.py).
"""

from __future__ import annotations

import os
import sys

from apps.api.security.tokens import issue_dev_token


def main(argv: list[str]) -> int:
    if os.environ.get("APP_ENV", "local") != "local":
        print("refused: development tokens are for APP_ENV=local only", file=sys.stderr)
        return 2
    secret = os.environ.get("AUTH_SECRET", "")
    if len(secret) < 32:
        print("AUTH_SECRET (>= 32 chars) is required", file=sys.stderr)
        return 2
    role = argv[1] if len(argv) > 1 else "dispatcher"
    subject = argv[2] if len(argv) > 2 else "dev-user"
    ttl = int(argv[3]) if len(argv) > 3 else 3600
    print(issue_dev_token(secret, subject, role, ttl=ttl))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
