import numpy as np
from collections import defaultdict

data = open(0).read()

grid = np.array([[i == '#' for i in line] for line in data.splitlines()], bool)

new_elves = set(int(j) + 1j * int(i) for i, j in zip(*np.nonzero(grid)))
elves = set()

adj = {
    'NW': -1 - 1j,
    'N': - 1j,
    'NE': + 1 - 1j,
    'W': - 1,
    'E': + 1,
    'SW': + (-1 + 1j),
    'S': + 1j,
    'SE': + (1 + 1j)
}


propose = [
    ['E', {'NE', 'E', 'SE'}],
    ['N', {'NW', 'N', 'NE'}],
    ['S', {'SW', 'S', 'SE'}],
    ['W', {'NW', 'W', 'SW'}],

]

n = 0
while elves ^ new_elves:
    elves = new_elves
    propose.append(propose.pop(0))
    proposals = {}
    new_elves = set()
    for elf in elves:
        adjacent = frozenset(k for k, v in adj.items() if elf+v in elves)
        if len(adjacent) == 0:
            new_elves.add(elf)
            continue
        for k, v in propose:
            if not (v & adjacent):
                break
        else:
            new_elves.add(elf)
            continue
        e = elf + adj[k]
        proposals[e] = *proposals.get(e, ()), elf
    for loc, e in proposals.items():
        if len(e) == 1:
            new_elves.add(loc)
        else:
            new_elves |= set(e)
    n += 1
    if n == 10:
        min_real = float('inf')
        max_real = 0
        min_imag = float('inf')
        max_imag = 0

        for elf in new_elves:
            r, i = int(elf.real), int(elf.imag)
            min_real = min(min_real, r)
            max_real = max(max_real, r)
            min_imag = min(min_imag, i)
            max_imag = max(max_imag, i)

        print((max_imag - min_imag + 1) * (max_real - min_imag + 1) - len(elves))
print(n)
