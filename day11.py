def solve(data: str):
    g = {sp[0][:-1]: sp[1:] for sp in map(str.split, data.splitlines())}

    yield dfs1("you", g)
    yield dfs2("svr", g), "out of", dfs1("svr", g)


def dfs1(node: str, g: dict[str, list[str]]) -> int:
    mem: dict[str, int] = {}

    def inner(node: str):
        if node == "out":
            return 1
        if node in mem:
            return mem[node]

        mem[node] = sum(inner(nxt) for nxt in g[node])
        return mem[node]

    return inner(node)


def dfs2(node: str, g: dict[str, list[str]]) -> int:
    mem: dict[tuple[str, bool, bool], int] = {}

    def inner(node: str, fft: bool, dac: bool) -> int:
        if node == "out":
            return fft and dac
        if (node, fft, dac) in mem:
            return mem[(node, fft, dac)]

        if node == "fft":
            fft = True
        if node == "dac":
            dac = True

        mem[(node, fft, dac)] = sum(inner(nxt, fft, dac) for nxt in g[node])
        return mem[(node, fft, dac)]

    return inner(node, False, False)


if __name__ == "__main__":
    from example import get

    for res in solve(get(11)):
        print(res)
