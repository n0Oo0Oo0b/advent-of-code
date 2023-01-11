from string import ascii_letters
from more_itertools import grouper


def solve(inp):
    lines = inp.splitlines()

    def priority(char):
        return ascii_letters.find(char) + 1

    part1 = 0
    for line in lines:
        partition = len(line) // 2
        a, b = line[:partition], line[partition:]
        common_char, = set(a) & set(b)
        part1 += priority(common_char)

    part2 = 0
    for a, b, c in grouper(lines, 3):
        common_char, = set(a) & set(b) & set(c)
        part2 += priority(common_char)

    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
