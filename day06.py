from math import prod


def solve(data: str):
    lines = data.splitlines()
    yield part1(lines)
    yield part2(lines)


def part1(lines: list[str]):
    nums = [line.split() for line in lines]
    N_OP = len(nums) - 1
    N_COL = len(nums[0])

    total = 0
    for col in range(N_COL):
        op = nums[N_OP][col]
        if op == "+":
            total += sum(int(nums[row][col]) for row in range(N_OP))
        else:
            total += prod(int(nums[row][col]) for row in range(N_OP))

    return total


def part2(lines: list[str]):
    col = max(len(line) for line in lines) - 1
    for i in range(len(lines)):
        lines[i] = lines[i].ljust(col + 1)

    line_op = lines[-1]
    line_nums = lines[:-1]

    total = 0
    while col >= 0:
        oprands = []
        while True:
            op = 0
            for row in range(len(line_nums)):
                if lines[row][col] != " ":
                    op *= 10
                    op += int(lines[row][col])
            oprands.append(op)
            op_code = line_op[col]
            col -= 1
            if op_code == "+":
                total += sum(oprands)
                break
            elif op_code == "*":
                total += prod(oprands)
                break
        col -= 1

    return total


if __name__ == "__main__":
    from example import get

    for res in solve(get(6)):
        print(res)
