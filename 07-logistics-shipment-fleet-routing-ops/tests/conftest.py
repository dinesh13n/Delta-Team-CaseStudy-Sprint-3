"""Shared fixtures. The fixture data/synthetic is copied (never modified) into a temp dir; ETL builds the curated layer."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from apps.api.config import ROOT, Settings, _semantic_dir
from apps.api.main import create_app
from apps.api.security.tokens import issue_dev_token
from etl.run_daily_batch import run as run_etl

SECRET = "unit-test-secret-" + "x" * 32  # secret-scan: allow (test-only value, not a credential)


@pytest.fixture(scope="session")
def data_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    d = tmp_path_factory.mktemp("data")
    shutil.copytree(ROOT / "data" / "synthetic", d / "synthetic")
    run_etl(d, d, _semantic_dir(), 0.05, False)
    return d


@pytest.fixture()
def settings(data_dir: Path, tmp_path: Path) -> Settings:
    return Settings(
        app_env="local",
        auth_mode="hs256",
        auth_secret=SECRET,
        data_dir=data_dir,
        audit_path=tmp_path / "audit.log",
        approvals_path=tmp_path / "approvals.jsonl",
        semantic_dir=_semantic_dir(),
        ai_rate_per_minute=1000,
    )


@pytest.fixture()
def client(settings: Settings) -> TestClient:
    return TestClient(create_app(settings))


def auth(role: str, subject: str = "u-test", purpose: str | None = None, secret: str = SECRET, ttl: int = 3600) -> dict[str, str]:
    return {"Authorization": "Bearer " + issue_dev_token(secret, subject, role, purpose=purpose, ttl=ttl)}


@pytest.fixture()
def dispatcher() -> dict[str, str]:
    return auth("dispatcher")
