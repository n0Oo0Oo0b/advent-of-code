import re
import numpy as np


def parse(dat):
    date = dat[1:11]
    guardNum = re.findall(r'#([0-9]{,4})', dat)
    timeStamp = dat[12:17]
    if guardNum:
        mode = int(guardNum[0])
    else:
        mode = 'sleep' if len(dat) == 31 else 'awake'
    return date, timeStamp, mode


def getMin(inp):
    return int(inp[0].split(':')[1])


with open('day4.txt') as file:
    data = [parse(i.strip()) for i in file.readlines()]

data.sort()
data = [i[1:] for i in data]

sleepTime = {}
sleepLocs = {}
for i in data:
    if type(i[1]) == int:
        sleepTime[i[1]] = 0
        sleepLocs[i[1]] = []

i = 0
guard = 0
while i < len(data):
    if type(data[i][1]) == int:
        guard = data[i][1]
        i += 1
    else:
        startTime = getMin(data[i])
        endTime = getMin(data[i + 1])
        sleepTime[guard] += endTime - startTime
        sleepLocs[guard].append((startTime, endTime))
        i += 2

sleepTime = {sleepTime[i]: i for i in sleepTime}
guard = sleepTime[max(sleepTime.keys())]


def getFreq(guardId):
    timeMap = np.zeros(60)
    for start, end in sleepLocs[guardId]:
        timeMap[start:end] += 1
    return list(timeMap)


timeMap = getFreq(guard)
print(timeMap.index(max(timeMap)) * guard)

timeMaps = {i: getFreq(i).index(max(getFreq(i))) for i in sleepLocs.keys()}

maxV = max(timeMaps.values())
print(list(timeMaps.keys())[list(timeMaps.values()).index(maxV)] * maxV)
