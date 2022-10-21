from collections import defaultdict, Counter
from functools import lru_cache


def parse_input(i):
    out = []
    for line in i:
        out.append(tuple(line.strip().split()))
    return tuple(out)


BLOCK_SIZE = 18


@lru_cache
def evaluate(block, digit, z0):
    """Evaluates a single block with a given digit and z0, determining the z0 afterwards"""
    x = 0 if ((z0 % 26) + int(block[5][2])) == digit else 1
    z = z0 // int(block[4][2])
    z1 = z * ((25 * x) + 1)
    z2 = z1 + (x * (digit + int(block[15][2])))
    return z2


@lru_cache
def getModelNumber(index, z0, rb, values):
    """Recursively determines the smallest sequence of digits necessary to run the rest of the program with z = z0 to start, and ending with z = 0"""
    if index + BLOCK_SIZE >= len(program):
        for i in values:
            if evaluate(program[index:], i, z0) == 0:
                return i
        return 0
    
    if program[index + 4][2] == "1":
        # inc block
        rng = values
    else:
        # dec block
        x = z0 % 26
        x += int(program[index + 5][2])
        if x <= 0 or x > 9:
            return 0
        rng = range(x, x + 1)
    
    for i in rng:
        res = getModelNumber((end := index + BLOCK_SIZE), evaluate(program[index:end], i, z0), rb - 1, values)
        if res > 0:
            return (i * (10 ** rb)) + res
    return 0


with open('inputs/day24.txt') as f:
    program = parse_input(f.readlines())
print(getModelNumber(0, 0, 13, range(9, 0, -1)))
print(getModelNumber(0, 0, 13, range(1, 10)))
