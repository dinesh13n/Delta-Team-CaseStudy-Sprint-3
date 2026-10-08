"""Characterization tests (runbook step C8): pin CURRENT behaviour of the as-delivered code.

Labels used in every docstring:
  INTENDED-LEGACY  behaviour that is meant to be preserved
  DEFECT-SCHEDULED defect that Stage H will change by approved decision; the test's
                   failure after that change is the proof of an intentional change.
"""

import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "characterization: pins current brownfield behaviour")


@pytest.fixture()
def client(settings):
    """After Stage H the client targets the transformed app (settings fixture from tests/conftest.py)."""
    from fastapi.testclient import TestClient

    from apps.api.main import create_app

    return TestClient(create_app(settings))


def pytest_collection_modifyitems(config, items):
    """Tests listed in approved_changes.json pin BASELINE behaviour that Stage H changed on purpose.

    They are marked xfail(strict=True): a failure is the proof of the approved change; an unexpected PASS fails the
    run, which would mean the behaviour did not change as documented (see docs/16-repo-validation/behavior-difference-report.md).
    """
    import json
    from pathlib import Path

    reg = json.loads((Path(__file__).parent / "approved_changes.json").read_text())
    for item in items:
        name = item.name
        if name in reg:
            item.add_marker(
                pytest.mark.xfail(
                    strict=True, reason=f"APPROVED CHANGE {reg[name]['id']}: {reg[name]['summary']} (spec {reg[name]['spec']})"
                )
            )
