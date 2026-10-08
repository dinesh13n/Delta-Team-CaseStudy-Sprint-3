# Synthetic Data

Domain: Logistics: Shipment, Fleet, Routing & Exception Operations

This data is fully synthetic and designed for realistic workshop discovery. It includes enough volume for baseline profiling, ETL validation, event-correlation exercises, observability design, AI FinOps analysis, and data-quality remediation.

## Included Files

- `synthetic/shipments.csv`: 354 rows
- `synthetic/tracking_events.csv`: 354 rows
- `synthetic/vehicles.csv`: 354 rows
- `synthetic/routes.csv`: 354 rows
- `synthetic/carrier_bookings.csv`: 354 rows
- `synthetic/ai_invocations.csv`: 354 rows
- `synthetic/events.jsonl`: 3000 operational events

## Deliberate Data Problems

- duplicate identifiers and duplicate business events
- blank mandatory fields
- stale or impossible timestamps
- out-of-range scores
- untrusted text payloads suitable for prompt-injection testing
- missing correlation identifiers
- mixed legacy and modern source-system semantics
