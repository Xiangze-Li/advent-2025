import itertools


def solve(data: str):
    coords: list[tuple[int, int]] = [
        tuple(map(int, line.split(",", 2))) for line in data.splitlines()
    ]  # type: ignore
    circular = coords.copy() + [coords[0]]

    area_1 = 0
    area_2 = 0
    for (x1, y1), (x2, y2) in itertools.combinations(coords, 2):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        area = (max_x - min_x + 1) * (max_y - min_y + 1)

        area_1 = max(area_1, area)
        for (cx1, cy1), (cx2, cy2) in itertools.pairwise(circular):
            if not (
                max(cx1, cx2) <= min_x
                or max_x <= min(cx1, cx2)
                or max(cy1, cy2) <= min_y
                or max_y <= min(cy1, cy2)
            ):
                break
        else:
            area_2 = max(area_2, area)

    yield area_1
    yield area_2


if __name__ == "__main__":
    from example import get

    for res in solve(get(9)):
        print(res)
