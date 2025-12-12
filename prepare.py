#!/usr/bin/env python
import requests
import os
import argparse

TEMPLATE = """def solve(data: str):
    pass


if __name__ == "__main__":
    from example import get

    solve(get({}))
"""


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2025 Preparer")
    parser.add_argument(
        "day",
        type=int,
        choices=range(1, 13),
        metavar="day",
        help="day of the Advent of Code (1-12)",
    )

    args = parser.parse_args()
    prepare(args.day)


def prepare(day: int):
    with open(f"{os.getenv("HOME", "")}/.adventofcode.session") as f:
        session = f.read().strip()

    with requests.get(
        f"https://adventofcode.com/2025/day/{day}/input",
        cookies={"session": session},
    ) as resp:
        if resp.status_code != 200:
            raise ConnectionError(
                f"Failed to fetch input data for day {day}: {resp.status_code} {resp.text}"
            )
        with open(f"input/{day:02d}.txt", "w") as f:
            f.write(resp.text)

    with open(f"day{day:02d}.py", "w") as f:
        f.write(TEMPLATE.format(day))
    with open(f"example/{day:02d}.txt", "w") as f:
        pass


if __name__ == "__main__":
    main()
