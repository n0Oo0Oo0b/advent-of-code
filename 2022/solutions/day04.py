import re


def solve(inp):
    part1 = 0
    part2_delta = 0
    for line in inp.splitlines():
        a1, a2, b1, b2 = map(int, re.findall(r'\d+', line))
        if b1 < a1:  # reorder lower and higher range
            (a1, a2), (b1, b2) = (b1, b2), (a1, a2)
        if a2 >= b2:
            part1 += 1
        elif a2 >= b1:
            part2_delta += 1
    return part1, part1 + part2_delta


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
