import re

with open('day9.txt') as file:
    data = file.read().split('\n')

vMap = {}
for i in data:
    result = re.findall(r'(.*?) to (.*?) = (.*)', i)[0]
    vMap.setdefault(result[0], {})[result[1]] = int(result[2])
    vMap.setdefault(result[1], {})[result[0]] = int(result[2])
for i in vMap:
    vMap[i][i] = 0
print(vMap)


def getMinDist(cities: list, prevCity=None):
    if not cities:
        return 0
    elif len(cities) == 1:
        return vMap[prevCity][cities[0]]
    minV = 65535
    for nextCity in cities:
        c = cities.copy()
        if prevCity is None:
            prevCity = nextCity
        c.remove(nextCity)
        total = vMap[prevCity][nextCity] + getMinDist(c, nextCity)
        if total < minV:
            minV = total
    return minV


def getMaxDist(cities: list, prevCity=None):
    if len(cities) == 1:
        return vMap[prevCity][cities[0]]
    
    maxV = 0
    for nextCity in cities:
        c = cities.copy()
        if prevCity is None:
            p = nextCity
        else:
            p = prevCity
        c.remove(nextCity)
        total = vMap[p][nextCity] + getMaxDist(c, nextCity)
        if total > maxV:
            maxV = total
    return maxV


print(getMinDist(list(vMap.keys())))
print(getMaxDist(list(vMap.keys())))
