from collections import Counter


def solution(inp):
    lines = inp.splitlines()
    part1 = ''
    part2 = ''
    for letters in zip(*lines):
        frequencies = Counter(letters).most_common()
        part1 += frequencies[0][0]
        part2 += frequencies[-1][0]
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
