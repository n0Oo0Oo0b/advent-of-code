from math import prod, pi
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
    target_sum = int(inp) / 10
    part1 = int(target_sum ** (2/3) / (6/pi**2))  # https://oeis.org/A000203
    while _sum_factors(part1) < target_sum:  # Brute force
        part1 += 1
    # Part 2
    part2 = 1
    target_sum = int(inp) / 11
    while _sum_factors(part2, div_limit=50) < target_sum:  # Also brute force
        part2 += 1
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day20(data)))
