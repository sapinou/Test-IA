#!/usr/bin/env python3
"""Check if a number is prime."""

from __future__ import annotations

import argparse


def is_prime(n: int) -> bool:
    """Return True if *n* is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check if a number is prime.")
    parser.add_argument("number", type=int, help="The integer to check.")
    args = parser.parse_args(argv)
    result = is_prime(args.number)
    print(f"{args.number} is {'a prime' if result else 'not a prime'} number.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
