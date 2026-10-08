"""Version-controlled prompt registry (F-27). The config hash binds prompt text, provider and limits."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

PROMPT_DIR = Path(__file__).resolve().parent / "prompts"
LOCK_PATH = PROMPT_DIR / "prompts.lock.json"
MODEL_LOCK_PATH = PROMPT_DIR / "models.lock.json"


class PromptIntegrityError(Exception):
    """A prompt file differs from prompts.lock.json (or has no lock entry): refuse to serve (P-X3)."""


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Prompt:
    name: str
    version: str
    text: str

    @property
    def prompt_version(self) -> str:
        return f"{self.name}_{self.version}"

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()


REGISTRY = {("exception_summary", "v1"): "exception_summary_v1.txt"}
CURRENT = ("exception_summary", "v1")


def load(name: str = CURRENT[0], version: str = CURRENT[1]) -> Prompt:
    text = (PROMPT_DIR / REGISTRY[(name, version)]).read_text(encoding="utf-8")
    prompt = Prompt(name, version, text)
    try:
        lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PromptIntegrityError("prompts.lock.json is missing or unreadable") from exc
    if lock.get(prompt.prompt_version) != prompt.sha256:
        raise PromptIntegrityError(f"prompt {prompt.prompt_version} does not match prompts.lock.json")
    return prompt


def config_hash(prompt: Prompt, provider_name: str, provider_version: str, max_record_tokens: int) -> str:
    raw = "|".join([prompt.sha256, provider_name, provider_version, str(max_record_tokens)])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def verify_model(name: str, version: str) -> None:
    """P-X3 for models: only a (provider, version) pair listed in models.lock.json may be put into service.

    Adding or upgrading a model therefore needs a reviewed change to the lock file (CODEOWNERS), exactly like a prompt change.
    """
    try:
        lock = json.loads(MODEL_LOCK_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PromptIntegrityError("models.lock.json is missing or unreadable") from exc
    if lock.get(name) != version:
        raise PromptIntegrityError(f"model {name} {version} is not listed in models.lock.json")
