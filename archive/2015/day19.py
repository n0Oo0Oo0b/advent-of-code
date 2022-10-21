from collections import defaultdict
from functools import reduce

def flatten(x):
    if not isinstance(x, list):
        return [x]
    return reduce(list.__add__, (flatten(i) for i in x))

def split_chemicals(inp):
    chemicals = []
    for i in inp:
        if i.isupper():
            chemicals.append(i)
        else:
            chemicals[-1] += i
    return chemicals

with open('day19.txt') as file:
    raw_conversions, raw_molecule = file.read().split('\n\n')

conversions = defaultdict(list)
for i in raw_conversions.splitlines():
    a, b = i.split(' => ')
    conversions[a].append(split_chemicals(b))

molecule = split_chemicals(raw_molecule)

possible = set()
for i, element in enumerate(molecule):
    for result in conversions[element]:
        m = molecule.copy()
        m[i] = result
        possible.add(tuple(flatten(m)))

print(len(possible))
