"""FEAT-01: exact-key lookup (AC-01, AC-02, AC-03; F-30, F-31, F-32)."""

from fastapi.testclient import TestClient

from tests.conftest import auth


def test_ac01_exact_key_returns_that_record(client: TestClient, dispatcher: dict[str, str]) -> None:
    r = client.get("/records/SHI-00002", headers=dispatcher)
    assert r.status_code == 200
    assert r.json()["shipment_id"] == "SHI-00002"


def test_ac02_unknown_well_formed_key_is_404_and_never_another_record(client: TestClient, dispatcher: dict[str, str]) -> None:
    r = client.get("/records/SHI-99999", headers=dispatcher)
    assert r.status_code == 404
    assert r.headers["content-type"].startswith("application/problem+json")
    assert "shipment_id" not in r.json()


def test_ac03_cross_entity_key_is_rejected(client: TestClient, dispatcher: dict[str, str]) -> None:
    assert client.get("/records/REC-0001", headers=dispatcher).status_code == 422


def test_f31_non_key_column_value_does_not_match(client: TestClient, dispatcher: dict[str, str]) -> None:
    # CUS-00002 is a customer_id of shipment SHI-00002; the legacy scan-all-columns lookup found it.
    assert client.get("/records/CUS-00002", headers=dispatcher).status_code == 422


def test_quarantined_duplicate_key_resolves_to_one_curated_row(client: TestClient, dispatcher: dict[str, str]) -> None:
    body = client.get("/shipments?limit=100&offset=0", headers=dispatcher).json()
    ids = [i["shipment_id"] for i in body["items"]]
    assert len(ids) == len(set(ids))


def test_list_is_paged_and_filterable(client: TestClient, dispatcher: dict[str, str]) -> None:
    r = client.get("/shipments?limit=5&status=queued", headers=dispatcher).json()
    assert r["limit"] == 5 and len(r["items"]) <= 5
    assert all(i["status"] == "queued" for i in r["items"])


def test_bad_paging_is_422(client: TestClient, dispatcher: dict[str, str]) -> None:
    assert client.get("/shipments?limit=0", headers=dispatcher).status_code == 422
    assert client.get("/shipments?limit=101", headers=dispatcher).status_code == 422


def test_events_of_unknown_shipment_is_404(client: TestClient) -> None:
    assert client.get("/shipments/SHI-99999/events", headers=auth("dispatcher")).status_code == 404


def test_events_of_known_shipment(client: TestClient) -> None:
    r = client.get("/shipments/SHI-00002/events", headers=auth("dispatcher"))
    assert r.status_code == 200 and isinstance(r.json(), list) and r.json()
