def solve(data: str):
    joltage_1 = 0
    joltage_2 = 0

    for line in data.splitlines():
        joltage_1 += solve_line(line, 2)
        joltage_2 += solve_line(line, 12)

    yield joltage_1
    yield joltage_2


def solve_line(line: str, count: int) -> int:
    digits = [int(c) for c in line] + [0]
    max_digits: list[int] = [0] * (count + 1)
    max_digits_idx: list[int] = [-1] * (count + 1)

    for n in range(1, count + 1):
        prev_idx = max_digits_idx[n - 1]
        for i, d in enumerate(
            digits[prev_idx + 1 : -(count - n + 1)], start=prev_idx + 1
        ):
            if d > max_digits[n]:
                max_digits[n] = d
                max_digits_idx[n] = i

    result = 0
    for d in max_digits[1:]:
        result = result * 10 + d
    return result


if __name__ == "__main__":
    from example import get

    for res in solve(get(3)):
        print(res)
