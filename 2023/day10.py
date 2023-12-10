import regex as re
from math import *
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

sparse_grid = SparseGrid.from_input(lines, lambda s: s if s != '.' else None)
grid = Grid.from_input(lines)


A = []
B = {}
C = set()

