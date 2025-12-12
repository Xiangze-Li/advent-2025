#!/usr/bin/env python

import argparse
import importlib
import time
import input


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2025 Solver")
    parser.add_argument(
        "day",
        type=int,
        choices=range(1, 13),
        metavar="day",
        help="day of the Advent of Code (1-12)",
    )

    args = parser.parse_args()
    try:
        solve(args.day)
    except Exception as e:
        print(e)


def solve(day: int):
    solver = importlib.import_module(f"day{day:02d}")

    if hasattr(solver, "solve") and callable(getattr(solver, "solve")):
        data = input.get(day)
        start = time.perf_counter_ns()
        res = [r for r in solver.solve(data)]
        end = time.perf_counter_ns()
        for r in res:
            print(r)
        print(f"Solved in {(end - start) / 1e6:.6f} ms.")
    else:
        raise NotImplementedError(f"No solve function found in module day{day:02d}.")


if __name__ == "__main__":
    main()
