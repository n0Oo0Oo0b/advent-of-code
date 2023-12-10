import regex as re
from math import *
import numpy as np
from collections import *
from itertools import *
from util import *
from functools import cmp_to_key

res = 0

blocks = [i.split("\n") for i in data.split("\n\n")]
lines = data.split("\n")
line_ints = [get_ints(line) for line in lines]
ints = get_ints(data)
floats = get_floats(data)

sparse_grid = SparseGrid.from_input(lines, lambda s: s if s != '.' else None)
grid = Grid.from_input(lines)

A = []
B = {}
C = set()

for block in blocks:
    pass

for line in lines:
    x, y = line.split()
    x = ["J23456789TQKA".index(i) for i in x]
    y = int(y)
    a = Counter(x)
    a.setdefault(0, 0)
    amount = a.pop(0)
    print(a)
    try:
        a[max(a, key=a.get)] += amount
    except ValueError:
        a[0] = amount
    A.append(([sorted(a.values(), reverse=True), x], y))
A = sorted(A)

for t, (a, bid) in enumerate(A, start=1):
    print(t, a, bid)
    res += bid * t
    t -= 1
