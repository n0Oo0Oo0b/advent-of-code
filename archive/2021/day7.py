with open('day7.txt') as file:
    data = [int(i) for i in file.read().split(',')]


def fuelNeeded(n):
    return n*(n+1) // 2


scores, scores2 = [], []
for target in range(min(data), max(data)):
    scores.append(sum(map(lambda x: abs(x-target), data)))
    scores2.append(sum(map(lambda x: fuelNeeded(abs(x-target)), data)))

print(f'Part 1: {min(scores)}\nPart 2: {min(scores2)}')
