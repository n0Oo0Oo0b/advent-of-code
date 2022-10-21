import numpy as np
from itertools import permutations


def parse(inp):
    return np.array([line.split(',') for line in inp.splitlines()[1:]], int)


with open('inputs/day19.txt') as file:
    data = [parse(i) for i in file.read().split('\n\n')]


def getDist(scanners):
    all_dists = []
    for scan in scanners:
        dists = []
        for point in scan:
            dists.append(np.sum(np.abs(scan - point), axis=1))
        all_dists.append(dists)
    return all_dists


def findOverlap(s1, s2):
    for i, d0 in enumerate(dists[s1]):
        for j, d1 in enumerate(dists[s2]):
            if len(overlaps := set(d0) & set(d1)) >= 12:
                return i, j, overlaps


def findPositions(s0, s1, p0, p1, overlaps):
    for d in overlaps:
        if d == 0:
            continue
        q0 = np.where(dists[s0][p0] == d)[0][0]
        q1 = np.where(dists[s1][p1] == d)[0][0]
        
        diff0 = data[s0][p0] - data[s0][q0]
        diff1 = data[s1][p1] - data[s1][q1]
        
        if len(set(np.abs(diff0))) < 3:
            continue
        
        order = []
        sign = []
        
        for i in range(3):
            idx = np.where(np.abs(diff1) == abs(diff0[i]))[0][0]
            order.append(idx)
            sign.append(diff1[idx] // diff0[i])
        
        new_orient = data[s1][:, order] * np.array(sign)
        
        break
    
    scanner_pos = data[s0][p0] - new_orient[p1]
    new_coords = new_orient + scanner_pos
    
    return scanner_pos, new_coords


def findScanners():
    found = {0}
    count = 1
    
    while count < len(data):
        s0 = found.pop()
        
        for i in range(len(data)):
            if len(scannerPos[i]):
                continue
            overlaps = findOverlap(s0, i)
            if not overlaps:
                continue
            
            scannerPos[i], data[i] = findPositions(s0, i, *overlaps)
            found.add(i)
            count += 1


def findBeacons():
    return set(tuple(pos) for i in data for pos in i)


dists = getDist(data)

scannerPos = [np.array(()) for _ in data]
scannerPos[0] = np.array([0, 0, 0])

findScanners()
beacons = findBeacons()

m = 0
for s1, s2 in permutations(scannerPos, r=2):
    m = max(m, sum(abs(s1 - s2)))

print(f'Part 1: {len(beacons)}\nPart 2: {m}')
