"""Configuration and secrets (AC-24; F-09..F-13, F-15)."""

import pytest

from apps.api.config import ConfigError, load_settings


def test_ac24_refuses_to_start_without_secret_outside_local() -> None:
    with pytest.raises(ConfigError, match="AUTH_SECRET"):
        load_settings({"APP_ENV": "prod"})


def test_short_secret_rejected() -> None:
    with pytest.raises(ConfigError, match="32"):
        load_settings({"APP_ENV": "prod", "AUTH_SECRET": "short"})


def test_legacy_modes_only_in_local() -> None:
    with pytest.raises(ConfigError):
        load_settings({"APP_ENV": "prod", "AUTH_SECRET": "x" * 40, "AUTH_MODE": "legacy_header"})
    with pytest.raises(ConfigError):
        load_settings({"APP_ENV": "staging", "AUTH_SECRET": "x" * 40, "LOOKUP_MODE": "legacy"})
    assert load_settings({"APP_ENV": "local", "AUTH_MODE": "legacy_header"}).auth_mode == "legacy_header"


def test_unknown_values_rejected() -> None:
    for k, v in (("AUTH_MODE", "basic"), ("DATA_LAYER", "db"), ("AI_PROVIDER", "x"), ("LOOKUP_MODE", "fuzzy")):
        with pytest.raises(ConfigError):
            load_settings({k: v})


def test_local_defaults_are_safe() -> None:
    s = load_settings({})
    assert (s.auth_mode, s.lookup_mode, s.data_layer, s.ai_provider, s.ai_enabled, s.log_level) == (
        "hs256",
        "exact",
        "curated",
        "deterministic",
        True,
        "INFO",
    )
