
from itertools import pairwise
from util import *

res = 0

lines = data.splitlines()


def diff(nums):
    return [(b - a) for a, b in pairwise(nums)]


for ints in map(get_ints, lines):
    layers = [ints]
    while any(layers[-1]):
        layers.append(diff(layers[-1]))
    n = 0
    for layer in layers: print(layer)
    layers.pop()
    for i in layers[::-1]:
        n = i[0] - n
    res += n

print(res)
