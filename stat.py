#!/usr/bin/env python

import time
import input
import tabulate2
import importlib
import statistics

N = 10


def main():
    contents = []

    for day in range(1, 13):
        avg, med, stderr = stat(day)
        contents.append([f"{day:02d}", avg, med, stderr])

    table = tabulate2.tabulate(
        contents,
        headers=("Day", "Average (ms)", "Median (ms)", "StdErr (ms)"),
        tablefmt="github",
    )
    print(table)


def stat(day: int):
    solver = importlib.import_module(f"day{day:02d}")
    solve_func = getattr(solver, "solve", None)
    assert callable(solve_func), f"No solve function found in module day{day:02d}."
    data = input.get(day)

    timings: list[float] = [0 for _ in range(N)]

    for i in range(N):
        start = time.perf_counter_ns()
        [v for v in solve_func(data)] # type: ignore
        end = time.perf_counter_ns()
        timings[i] = (end - start) / 1_000_000

    avg: float = statistics.fmean(timings)
    med: float = statistics.median(timings)
    stderr: float = statistics.stdev(timings, avg)

    return avg, med, stderr


if __name__ == "__main__":
    main()
