from collections import deque
from time import time

start = time()

puzzle = 376
spinlock = deque([0])

for i in range(1, 50000001):
    spinlock.rotate(-puzzle)
    spinlock.append(i)

print(spinlock[spinlock.index(0) + 1])
print(time()-start)
