from functools import lru_cache
from time import time

# Puzzle input
with open('inputs/day21.txt') as file:
    data = [int(i.rsplit(maxsplit=1)[1])-1 for i in file.read().splitlines()]

# Yes, I am timing this
start = time()


locations = data.copy()
scores = [0, 0]
diceNum = rollCount = 0
player = False
while max(scores) < 1000:
    for _ in range(3):  # Roll dice
        diceNum = diceNum + 1 if diceNum < 100 else 1
        locations[player] = (locations[player] + diceNum) % 10
    
    scores[player] += locations[player] + 1  # Bool works as indices (False=0, True=1)
    rollCount += 3
    player = not player

part1 = scores[player] * rollCount


# Frequency of outcomes from rolling dice 3 times
counts = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@lru_cache(maxsize=None)  # Runtime improvement 30s -> 100ms
def simulateDirac(locations, scores, turn):
    x = y = 0  # Count of number of wins for each player
    
    for diceTotal, count in zip(counts.keys(), counts.values()):  # Iterate all possible outcomes of dice
        l, s = list(locations), list(scores)
        
        # Add score
        l[turn] = (l[turn] + diceTotal) % 10
        s[turn] += l[turn] + 1

        if s[turn] >= 21:  # Player immediately wins
            if turn:
                y += count
            else:
                x += count
        else:  # No winner, check recursively for following turns
            a, b = simulateDirac(tuple(l), tuple(s), not turn)
            x += a * count
            y += b * count
    
    return x, y


part2 = max(simulateDirac(tuple(data), (0, 0), False))

# Output
end = time()
print(f'Part 1: {part1}\nPart 2: {part2}')
print(f'Time: {(end-start)*1000:.3f}ms')  # Avg. 90ms runtime
