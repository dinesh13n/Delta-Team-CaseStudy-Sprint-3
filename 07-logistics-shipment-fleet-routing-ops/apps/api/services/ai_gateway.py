"""Compatibility shim. The AI gateway moved to apps.api.ai.gateway (H7, F-22..F-29).

The previous implementation formatted a prompt with str.format() from record data and reported
guardrail_status "not_enforced"; it has been removed with no flag to bring it back (FF-05).
"""

from apps.api.ai.gateway import AiGateway  # noqa: F401
