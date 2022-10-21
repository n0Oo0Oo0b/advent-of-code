# Python 3.10 (pattern matching @36-58)
from itertools import permutations  # Built-in library, don't judge


def parse(line):
    before, after = tuple(line.split(' | '))
    return before.split(), after.split()


# Import puzzle input
with open('day8.txt') as file:
    data = [parse(i) for i in file.read().split('\n')]


t, totalOutput = 0, 0
for signals, output in data:
    # Find special sections (sig1 -> cf, sig4 -> bcdf, diff -> bd)
    for signal in signals:
        if len(signal) == 2:
            sig1 = set(signal)
        elif len(signal) == 4:
            sig4 = set(signal)
    diff = sig4.difference(sig1)
    
    trueOutput = ''
    for signal in output:
        signal = set(signal)
        
        # Counter for part 1 (1->2, 4->4, 7->3, 8->7 segments)
        if len(signal) in (2, 3, 4, 7):
            t += 1
        
        # logic from https://www.reddit.com/r/adventofcode/comments/rbvpui/
        match len(signal):
            # Easy digits
            case 2: trueOutput += '1'
            case 3: trueOutput += '7'
            case 4: trueOutput += '4'
            case 7: trueOutput += '8'
            
            # 5 segments (2, 3 or 5)
            case 5:
                if signal.intersection(sig1) == sig1:
                    trueOutput += '3'
                elif signal.intersection(diff) == diff:
                    trueOutput += '5'
                else:
                    trueOutput += '2'
            
            # 6 segments (6, 9 or 0)
            case 6:
                if signal.intersection(sig4) == sig4:
                    trueOutput += '9'
                elif signal.intersection(diff) == diff:
                    trueOutput += '6'
                else:
                    trueOutput += '0'
    totalOutput += int(trueOutput)


# Output
print(f'Part 1: {t}\nPart 2: {totalOutput}')
