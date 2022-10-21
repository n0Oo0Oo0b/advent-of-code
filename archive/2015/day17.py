from itertools import combinations

with open('day17.txt') as file:
    data = sorted(int(i) for i in file.read().splitlines())

print(data)

t = 0
a = {}
for x in range(4, 11):
    t2 = 0
    for i in combinations(data, x):
        if sum(i) == 150:
            t += 1
            t2 += 1
    a[x] = t2
print(t)
print(a)
