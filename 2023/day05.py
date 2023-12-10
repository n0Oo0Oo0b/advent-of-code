import regex as re
import math
import numpy as np
from collections import *
from itertools import *
from util import *

res = 0

blocks = [i.split("\n") for i in data.split("\n\n")]
lines = data.split("\n")
line_ints = [get_ints(line) for line in lines]
ints = get_ints(data)
floats = get_floats(data)


a, *b = blocks
data = {}
# v = set(get_ints(a[0]))
# v = {1}
v = MultiRange([])
for x, y in batched(get_ints(a[0]), 2):
    v |= MultiRange([x, x + y])

for (_, *y) in b:
    *y, = map(get_ints, y)
    # for dest, source, size in y:
    #     S = range(source, source + size)
    #     D = range(dest, dest + size)
    #     for i in v:
    #         if i not in S:
    #             continue
    #         v2.add(D[S.index(i)])
    #         R.remove(i)
    mapping = {}
    R = v.copy()

    def find(x):
        for k, v in mapping.items():
            if x in k:
                return v[k.index(x)]
        return x
    r = MultiRange([])
    for dest, source, size in y:
        S = range(source, source+size)
        D = range(dest, dest+size)
        mapping[S] = D
        for s, e in batched((MultiRange(S) & R).values, 2):
            if s == e: continue
            R -= MultiRange([s, e])
            r |= MultiRange([find(s), find(e - 1) + 1])
    r |= R
    v = r

print(res := v.values[0])
# print(min(v))
# res = min(v)
