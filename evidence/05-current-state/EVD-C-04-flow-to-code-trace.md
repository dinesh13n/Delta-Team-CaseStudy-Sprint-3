# EVD-C-04 Flow-to-code trace (2026-10-08)
| Declared flow | Code found | Status |
|---|---|---|
| Booking to pickup | none | NOT IMPLEMENTED |
| Hub scan to route assignment | none | NOT IMPLEMENTED |
| Carrier booking saga | none | NOT IMPLEMENTED |
| Exception investigation to delivery evidence | apps/api/main.py, domain_service.py, ai_gateway.py | PARTIAL |
| ETA prediction | none | NOT IMPLEMENTED |
| Route optimisation | none | NOT IMPLEMENTED |
| Exception copilot | ai_gateway.summarize_record (simulated) | NOT IMPLEMENTED (placeholder) |
Method: grep for domain verbs (book, pickup, scan, route, saga, retry, compensat, eta) across *.py: only data/CSV column names match.
