from collections import Counter
from itertools import permutations

with open('day2.txt') as file:
    data = [i.strip() for i in file.readlines()]

num2 = 0
num3 = 0
for boxName in data:
    c = Counter(list(boxName))
    if 2 in c.values():
        num2 += 1
    if 3 in c.values():
        num3 += 1

print(num2*num3)


def getDiff(id1, id2):
    count = 0
    for char1, char2 in zip(id1, id2):
        if char1 == char2:
            count += 1
    return len(id1)-count


closeIDs = ('', '')
minDiff = 1000
for id1, id2 in permutations(data, r=2):
    diff = getDiff(id1, id2)
    if diff < minDiff:
        minDiff = diff
        closeIDs = (id1, id2)

r = ''
for char1, char2 in zip(*closeIDs):
    if char1 == char2:
        r += char1

print(closeIDs)
print(r)
