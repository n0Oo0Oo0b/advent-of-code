data = [ int(i) for i in '130254-678275'.split('-') ]

import re
from itertools import combinations_with_replacement as combinations

# Part 1
def checkForDouble(num):
    return len(re.findall(r'11|22|33|44|55|66|77|88|99|00',str(num)))

total = 0
for i in combinations('0123456789',6):
    i = int(''.join(i))
    if i>data[0] and i<data[1] and checkForDouble(i):
        total += 1
print(total)

# Part 2
def checkForDouble(num):
    num = str(num)
    for i in range(10):
        if len(re.findall(str(i),num)) == 2:
            return True
    return False
total = 0
for i in combinations('0123456789',6):
    i = int(''.join(i))
    if i>data[0] and i<data[1] and checkForDouble(i):
        total += 1
print(total)
