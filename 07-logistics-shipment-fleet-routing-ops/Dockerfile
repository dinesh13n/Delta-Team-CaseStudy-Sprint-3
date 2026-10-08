# Platform-neutral container recipe (ADR-0009, F-07).
# BUILD CONTEXT IS THE REPOSITORY ROOT (the semantic layer lives one level above this directory):
#   docker build -f 07-logistics-shipment-fleet-routing-ops/Dockerfile -t logistics-api .
# NOT BUILT: no container runtime was available while this was written (CONDITIONAL). Corrected in P2 after a clean-copy exercise showed the
# previous recipe could not find the semantic layer and never published data before serving.
FROM python:3.14-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 APP_ENV=prod SEMANTIC_LAYER_DIR=/app/semantic-layer
WORKDIR /app
COPY 07-logistics-shipment-fleet-routing-ops/requirements.txt .
RUN python -m pip install --no-cache-dir --require-hashes -r requirements.txt
COPY 07-logistics-shipment-fleet-routing-ops/apps ./apps
COPY 07-logistics-shipment-fleet-routing-ops/etl ./etl
COPY 07-logistics-shipment-fleet-routing-ops/data/contracts ./data/contracts
COPY 07-logistics-shipment-fleet-routing-ops/data/synthetic ./data/synthetic
COPY semantic-layer ./semantic-layer
COPY 07-logistics-shipment-fleet-routing-ops/docker-entrypoint.sh ./docker-entrypoint.sh
RUN useradd --system --uid 10001 app && mkdir -p /app/logs /app/data && chown -R app /app/logs /app/data
USER app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"
# AUTH_SECRET must be injected by the platform secret store; the app refuses to start without it when APP_ENV is not local.
CMD ["sh", "./docker-entrypoint.sh"]
