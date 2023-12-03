import regex as re
import math
import numpy as np
from itertools import batched, product
from util import get_ints, get_floats, data

blocks = [i.split("\n") for i in data.split("\n\n")]
lines = data.split("\n")
ints = get_ints(data)
floats = get_floats(data)


nums = list(map(get_ints, lines))

res = 0

for i in nums:
    res += int(str(i[0]) + str(i[-1]))
