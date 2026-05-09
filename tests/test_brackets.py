from weather_resolver import parse_bracket, resolve_bracket


def test_range_bracket_contains_values_inside_range():
    bracket = parse_bracket("72 to 74")
    assert bracket.low_f == 72
    assert bracket.high_f == 74
    assert resolve_bracket("72 to 74", 73.2) == "yes"


def test_range_bracket_rejects_values_outside_range():
    assert resolve_bracket("72 to 74", 75.1) == "no"


def test_or_above_bracket():
    assert resolve_bracket("80 or above", 84.0) == "yes"
    assert resolve_bracket("80 or above", 79.9) == "no"


def test_or_below_bracket():
    assert resolve_bracket("65 or below", 64.8) == "yes"
    assert resolve_bracket("65 or below", 67.0) == "no"

