# Kalshi Weather Resolver Demo

Recruiter-facing slice of a weather-market trading system. This repository keeps the public, non-sensitive parts: contract bracket parsing, station-based settlement resolution, and a small CLI/test harness.

## What This Demonstrates

- Dataclass-based domain modeling for weather contracts and observations
- Robust bracket parsing for ranges, "or above", and "or below" contracts
- Settlement logic that uses observed station highs instead of vague city-level weather
- Input validation and clear error handling
- Unit tests around edge cases

## What Is Intentionally Not Included

- API credentials, private keys, `.env` files, databases, logs, or trade history
- Automated execution, order placement, sizing, model weighting, optimization, or live strategy logic
- Any proprietary thresholds or profitable signal-generation code

This is a clean code sample. It is not a trading bot and it is not financial advice.

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
pytest
python -m weather_resolver.cli --label "72 to 74" --actual 73.4
```

