#!/usr/bin/env python3
"""Minimal repository validation utility.

This script checks whether key project files exist.
Comments and docs are intentionally in English for consistency.
"""

from pathlib import Path
import sys

REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "docs/ROADMAP.md",
    "docs/CURATION_POLICY.md",
    "docs/TEMPLATE_STANDARD.md",
]


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    missing = [f for f in REQUIRED_FILES if not (root / f).exists()]

    if missing:
        print("Missing required files:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Validation passed: baseline files are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
