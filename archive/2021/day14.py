from collections import defaultdict
from time import time

start = time()

# Get input
with open('day14.txt') as file:
    startPolymer, b = tuple(file.read().split('\n\n'))
    d = {(x := line.split(' -> '))[0]: x[1] for line in b.split('\n')}
    data = {i: (i[0] + (di := d[i]), di + i[1]) for i in d}


def elemCountDiff(pairs):
    """
    Function that returns the counts of each element within the pairs given
    """
    elements = defaultdict(int)
    for pair in pairs:
        c1, c2 = tuple(pair)
        # ÷2 is used here because each element will be counted twice (in the pair before and after)
        elements[c1] += (v := pairs[pair]) / 2
        elements[c2] += v / 2
    # The first and last ends of the polymer are only counted once (no additional pair at each end),
    # so the values are rounded up to account for it
    return max((v := [int(i+0.5) for i in elements.values()])) - min(v)


# Dict containing the number of each pair that the polymer contains
pairs = defaultdict(int)
for i in range(len(startPolymer) - 1):
    pairs[startPolymer[i:i + 2]] += 1


# Insertion process
for step in range(40):
    new = defaultdict(int)  # Data of polymer after current insertion is complete
    for i in pairs:
        ra, rb = data[i]
        # Insert values
        new[ra] += (middle := pairs[i])
        new[rb] += middle
    pairs = new
    if step == 9:  # Store value for part 1 (after 10 steps)
        v = elemCountDiff(pairs)
v2 = elemCountDiff(pairs)

end = time()

# Output
print(f'Part 1: {v}\nPart 2: {v2}')
print(f'Time: {(end-start)*1000:.3f}ms')  # Avg. runtime: 1.8ms
