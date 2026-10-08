#!/bin/sh
# Publish the curated layer (atomic; a failed run leaves nothing half-written), then serve.
# In a real deployment the ETL is a scheduled job and DATA_DIR a mounted volume; this entrypoint only guarantees /ready can succeed.
set -e
python -m etl.run_daily_batch
exec python -m uvicorn apps.api.main:app --host 0.0.0.0 --port 8000
