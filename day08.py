import math
from sortedcollections import SortedDict


n = 1000


def solve(data: str):
    cords: list[tuple[int, int, int]] = []
    for line in data.splitlines():
        x, y, z = map(int, line.split(","))
        cords.append((x, y, z))

    dists = SortedDict()
    for i, cord_i in enumerate(cords):
        for j, cord_j in enumerate(cords[i + 1 :], start=i + 1):
            dists[math.dist(cord_i, cord_j)] = (i, j)

    circuits: dict[int, list[int]] = {i: [i] for i in range(len(cords))}
    belongs_to: list[int] = list(range(len(cords)))
    connection = 0
    for i, j in dists.values():
        if belongs_to[i] != belongs_to[j]:
            cid_i = belongs_to[i]
            cid_j = belongs_to[j]
            for k in circuits[cid_j]:
                belongs_to[k] = cid_i
            circuits[cid_i].extend(circuits[cid_j])
            del circuits[cid_j]

        connection += 1
        if connection == n:
            vals = list(circuits.values())
            vals.sort(key=len, reverse=True)
            yield math.prod(len(v) for v in vals[:3])

        if len(circuits) == 1:
            yield cords[i][0] * cords[j][0]
            break


if __name__ == "__main__":
    from example import get

    n = 10
    for res in solve(get(8)):
        print(res)
