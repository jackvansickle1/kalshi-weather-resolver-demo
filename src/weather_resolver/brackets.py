from __future__ import annotations

import re

from .models import Bracket


NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?")


def parse_bracket(label: str) -> Bracket:
    text = " ".join(label.strip().lower().split())
    values = [float(item) for item in NUMBER_RE.findall(text)]
    if not values:
        raise ValueError(f"No numeric temperature found in bracket label: {label!r}")

    if "or below" in text or "or lower" in text or "below" in text:
        return Bracket(label=label, low_f=None, high_f=values[0])

    if "or above" in text or "or higher" in text or "above" in text:
        return Bracket(label=label, low_f=values[0], high_f=None)

    if len(values) >= 2:
        low, high = min(values[0], values[1]), max(values[0], values[1])
        return Bracket(label=label, low_f=low, high_f=high)

    exact = values[0]
    return Bracket(label=label, low_f=exact, high_f=exact)


def resolve_bracket(label: str, actual_high_f: float) -> str:
    bracket = parse_bracket(label)
    return "yes" if bracket.contains(actual_high_f) else "no"

