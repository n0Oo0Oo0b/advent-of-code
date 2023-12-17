import numpy as np
from util import *

res = 0
blocks = [i.split("\n") for i in data.split("\n\n")]


def f(x):
    for i in x:
        print("".join('.#'[n] for n in i))


for block in blocks:
    g: np.ndarray = np.array([*map(list, block)]) == '#'
    for x in range(g.shape[0]):
        a = g[:x][::-1]
        b = g[x:]
        a = a[:len(b)]
        b = b[:len(a)]
        f(a[::-1])
        print("-"*10)
        f(b)
        if (a != b).sum() == 1:
            res += x * 100
            print(x*100)
        print()
    for x in range(g.shape[1]):
        a = g.T[:x][::-1]
        b = g.T[x:]
        a = a[:len(b)]
        b = b[:len(a)]
        f(a[::-1])
        print("-"*10)
        f(b)
        if (a != b).sum() == 1:
            res += x
            print(x)
        print()
