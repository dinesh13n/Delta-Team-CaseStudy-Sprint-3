"""Minimal in-process metrics with Prometheus text exposition (observability-spec, F-46)."""

from __future__ import annotations

import threading
from collections import defaultdict

BUCKETS = (0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0)


class Metrics:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._counters: dict[tuple[str, tuple[tuple[str, str], ...]], float] = defaultdict(float)
        self._gauges: dict[str, float] = {}
        self._hist: dict[tuple[str, tuple[tuple[str, str], ...]], list[float]] = {}

    @staticmethod
    def _key(name: str, labels: dict[str, str] | None) -> tuple[str, tuple[tuple[str, str], ...]]:
        return name, tuple(sorted((labels or {}).items()))

    def inc(self, name: str, value: float = 1.0, labels: dict[str, str] | None = None) -> None:
        with self._lock:
            self._counters[self._key(name, labels)] += value

    def set_gauge(self, name: str, value: float) -> None:
        with self._lock:
            self._gauges[name] = value

    def observe(self, name: str, seconds: float, labels: dict[str, str] | None = None) -> None:
        with self._lock:
            h = self._hist.setdefault(self._key(name, labels), [0.0] * (len(BUCKETS) + 2))
            for i, b in enumerate(BUCKETS):
                if seconds <= b:
                    h[i] += 1
            h[len(BUCKETS)] += 1  # +Inf / count
            h[len(BUCKETS) + 1] += seconds  # sum

    @staticmethod
    def _fmt(labels: tuple[tuple[str, str], ...], extra: str = "") -> str:
        parts = [f'{k}="{v}"' for k, v in labels] + ([extra] if extra else [])
        return "{" + ",".join(parts) + "}" if parts else ""

    def render(self) -> str:
        out: list[str] = []
        with self._lock:
            for (name, labels), v in sorted(self._counters.items()):
                out.append(f"{name}{self._fmt(labels)} {v:g}")
            for name, v in sorted(self._gauges.items()):
                out.append(f"{name} {v:g}")
            for (name, labels), h in sorted(self._hist.items()):
                for i, b in enumerate(BUCKETS):
                    le = 'le="' + str(b) + '"'
                    out.append(f"{name}_bucket{self._fmt(labels, le)} {h[i]:g}")
                inf = 'le="+Inf"'
                out.append(f"{name}_bucket{self._fmt(labels, inf)} {h[len(BUCKETS)]:g}")
                out.append(f"{name}_count{self._fmt(labels)} {h[len(BUCKETS)]:g}")
                out.append(f"{name}_sum{self._fmt(labels)} {h[len(BUCKETS) + 1]:g}")
        return "\n".join(out) + "\n"
