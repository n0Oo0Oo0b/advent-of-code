import re
from time import time
from collections import defaultdict
from math import prod


with open('inputs/day22.txt') as file:
    data = [(tuple(map(int, re.findall(r'-?\d+', i))), int(i[1] == 'n')) for i in file.read().splitlines()]


start = time()  # Timing this one as well :)

allAreas = defaultdict(int)
for region, sign in data:
    for region2, sign2 in tuple(allAreas.items()):
        if not sign2:  # Area has already been cancelled out (sign == 0)
            continue
        
        # Find overlapped region (if any)
        overlapRegion = ()
        for ai in range(0, 6, 2):  # Check each axis for overlap
            overlapStart, overlapEnd = max(region[ai], region2[ai]), min(region[ai + 1], region2[ai + 1])
            if overlapStart > overlapEnd:  # No overlap on axis
                break
            overlapRegion += (overlapStart, overlapEnd)
        else:  # There is overlap on all 3 axis, cancel out the overlapped region
            allAreas[overlapRegion] -= sign2
    
    allAreas[region] += sign  # Turn the region itself on/off

t = t2 = 0
for region, sign in allAreas.items():  # Add up the numbers
    t2 += (count := sign * prod((region[i+1] - region[i] + 1) for i in range(0, 6, 2)))
    if min(region) >= -50 and max(region) <= 50:
        t += count

end = time()


# Output
print(f'Part 1: {t}\nPart 2: {t2}')
print(f'Time taken: {(end-start)*1000:.1f}ms')  # Avg. 330ms
