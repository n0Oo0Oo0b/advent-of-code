from math import prod
from sympy import factorint


def _sum_factors(n, div_limit=None):
    if div_limit:
        t = 0
        for i in range(1, div_limit+1):
            d, m = divmod(n, i)
            if m == 0:
                t += d
        return t
    else:
        return prod(((base**(exp+1)-1) / (base-1)) for base, exp in factorint(n).items())


def day20(inp):  # Can 100% be improved
    # Part 1
    part1 = 1
    target_factor = int(inp) / 10
    while _sum_factors(part1) < target_factor:  # Brute force
        part1 += 1
    # Part 2
    part2 = 1
    target_factor = int(inp) / 11
    while _sum_factors(part2, div_limit=50) < target_factor:  # Also brute force
        part2 += 1
    return part1, part2


if __name__ == '__main__':
    with open('inputs/day20.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day20(data)))
