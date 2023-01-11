from itertools import combinations
import math


def find_arrangement(data, compartments):
    target = sum(data) // compartments
    for n in range(1, len(data)):
        possible = []
        if sum(data[-n:]) < target:
            continue
        for c in combinations(data, n):
            if sum(c) == target:
                possible.append(c)
        if possible:
            # Apparently you don't have to check that the combination
            # can divide the remaining presents correctly
            return min(map(math.prod, possible))


def day24(inp):
    data = [int(i) for i in inp.splitlines()]
    part1 = find_arrangement(data, 3)
    part2 = find_arrangement(data, 4)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day24(data)))
