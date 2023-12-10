import regex as re
import math
import numpy as np
from collections import *
from itertools import *
from util import *

res = 1

blocks = [i.split("\n") for i in data.split("\n\n")]
lines = data.split("\n")
line_ints = [get_ints(line) for line in lines]
ints = get_ints(data)
floats = get_floats(data)

*a, = zip(*map(get_ints, lines))
print(a)

for t, d in a:
    m = 0
    for x in range(t):
        if x*(t-x) > d:
            m += 1
    res *= m
