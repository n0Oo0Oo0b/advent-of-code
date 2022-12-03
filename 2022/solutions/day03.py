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


def speedcode_solution(inp):
    lines = inp.splitlines()  # originally aocd.lines

    def priority(a):
        if a.islower():
            return ord(a) - ord('a') + 1
        else:
            return ord(a) - ord('A') + 27

    t = 0
    for line in lines:
        s = len(line) // 2
        a = ''.join(set(line[:s]) & set(line[s:]))
        t += priority(a)
    part1 = t

    t = 0
    for x in range(0, len(lines), 3):
        d = lines[x:x + 3]
        t += priority(''.join(set(d[0]) & set(d[1]) & set(d[2])))
    part2 = t

    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
