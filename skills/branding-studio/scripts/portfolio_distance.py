#!/usr/bin/env python3
"""Compatibility wrapper. New workflows should call portfolio_collision.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from portfolio_collision import main  # noqa: E402

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Deprecated: use `python portfolio_collision.py portfolio.json spec.json`.")
        sys.exit(0)
    print("DEPRECATED: portfolio_distance.py now delegates to portfolio_collision.py.", file=sys.stderr)
    sys.exit(main(sys.argv[1], sys.argv[2]))
