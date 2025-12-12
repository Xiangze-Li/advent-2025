import pkg.ranges as ranges


def solve(data: str):
    sp = data.split("\n\n", 2)
    range = ranges.Ranges()
    for line in sp[0].splitlines():
        val = line.split("-", 2)
        range.add((int(val[0]), int(val[1])))

    count = 0
    for val in sp[1].splitlines():
        if range.check(int(val)):
            count += 1

    yield count

    yield sum(ub - lb + 1 for lb, ub in range)


if __name__ == "__main__":
    from example import get

    for res in solve(get(5)):
        print(res)
