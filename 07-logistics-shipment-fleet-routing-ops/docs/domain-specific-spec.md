# Logistics: Shipment, Fleet, Routing & Exception Operations

## Centre of Gravity

Distributed state, partner failures, event ordering, route constraints, ETA provenance, and cost per shipment.

## Enterprise Context

This repository represents a brownfield estate built over several engineering generations: legacy scripts and files, partially modernized APIs, operational portals, synthetic enterprise data, and newly introduced AI assistance. The design is intentionally credible rather than clean. Participants must infer reality by reading code, data, configuration, tests, docs, and operational artifacts.

## Business Flows

- Booking to pickup
- Hub scan to route assignment
- Carrier booking saga
- Exception investigation to delivery evidence

## Core Personas and Identities

- `dispatcher`
- `warehouse_ops`
- `fleet_manager`
- `driver`
- `customs_agent`
- `customer_support`
- `carrier_partner`
- `ai_agent`

## Domain Data Model

- `shipments`: shipment_id, customer_id, origin, destination, service_tier, declared_weight_kg, actual_weight_kg, promised_at, status, customs_required, temperature_controlled
- `tracking_events`: event_id, shipment_id, event_type, event_time, source_system, location, sequence_no, duplicate_flag, timezone, confidence
- `vehicles`: vehicle_id, vehicle_type, capacity_kg, current_location, driver_id, maintenance_status, cold_chain_capable, fuel_level_pct, region
- `routes`: route_id, origin, destination, distance_km, restricted_zone_flag, weather_risk, border_risk, estimated_cost, eta_minutes
- `carrier_bookings`: booking_id, shipment_id, carrier, status, retry_count, partner_ref, created_at, compensation_required
- `ai_invocations`: ai_call_id, shipment_id, use_case, model, route_candidates, token_count, constraint_violations, recommendation, human_override

## What Makes This a Strong Brownfield Candidate

- multiple teams appear to own overlapping capabilities
- legacy and modern paths disagree on semantics
- AI is assistive but insufficiently governed
- audit evidence exists but cannot yet reconstruct the full decision chain
- authorization is role-centric and needs contextual policy
- reliability behavior is uneven across synchronous, batch, and event paths
- cost and token usage are visible in fragments but not tied to business outcomes
