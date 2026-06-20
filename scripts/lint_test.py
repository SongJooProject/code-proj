#!/usr/bin/env python3
"""Lint and test automation script."""

import subprocess
import sys


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"\n{'=' * 50}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print("=" * 50)

    result = subprocess.run(cmd, capture_output=False)

    if result.returncode != 0:
        print(f"\n[FAIL] {description} failed!")
        return False

    print(f"\n[PASS] {description} completed.")
    return True


def main() -> int:
    """Run all checks."""
    print("\n" + "=" * 50)
    print("  Python Project Automation Script")
    print("=" * 50)

    # Ruff check
    if not run_command(["ruff", "check", "."], "Ruff Linting"):
        return 1

    # Ruff format
    if not run_command(["ruff", "format", "."], "Ruff Format"):
        return 1

    # Pytest
    if not run_command([sys.executable, "-m", "pytest", "tests/", "-v"], "Pytest"):
        return 1

    print("\n" + "=" * 50)
    print("  All checks passed!")
    print("=" * 50)

    return 0


if __name__ == "__main__":
    sys.exit(main())
