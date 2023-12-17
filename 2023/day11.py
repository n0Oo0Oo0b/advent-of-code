import numpy as np
from itertools import *
from util import *

res = 0

lines = data.splitlines()
g = np.array([*map(list, lines)]) == '#'
er = set()
for row in range(g.shape[0]):
    if not any(g[row]):
        er.add(row)
ec = set()
for col in range(g.shape[1]):
    if not any(g[:, col]):
        ec.add(col)

G = SparseGrid.from_input(g, lambda x: x if x else None)
for a, b in combinations(G, 2):
    ar, ai = cparts(a)
    br, bi = cparts(b)
    for i in autorange(ar, br):
        if i in er:
            res += 1000000 - 1
    for i in autorange(ai, bi):
        if i in ec:
            res += 1000000 - 1
    res +=abs(( a-b).real)
    res += abs((a-b).imag)
