from itertools import combinations
from math import prod

with open('day24.txt') as file:
    data = [int(i) for i in file.read().splitlines()]
data.reverse()

target = sum(data) // 3  # use // 4 for part 2

def validate(x):
    others = set(data) - set(x)
    for count in range(len(others)):
        for d in combinations(others, count):
            if sum(d) == target:
                return True

for count in range(len(data)):
    possible = []
    for c in combinations(data, count):
        if sum(c) == target:
            possible.append(c)
            #if validate(c):  # apparently you don't need this bit :/
            #    possible.append(c)
    if possible:
        break

print(possible)
print(min(map(prod, possible)))
