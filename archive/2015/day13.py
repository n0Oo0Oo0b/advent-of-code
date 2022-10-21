from collections import defaultdict
from itertools import permutations
import re

with open('day13.txt') as file:
    data = file.read().split('\n')

happiness = defaultdict(int)
people = set()
for line in data:
    match = re.match(r'(\w).*(gain|lose) (\d+).*\s(\w)\w*\.$', line)
    a, sign, v, b = match.groups()
    boost = int(v) * (1 if sign == 'gain' else -1)
    happiness[frozenset((a, b))] += boost
    people.add(a)

# people.add("Y")

count = len(people)

max_happiness = 0
for arrangement in permutations(people):
    t = 0
    for i in range(count):
        t += happiness[frozenset((arrangement[i], arrangement[i-1]))]
    max_happiness = max(max_happiness, t)

# Uncomment L17 for part 1
print(max_happiness)
