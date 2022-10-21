import numpy as np
from day10 import *


data = 'stpzcrnm'
fullOutput = ''
for i in range(128):
    hashOutput = fullHash(f'{data}-{i}')
    for j in hashOutput:
        output = bin(int(j,16))[2:]
        while len(output) < 4:
            output = '0' + output
        fullOutput += output


print(fullOutput.count('1'))


l = list(map(int, fullOutput))
p = set()
disc = np.array(l)
disc = disc.reshape(128,128)
disc2 = np.zeros(shape=(130,130),dtype=int)
for c1 in range(128):
    for c2 in range(128):
        disc2[c1+1, c2+1] = disc[c1, c2]
        if disc[c1,c2] == 1:
            p.add(f'[{c1+1}, {c2+1}]')
directions = [
    np.array([0,1]),
    np.array([0,-1]),
    np.array([1,0]),
    np.array([-1,0])
]


def getRegion(startX, startY):
    global disc2
    if disc2[startX, startY] == 0:
        return []
    pool = [[startX, startY]]
    length = 0
    while len(pool) != length:
        length = len(pool)
        for location in pool:
            for direction in directions:
                l = list(np.array(location) + direction)
                if l not in pool and disc2[l[0],l[1]] == 1:
                    pool.append(l)
    return set(map(str,pool))


t = 0
while p:
    t += 1
    p.difference_update(getRegion(*eval(list(p)[0])))
print(t)
