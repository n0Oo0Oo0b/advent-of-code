# Import puzzle input
with open('day3.txt') as file:
    data = file.read().split('\n')


# Rotate the data (dataR[0] would be the first bit of each line, etc.)
dataR = [''.join([data[j][i] for j in range(len(data))]) for i in range(len(data[0]))]

gamma = int(''.join(['0' if i.count('0') > i.count('1') else '1' for i in dataR]), 2)  # Calculate gamma
epsilon = gamma ^ (2**len(dataR) - 1)  # Big brain math¹


# Copy the input data so they don't mess with each other
o2ratings = data.copy()
co2ratings = data.copy()

for indexNum in range(len(dataR)):
    # Count number of 0s and 1s in index position
    c0 = [i[indexNum] for i in o2ratings].count('0')
    c1 = len(o2ratings) - c0
    
    # Remove values with incorrect bit in current position
    for i in [i for i in o2ratings if i[indexNum] == ('0' if c0 <= c1 else '1')]:
        o2ratings.remove(i)

for indexNum in range(len(dataR)):
    # Count number of 0s and 1s in index position
    c0 = [i[indexNum] for i in co2ratings].count('0')
    c1 = len(co2ratings) - c0
    
    # Remove values with incorrect bit in current position
    for i in [i for i in co2ratings if i[indexNum] == ('1' if c0 <= c1 else '0')]:
        co2ratings.remove(i)

    # Break out of loop if 1 value remains (CO2 rating)
    if len(co2ratings) == 1:
        break


# Output
oxygenRating, co2rating = int(o2ratings[0], 2), int(co2ratings[0], 2)
print(f'Part 1: {gamma * epsilon}\nPart 2: {oxygenRating * co2rating}')

"""
Footnotes

¹ - Because gamma takes the most common bits (1 or 0) and epsilon takes the least common bits, they are binary opposites of each other (eg: if gamma='010011' then epsilon='101100').
    Therefore, they will produce an XOR of '111111...' (gamma^epsilon='111111...'), which translates to gamma^epsilon = 2**[length of gamma/epsilon]-1
    Combined with the fact that if A^B=C then A^C=B, we can calculate epsilon using gamma using gamma^(2**len(dataR)-1)
    
    ^ = bitwise XOR
"""