# Glossary and Entity Definitions (Step D1)

| Field | Value |
|---|---|
| Stage | D: Semantic Layer Extraction |
| Runbook step | D1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL |
| Evidence sources | docs/domain-specific-spec.md; EVD-C-05; entities.yaml |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Markdown explains; `entities.yaml` defines (source of truth). Field coverage: 56 of 56 columns defined (EVD-D-01).

## Business terms
- **Shipment**: a consignment moving from an origin to a destination under a service tier.
- **Tracking event**: a dated record of something happening to a shipment (scan, departure, arrival, delay, exception, delivery).
- **Hub scan**: a tracking event produced when a parcel is read at a handling site.
- **Route**: a planned path between two locations with distance, cost, risk flags and estimated time.
- **Restricted zone**: an area a route may not cross without explicit permission.
- **Carrier booking**: a reservation of a shipment with a carrier partner; may be retried and may require compensation if it must be undone.
- **Carrier booking saga**: the multi-step booking process (book, confirm, compensate if required).
- **Exception**: any departure from the expected shipment path that needs investigation.
- **Correlation identifier**: a value that ties together every record created by one request or case.
- **Confidence**: a fraction between 0 and 1 stating how reliable a record is.
- **Human override**: a person's decision on a recommendation.
- **Assisted call**: a request to automated assistance about a shipment, recorded with its model and declared token count.
- **Persona**: a role of a person or automated agent that uses the system (eight are defined).
- **Purpose**: the reason for which data is accessed; access depends on persona and purpose.
- **Quarantine**: holding a record aside, counted and reportable, instead of accepting or discarding it.

## Entities

### shipments
A consignment moving from origin to destination. Dataset `shipments.csv`, business key `shipment_id`.

| Field | Type | Unit | Meaning | Observed blanks |
|---|---|---|---|---|
| shipment_id | string | - | Unique business identifier of a shipment, prefix SHI- | 0 |
| customer_id | string | - | Customer reference, prefix CUS- (customer entity is outside the dataset) | 1 |
| origin | location_ref | - | Origin location reference | 1 |
| destination | location_ref | - | Destination location reference | 1 |
| service_tier | enum | - | Contracted service level | 1 |
| declared_weight_kg | decimal | kg | Weight declared by the customer | 1 |
| actual_weight_kg | decimal | kg | Weight measured at handling | 1 |
| promised_at | timestamp | ISO-8601 local | Delivery time promised to the customer | 1 |
| status | enum | - | Lifecycle state of the shipment | 1 |
| customs_required | boolean | - | Whether customs clearance applies | 1 |
| temperature_controlled | boolean | - | Whether cold chain handling applies | 1 |

### tracking_events
A recorded event in the movement of a shipment. Dataset `tracking_events.csv`, business key `event_id`.

| Field | Type | Unit | Meaning | Observed blanks |
|---|---|---|---|---|
| event_id | string | - | Unique identifier of a tracking event, prefix EVE- | 0 |
| shipment_id | string | - | Shipment the event belongs to | 1 |
| event_type | enum | - | Kind of tracking event | 1 |
| event_time | timestamp | ISO-8601 local | When the event occurred | 1 |
| source_system | enum | - | System that produced the event | 1 |
| location | location_ref | - | Where the event occurred (location data) | 1 |
| sequence_no | integer | - | Ordering number of the event within its shipment | 1 |
| duplicate_flag | boolean | - | Producer-declared duplicate marker | 1 |
| timezone | timezone | - | Time zone of event_time | 1 |
| confidence | decimal | ratio 0..1 | Confidence of the event record | 1 |

### vehicles
A vehicle that can carry shipments. Dataset `vehicles.csv`, business key `vehicle_id`.

| Field | Type | Unit | Meaning | Observed blanks |
|---|---|---|---|---|
| vehicle_id | string | - | Unique vehicle identifier, prefix VEH- | 0 |
| vehicle_type | enum | - | Vehicle class | 1 |
| capacity_kg | decimal | kg | Load capacity | 1 |
| current_location | location_ref | - | Last known position (location data) | 1 |
| driver_id | string | - | Assigned driver, prefix DRI- (personal identifier) | 1 |
| maintenance_status | enum | - | Maintenance state | 1 |
| cold_chain_capable | boolean | - | Can carry temperature-controlled goods | 1 |
| fuel_level_pct | decimal | ratio 0..1 | Fuel level as a fraction | 1 |
| region | enum | - | Operating region | 1 |

### routes
A planned path between two locations. Dataset `routes.csv`, business key `route_id`.

| Field | Type | Unit | Meaning | Observed blanks |
|---|---|---|---|---|
| route_id | string | - | Unique route identifier, prefix ROU- | 0 |
| origin | location_ref | - | Route origin | 1 |
| destination | location_ref | - | Route destination | 1 |
| distance_km | decimal | km | Route length | 1 |
| restricted_zone_flag | boolean | - | Route crosses a restricted zone | 1 |
| weather_risk | enum | - | Weather risk class | 1 |
| border_risk | enum | - | Border crossing risk class | 1 |
| estimated_cost | decimal | cost units | Estimated cost of the route | 1 |
| eta_minutes | integer | minutes | Estimated travel time | 1 |

### carrier_bookings
A booking of a shipment with a carrier partner. Dataset `carrier_bookings.csv`, business key `booking_id`.

| Field | Type | Unit | Meaning | Observed blanks |
|---|---|---|---|---|
| booking_id | string | - | Unique booking identifier, prefix BOO- | 0 |
| shipment_id | string | - | Shipment being booked | 1 |
| carrier | carrier_ref | - | Carrier reference | 1 |
| status | enum | - | Booking state | 1 |
| retry_count | integer | count | Booking attempts made | 1 |
| partner_ref | string | - | Reference at the carrier partner, prefix PAR- | 1 |
| created_at | timestamp | ISO-8601 local | When the booking was created | 1 |
| compensation_required | boolean | - | Whether a compensating action is needed | 1 |

### ai_invocations
A call to automated assistance about a shipment. Dataset `ai_invocations.csv`, business key `ai_call_id`.

| Field | Type | Unit | Meaning | Observed blanks |
|---|---|---|---|---|
| ai_call_id | string | - | Unique identifier of an automated-assistance call, prefix AI_- | 0 |
| shipment_id | string | - | Shipment the call concerned | 1 |
| use_case | enum | - | Capability invoked | 1 |
| model | model_ref | - | Identifier of the model that served the call | 1 |
| route_candidates | integer | count | Number of route candidates considered | 1 |
| token_count | integer | tokens | Declared tokens consumed by the call | 1 |
| constraint_violations | enum | - | Constraint violation class reported | 1 |
| recommendation | enum | - | Outcome recommended by the assistance | 1 |
| human_override | enum | - | Human decision on the recommendation | 1 |
