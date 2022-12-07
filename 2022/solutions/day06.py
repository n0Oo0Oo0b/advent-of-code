def solve(inp):
    part1 = None
    part2 = None
    for i in range(len(inp) - 14):
        if part1 is None and len(set(inp[i:i + 4])) == 4:
            part1 = i + 4
        if len(set(inp[i:i + 14])) == 14:
            part2 = i + 14
            break
    return part1, part2


def speedcode_solution(inp):
    for i in range(len(inp)):
        if len(set(inp[i:i + 4])) == 4:
            break
    part1 = i + 4
    for i in range(len(inp)):
        if len(set(inp[i:i + 14])) == 14:
            break
    part2 = i + 14

    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
