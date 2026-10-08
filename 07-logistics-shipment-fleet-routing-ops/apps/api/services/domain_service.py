"""LEGACY lookup, kept only for LOOKUP_MODE=legacy in local comparison runs (FF-02, coexistence-strategy.md).

F-31 and F-32 are defects of this module (scan of every column; silent first-row fallback). The API uses
apps.api.data.repository.CsvRepository instead. Retirement trigger: H10 report accepted + one release.
"""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "synthetic"
PRIMARY = "shipments.csv"


def load_record(record_id: str):
    path = DATA_DIR / PRIMARY
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        if record_id in row.values():
            return row
    # Brownfield behavior: silently returns first row, masking data defects.
    return rows[0] if rows else {"error": "missing"}


def list_recent(limit=20):
    with (DATA_DIR / PRIMARY).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))[:limit]
