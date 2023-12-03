from operator import attrgetter

import regex as re
import math
import numpy as np
from itertools import batched, product
from util import *

blocks = [i.split("\n") for i in data.split("\n\n")]
lines = data.split("\n")
ints = get_ints(data)
floats = get_floats(data)


g = {}
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == '.': continue
        g[complex(x, y)] = int(c) if c.isdigit() else -1
res = 0
keep = set()
for k, v in g.items():
    if v != -1:
        continue
    nums = set()
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            n = k + complex(dy, dx)
            if g.get(n, -1) >= 0:
                nums.add(n)
    fullnums = set()
    for p in nums:
        n = set()
        for d in range(3):
            if g.get(p + d, -1) >= 0:
                keep.add(p+d)
                n.add(p+d)
            else:
                break
        for d in range(3):
            if g.get(p - d, -1) >= 0:
                keep.add(p-d)
                n.add(p-d)
            else:
                break
        fullnums.add(int(''.join(map(str, map(g.get, sorted(n, key=attrgetter('real')))))))
    # part 2
    # if len(fullnums) == 2:
    #     res += math.prod(fullnums)

r = [[' ']*150 for _ in range(150)]
for k, v in g.items():
    if k in keep:
        r[int(k.imag)][int(k.real)] = str(v)
    if v == -1: r[int(k.imag)][int(k.real)] = "#"

# part 1
for i in r: res += sum(get_ints(''.join(i)))
