def validate_triangle(side_lengths):
    a, b, c = sorted(side_lengths)
    return a + b > c


def solution(inp):
    inp = [[int(i) for i in line.split()] for line in inp.splitlines()]
    # Part 1
    part1 = 0
    for triangle in inp:
        part1 += validate_triangle(triangle)
    # Part 2
    part2 = 0
    for group in zip(*[iter(inp)] * 3):  # get chunks of 3 rows
        for triangle in zip(*group):
            part2 += validate_triangle(triangle)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
