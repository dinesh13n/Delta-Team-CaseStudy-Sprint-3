"""Runtime settings read once from the environment (spec: security-spec, feature-flag-plan FF-01..FF-07)."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEGACY_ONLY_LOCAL = "legacy modes are allowed only when APP_ENV=local"
MIN_SECRET_LEN = 32


class ConfigError(RuntimeError):
    """Raised at start-up when configuration is unsafe or incomplete."""


def _semantic_dir() -> Path:
    env = os.environ.get("SEMANTIC_LAYER_DIR")
    if env:
        return Path(env)
    for cand in (ROOT / "semantic-layer", ROOT.parent / "semantic-layer"):
        if cand.is_dir():
            return cand
    return ROOT / "semantic-layer"


@dataclass(frozen=True)
class Settings:
    app_env: str = "local"
    auth_mode: str = "hs256"  # FF-01: hs256 | jwks | legacy_header (local only)
    auth_secret: str | None = None
    lookup_mode: str = "exact"  # FF-02: exact | legacy (local only)
    data_layer: str = "curated"  # FF-03: curated | fixture
    ai_provider: str = "deterministic"  # FF-04: deterministic | model
    ai_enabled: bool = True  # FF-07 kill switch
    ai_rate_per_minute: int = 30
    ai_timeout_s: float = 5.0
    ai_breaker_threshold: int = 5
    ai_breaker_reset_s: float = 30.0
    data_max_age_s: float = 0.0  # 0 = freshness not checked; otherwise /ready fails when the last ETL run is older (M3 drill 4)
    data_dir: Path = ROOT / "data"
    audit_path: Path = ROOT / "logs" / "audit-v2.log"
    approvals_path: Path = ROOT / "logs" / "approvals.jsonl"
    semantic_dir: Path = ROOT / "semantic-layer"
    tenant: str = "default"
    log_level: str = "INFO"

    @property
    def is_local(self) -> bool:
        return self.app_env == "local"


def load_settings(env: dict[str, str] | None = None) -> Settings:
    e = os.environ if env is None else env
    s = Settings(
        app_env=e.get("APP_ENV", "local"),
        auth_mode=e.get("AUTH_MODE", "hs256"),
        auth_secret=e.get("AUTH_SECRET") or None,
        lookup_mode=e.get("LOOKUP_MODE", "exact"),
        data_layer=e.get("DATA_LAYER", "curated"),
        ai_provider=e.get("AI_PROVIDER", "deterministic"),
        ai_enabled=e.get("AI_ENABLED", "true").lower() == "true",
        ai_rate_per_minute=int(e.get("AI_RATE_PER_MINUTE", "30")),
        ai_timeout_s=float(e.get("AI_PROVIDER_TIMEOUT_S", "5")),
        ai_breaker_threshold=int(e.get("AI_BREAKER_THRESHOLD", "5")),
        ai_breaker_reset_s=float(e.get("AI_BREAKER_RESET_S", "30")),
        data_max_age_s=float(e.get("DATA_MAX_AGE_S", "0")),
        data_dir=Path(e["DATA_DIR"]) if e.get("DATA_DIR") else ROOT / "data",
        audit_path=Path(e["AUDIT_PATH"]) if e.get("AUDIT_PATH") else ROOT / "logs" / "audit-v2.log",
        approvals_path=Path(e["APPROVALS_PATH"]) if e.get("APPROVALS_PATH") else ROOT / "logs" / "approvals.jsonl",
        semantic_dir=_semantic_dir(),
        tenant=e.get("TENANT", "default"),
        log_level=e.get("LOG_LEVEL", "INFO"),
    )
    validate(s)
    return s


def validate(s: Settings) -> None:
    if s.auth_mode not in {"hs256", "jwks", "legacy_header"}:
        raise ConfigError(f"AUTH_MODE {s.auth_mode!r} is not supported")
    if s.lookup_mode not in {"exact", "legacy"}:
        raise ConfigError(f"LOOKUP_MODE {s.lookup_mode!r} is not supported")
    if s.data_layer not in {"curated", "fixture"}:
        raise ConfigError(f"DATA_LAYER {s.data_layer!r} is not supported")
    if s.ai_provider not in {"deterministic", "model"}:
        raise ConfigError(f"AI_PROVIDER {s.ai_provider!r} is not supported")
    if s.data_max_age_s < 0:
        raise ConfigError("DATA_MAX_AGE_S must not be negative")
    if s.ai_timeout_s <= 0 or s.ai_breaker_threshold < 1 or s.ai_breaker_reset_s <= 0:
        raise ConfigError("AI timeout, breaker threshold and reset must be positive")
    if not s.is_local and (s.auth_mode == "legacy_header" or s.lookup_mode == "legacy"):
        raise ConfigError(LEGACY_ONLY_LOCAL)
    if s.auth_mode == "hs256":
        if not s.auth_secret:
            if not s.is_local:
                raise ConfigError("AUTH_SECRET is required outside local mode")
        elif len(s.auth_secret) < MIN_SECRET_LEN:
            raise ConfigError(f"AUTH_SECRET must be at least {MIN_SECRET_LEN} characters")
