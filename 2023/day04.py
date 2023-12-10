from collections import Counter

import regex as re
import math
import numpy as np
from itertools import *
from util import *

blocks = [i.split("\n") for i in data.split("\n\n")]
lines = data.split("\n")
ints = get_ints(data)
floats = get_floats(data)
p1 = 0

c = Counter()
for game, line in enumerate(lines, start=1):
    mult = c[game] + 1
    a, b = line.split("|")
    a = get_ints(a)[1:]
    b = get_ints(b)
    m = len(set(a) & set(b))
    if not len(set(a) & set(b)): continue
    n = 2**(m - 1) * mult
    p1 += n
    # for i in range(game+1, game+m+1): c[i] += mult
    c += {i: mult for i in range(game+1, game+m+1)}
p2 = (sum(c.values()) + game)
print(p1, p2)
