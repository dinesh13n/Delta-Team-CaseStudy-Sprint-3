"""Conformance: the application agrees with the semantic layer (semantic-layer/*.yaml, api-contract.json).
The layer is the source of truth; a mismatch means the application or the layer must change."""

from __future__ import annotations

import json

import yaml
from conftest import SECRET

from apps.api import main as api_main
from apps.api.ai import providers
from apps.api.config import _semantic_dir
from apps.api.security.policy import MASK
from apps.api.security.tokens import issue_dev_token

SL = _semantic_dir()


def _y(n: str) -> dict:
    return yaml.safe_load((SL / f"{n}.yaml").read_text(encoding="utf-8"))


def test_platform_roles_in_code_equal_the_layer() -> None:
    declared = {r: v["endpoint_class"] for r, v in _y("access-semantics")["platform_roles"].items()}
    assert declared == api_main.PLATFORM_ROLES


def test_retry_ceiling_and_status_sets_equal_the_layer() -> None:
    ws = _y("workflow-semantics")
    assert ws["ai_decision_semantics"]["retry_ceiling"]["value"] == providers.RETRY_CEILING
    canon = set(_y("status-taxonomy")["enums"]["shipment_status"]["values"])
    assert canon == providers.EXCEPTION_STATUSES | providers.IN_DOMAIN_OK


def test_mask_token_equals_the_layer() -> None:
    assert _y("access-semantics")["operating_semantics"]["field_mask"]["token"] == MASK


def test_operations_equal_the_api_contract() -> None:
    contract = json.loads((SL / "api-contract.json").read_text(encoding="utf-8"))
    declared = {(o["method"].lower(), o["path"]) for o in contract["operations"]}
    actual = {(m, p) for p, v in api_main.app.openapi()["paths"].items() for m in v}
    assert declared == actual


def test_audit_write_failure_fails_closed(settings, data_dir) -> None:  # noqa: ANN001
    from fastapi.testclient import TestClient

    app = api_main.create_app(settings)
    tok = issue_dev_token(SECRET, "u1", "dispatcher", purpose="dispatch")
    client = TestClient(app, raise_server_exceptions=False)
    rid = client.get("/shipments", headers={"Authorization": f"Bearer {tok}"}).json()["items"][0]["shipment_id"]
    assert rid

    def boom(_ev):  # noqa: ANN001, ANN202
        raise OSError("disk full")

    app.state.svc.audit.append = boom
    r = client.get(f"/records/{rid}", headers={"Authorization": f"Bearer {tok}"})
    assert r.status_code == 500 and rid not in r.text
