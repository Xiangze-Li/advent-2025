from itertools import chain, combinations

import pulp


def solve(data: str):
    light_count = 0
    joltage_count = 0
    for fields in map(str.split, data.splitlines()):
        light: tuple[int, ...] = tuple(1 if c == "#" else 0 for c in fields[0][1:-1])
        light_v: int = sum((1 << i) for i, v in enumerate(light) if v)
        buttons: list[tuple[int, ...]] = [
            tuple(map(int, b[1:-1].split(","))) for b in fields[1:-1]
        ]
        joltage: tuple[int, ...] = tuple(map(int, fields[-1][1:-1].split(",")))

        for r in range(len(buttons)):
            found = False
            for combo in combinations(buttons, r + 1):
                combined = 0
                for b in chain(*combo):
                    combined ^= 1 << b
                if combined == light_v:
                    light_count += r + 1
                    found = True
                    break
            if found:
                break

        joltage_count += lp_solve(buttons, joltage)

    yield light_count
    yield joltage_count


def lp_solve(buttons: list[tuple[int, ...]], target: tuple[int, ...]) -> int:
    vars: list[pulp.LpVariable] = []
    for i in range(len(buttons)):
        vars.append(pulp.LpVariable(f"b{i}", lowBound=0, cat=(pulp.LpInteger)))

    problem = pulp.LpProblem(sense=pulp.LpMinimize)
    for i, j in enumerate(target):
        equation = pulp.LpAffineExpression()
        for idx_b, b in enumerate(buttons):
            if i in b:
                equation += vars[idx_b]
        problem += equation == j
    problem += pulp.lpSum(vars)

    problem.solve(pulp.PULP_CBC_CMD(msg=False))
    return sum(int(v.value()) for v in vars)  # type: ignore


if __name__ == "__main__":
    from example import get

    for res in solve(get(10)):
        print(res)
