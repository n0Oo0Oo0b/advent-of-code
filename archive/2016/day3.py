import numpy as np


with open('day3.txt') as file:
    data = np.array([[int(j) for j in i.strip().split()] for i in file.readlines()])

t = 0
for i in data:
    s = sorted(i)
    if s[0] + s[1] > s[2]:
        t += 1

print(t)


data2 = []
for row in np.rot90(data):
    data2 += list(np.split(row, len(row)//3))


t = 0
for i in data2:
    s = sorted(i)
    if s[0] + s[1] > s[2]:
        t += 1

print(t)
