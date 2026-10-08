package logistics.access_test

import data.logistics.access
import rego.v1

# Positive cases
test_dispatcher_can_write_shipments_for_dispatch if {
	access.allow with input as {"persona": "dispatcher", "entity": "shipments", "action": "write", "purpose": "dispatch"}
}

test_support_can_read_shipments_for_support if {
	access.allow with input as {"persona": "customer_support", "entity": "shipments", "action": "read", "purpose": "customer_support"}
}

# Negative cases (F-18, F-19, F-20)
test_support_cannot_write_shipments if {
	not access.allow with input as {"persona": "customer_support", "entity": "shipments", "action": "write", "purpose": "customer_support"}
}

test_wrong_purpose_denied if {
	not access.allow with input as {"persona": "dispatcher", "entity": "shipments", "action": "read", "purpose": "marketing"}
}

test_clinician_is_not_a_persona if {
	not access.allow with input as {"persona": "clinician", "entity": "shipments", "action": "read", "purpose": "dispatch"}
}

test_ai_agent_has_no_vehicle_access if {
	not access.allow with input as {"persona": "ai_agent", "entity": "vehicles", "action": "read", "purpose": "exception_summary"}
}

test_admin_is_not_a_blanket_allow if {
	not access.allow with input as {"persona": "admin", "entity": "shipments", "action": "read", "purpose": "dispatch"}
}
