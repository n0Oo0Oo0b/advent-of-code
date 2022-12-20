import numpy as np


def speedcode_solution(inp):
    def v2(x, y):
        return np.array((x, y))

    lengths = [v2(0, 0) for _ in range(10)]
    head = lengths[0]
    second = lengths[1]
    tail = lengths[-1]
    visited = set()
    visited2 = set()
    for line in inp.splitlines():
        d, a = line.split()
        a = int(a)
        if d == 'D':
            d = v2(0, 1)
        elif d == 'U':
            d = v2(0, -1)
        elif d == 'L':
            d = v2(-1, 0)
        else:
            d = v2(1, 0)
        for _ in range(a):
            head += d
            for i in range(9):
                front, back = lengths[i], lengths[i + 1]
                delta = front - back
                if abs(delta).max() > 1:
                    back += delta.clip(-1, 1)
            visited.add(tuple(second))
            visited2.add(tuple(tail))
    return len(visited), len(visited2)


if __name__ == '__main__':
    from aocd import data
    part1, part2 = speedcode_solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
