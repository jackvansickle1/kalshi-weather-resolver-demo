from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Bracket:
    label: str
    low_f: float | None
    high_f: float | None

    def contains(self, value_f: float) -> bool:
        if self.low_f is not None and value_f < self.low_f:
            return False
        if self.high_f is not None and value_f > self.high_f:
            return False
        return True


@dataclass(frozen=True)
class Observation:
    station: str
    observed_at: datetime
    temp_f: float

