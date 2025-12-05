import ranges


def solve(data: str) -> None:
    sp = data.split("\n\n", 2)
    range = ranges.Ranges()
    for line in sp[0].splitlines():
        val = line.split("-", 2)
        range.add((int(val[0]), int(val[1])))

    count = 0
    for val in sp[1].splitlines():
        if range.check(int(val)):
            count += 1

    print(count)

    print(sum(ub - lb + 1 for lb, ub in range))


if __name__ == "__main__":
    import example

    solve(example.get(5))
