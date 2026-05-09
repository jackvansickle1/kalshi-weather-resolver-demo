from __future__ import annotations

from collections.abc import Iterable

from .models import Observation


def daily_high(observations: Iterable[Observation]) -> float:
    values = [obs.temp_f for obs in observations]
    if not values:
        raise ValueError("At least one station observation is required.")
    return max(values)


def station_summary(observations: Iterable[Observation]) -> dict[str, float]:
    grouped: dict[str, list[float]] = {}
    for obs in observations:
        grouped.setdefault(obs.station.upper(), []).append(obs.temp_f)
    return {station: max(values) for station, values in grouped.items()}

