from __future__ import annotations

import argparse

from .brackets import resolve_bracket


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve a weather market bracket from an observed daily high.")
    parser.add_argument("--label", required=True, help='Bracket label, for example "72 to 74" or "80 or above".')
    parser.add_argument("--actual", type=float, required=True, help="Observed daily high temperature in Fahrenheit.")
    args = parser.parse_args()
    print(resolve_bracket(args.label, args.actual))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

