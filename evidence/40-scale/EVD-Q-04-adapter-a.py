"""Model A shim for the portability harness: exposes summarize_case(case, provider) over Model A's AiGateway.
Run with PYTHONPATH = the 07-* root. This file is the ONLY Model A-specific piece of the eval harness."""
from __future__ import annotations
import json
from apps.api.ai.gateway import AiGateway
from apps.api.ai.providers import DeterministicProvider, ProviderResult, ProviderUnavailable
from apps.api.ai.sanitize import load_enums
from apps.api.config import _semantic_dir
from apps.api.data.repository import load_entities
from apps.api.security.policy import PolicyEngine
from evaluation.run_eval import MemRepo

_sem = _semantic_dir()
_ents = load_entities(_sem)
_pol = PolicyEngine.from_dir(_sem).ai_policy
_enums = load_enums(_sem)


class _Wrap:
    def __init__(self, fn):
        self.fn, self.name, self.version = fn, "callable", "1"

    def complete(self, parts, facts):
        try:
            return ProviderResult(self.fn(parts.system, parts.data_json))
        except ConnectionError as e:
            raise ProviderUnavailable(str(e))


def summarize_case(case, provider=None):
    repo = MemRepo(case, _ents)
    prov = DeterministicProvider() if provider is None else _Wrap(provider)
    gw = AiGateway(repo, _pol, prov, enums=_enums)
    return gw.summarize(case["shipment"]["shipment_id"], "corr-eval-0001").output
