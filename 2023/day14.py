import numpy as np
from itertools import *
from util import *

res = 0

lines = data.split("\n")

# output = [["#"]*len(lines[0])] + [list(l.replace("O", ".")) for l in lines]
# print(output)
# for y, line in enumerate(lines, start=1):
#     for i, c in enumerate(line):
#         if c != "O": continue
#         ny = y
#         while output[ny-1][i] == '.':
#             print(y, i)
#             ny -= 1
#         output[ny][i] = "O"
#         res += len(lines) - ny +1
#         for line in output:
#             print("".join(line))
#     print()

size = len(lines)
arr = np.array([list(l) for l in lines])
new: np.ndarray = (arr == 'O').astype(int) - (arr == '#')
new = np.pad(new, 1, constant_values=-1)
rocks = set(SparseGrid.from_input(new, lambda x: x if x==1 else None).keys())
ground = set(SparseGrid.from_input(new, lambda x: x if x==-1 else None).keys())
# ground: np.ndarray = new == '#'


def tilt(rocks, direction):
    res = set()
    for i in sorted(rocks, key=lambda x: -(x / direction).real):
        while i+direction not in ground and i+direction not in res:
            i += direction
        res.add(i)
    return res


steps = {}
for R in count():
    for i in range(4):
        rocks = tilt(rocks, -1 * 1j**i)
    fs = frozenset(rocks)
    if fs in steps:
        print(steps[fs], R)
        a, b = steps[fs], R
        break
    steps[fs] = R
    t = 0
    for x in range(102):
        for y in range(102):
            if complex(x, y) in rocks:
                t += size - x + 1
    print(R, t)

N = 1_000_000_000
N -= a
b -= a
c = N % b - 1

for i in range(4 * c):
    rocks = tilt(rocks, -1 * 1j ** i)

for x in range(102):
    for y in range(102):
        if complex(x, y) in rocks:
            res += size - x + 1
#             print(size - x + 1, end='')
#         elif complex(x, y) in ground:
#             print("#", end='')
#         else:
#             print(".", end='')
#     print()
# print()
