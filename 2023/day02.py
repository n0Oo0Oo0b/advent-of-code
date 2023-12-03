from collections import defaultdict

import regex as re
import math
import numpy as np
from itertools import batched, product
from util import get_ints, get_floats, data

blocks = [i.split("\n") for i in data.split("\n\n")]
lines = data.split("\n")
ints = get_ints(data)
floats = get_floats(data)

M = {'red': 12, 'green': 13, 'blue': 14}

def t(x):
    return all(M[i] >= x[i] for i in x)

res1 = 0
res2 = 0
for n, line in enumerate(lines, start=1):
    line = line.split(":")[1]
    parts = line.split(";")
    items = defaultdict(lambda: 0)
    for part in parts:
        for i in re.finditer(r"(\d+) (\w+)", part):
            x, y = i.groups()
            x = int(x)
            items[y] = max(items[y], x)
    if t(items):
        res1 += n
    res2 += math.prod(items.values())

print(res1, res2)
