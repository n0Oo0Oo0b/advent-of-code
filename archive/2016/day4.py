from collections import Counter

with open('day4.txt') as file:
    data = [i.strip().split('-') for i in file.readlines()]

t = 0
remove = []
for i, sector in enumerate(data):
    sector = sector.copy()
    check = sector.pop(-1)
    ID = int(check[:3])
    others = Counter(''.join(sector))
    mostCommon = ''.join(map(lambda x: x[0], sorted(others.items(), key=lambda x: (-x[1], x[0]))[:5]))
    if check[3:] == f'[{mostCommon}]':
        t += ID
    else:
        remove.append(i)

print(t)

for i in reversed(remove):
    data.pop(i)

ab = 'abcdefghijklmnopqrstuvwxyz'
for sector in data:
    check = sector.pop(-1)
    ID = int(check[:3])
    others = ' '.join(sector)
    new = ''
    for char in others:
        if char == ' ':
            new += ' '
        else:
            new += ab[(ab.index(char) + ID)%26]
    if 'north' in new:
        print(ID)
