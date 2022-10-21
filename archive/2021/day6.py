with open('day6.txt') as file:
    data = [int(i) for i in file.read().split(',')]

#  Adapted from Eddie's solution
fish = [data.count(i) for i in range(9)]

for i in range(256):
    newFish = fish.pop(0)
    fish.append(newFish)
    fish[6] += newFish
    if i == 79:
        part1 = sum(fish)
print(f'Part 1: {part1}\nPart 2: {sum(fish)}')

"""
How does this work?

basically, fish is a first in, first out stack.
At any given point, fish[n] will give the number of fish that will reproduce in n days.
The list is initialized with the input data (line 5), and for each step:
  - the first index is popped from fish (assigned to newFish) as the number of fish that will reproduce on that step
  - the newborn fish is appended (to index 8) where it will wait 8 days
  - the preexisting fish will be added to fish[6] to wait 6 days before reproducing again
"""