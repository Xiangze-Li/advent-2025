def solve(data: str):
    lines = data.splitlines()
    N = len(lines[0])

    start = lines[0].find("S")

    splitters: list[list[int]] = [
        [i for i, c in enumerate(line) if c == "^"]
        for line in lines[1:]
    ]

    count = 0
    beams: list[int] = [1 if i == start else 0 for i in range(N)]
    for splitter in splitters:
        for s in splitter:
            if beams[s] > 0:
                beams[s - 1] += beams[s]
                beams[s + 1] += beams[s]
                beams[s] = 0
                count += 1

    yield count
    yield sum(beams)


if __name__ == "__main__":
    from example import get

    for res in solve(get(7)):
        print(res)
