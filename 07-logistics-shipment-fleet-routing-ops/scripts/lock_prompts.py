"""Write apps/api/ai/prompts/prompts.lock.json: the SHA-256 of every registered prompt (P-X3).

    python -m scripts.lock_prompts

The API refuses to start the AI gateway when a prompt file differs from the lock, so a prompt cannot change in production without
a reviewed change to this lock file (CODEOWNERS covers it). Re-run only after a deliberate, reviewed prompt version change.
"""

from __future__ import annotations

import json

from apps.api.ai import registry


def main() -> None:
    lock = {f"{n}_{v}": registry.sha256_of(registry.PROMPT_DIR / f) for (n, v), f in registry.REGISTRY.items()}
    registry.LOCK_PATH.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(lock, indent=2))


if __name__ == "__main__":
    main()
