from typing import Iterable


DELTA_4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

DELTA_8 = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def enumerate_grid[T](grid: Iterable[Iterable[T]]):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            yield (i, j, val)
