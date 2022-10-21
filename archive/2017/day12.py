def parseLine(s):
    i = s.strip().split(' <-> ')
    i[0] = int(i[0])
    i[1] = list(map(int, i[1].split(', ')))
    return i


with open('day12.txt') as file:
    data = [parseLine(i) for i in file.readlines()]
    data = {i[0]:set(i[1]) for i in data}


def getSystem(program):
    global data
    pool = {program}
    prevLen = 0
    while prevLen != len(pool):
        prevLen = len(pool)
        for i in pool:
            pool = pool.union(data[i])
    return pool


print(len(getSystem(0)))


pool = set(range(2000))
t = 0
for i in range(2000):
    if i in pool:
        pool.difference_update(getSystem(i))
        t += 1
print(t)
