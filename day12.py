def solve(data: str) -> None:
    blocks = data.split("\n\n")
    patterns: list[list[bool]] = []
    for block in blocks[:-1]:
        patterns.append([c == "#" for c in block.replace("\n", "")[2:]])

    total = 0
    for question in blocks[-1].splitlines():
        size, target = question.split(": ")
        x, y = map(int, size.split("x"))
        targets = list(map(int, target.split()))

        total += x * y > sum(
            sum(pattern) * count for pattern, count in zip(patterns, targets)
        )

    print(total)
    print("Happy holiday!")


if __name__ == "__main__":
    import example

    solve(example.get(12))
