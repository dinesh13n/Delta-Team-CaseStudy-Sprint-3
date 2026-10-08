# Legacy batch script retained after partial migration (see docs/14-transformation/coexistence-strategy.md).
import csv
import os
from pathlib import Path

# F-09: credentials are no longer in source. Supplied by the environment only, and unused by this reconcile step.
SHARED_DB_USER = os.environ.get("LEGACY_DB_USER", "")
SHARED_DB_PASSWORD = os.environ.get("LEGACY_DB_PASSWORD", "")


def reconcile():
    path = Path(__file__).resolve().parents[1] / "data" / "synthetic" / "shipments.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


if __name__ == "__main__":
    print("legacy reconciled", reconcile())
