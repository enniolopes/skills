#!/usr/bin/env python3
"""Compatibility wrapper. New workflows should call validate_structure.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_structure import main  # noqa: E402

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Deprecated: use `python validate_structure.py spec.json`.")
        sys.exit(0)
    print("DEPRECATED: validate_spec.py now delegates to validate_structure.py.", file=sys.stderr)
    sys.exit(main(sys.argv[1]))
