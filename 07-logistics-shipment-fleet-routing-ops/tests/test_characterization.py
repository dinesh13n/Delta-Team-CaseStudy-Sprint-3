"""Original characterization test, adapted (approved change AB-01, F-32/F-51).

The delivered test asserted that a missing record returns a row. The approved behaviour is the opposite: the legacy
function is retained only for LOOKUP_MODE=legacy; the API returns 404 (tests/test_record_lookup.py).
"""

from apps.api.services import domain_service


def test_legacy_missing_record_behavior_is_still_characterized_for_legacy_mode_only():
    row = domain_service.load_record("DOES-NOT-EXIST")
    assert isinstance(row, dict) and row  # legacy module unchanged; unreachable unless LOOKUP_MODE=legacy (local)
