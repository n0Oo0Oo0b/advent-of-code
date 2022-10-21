with open('day8.txt') as file:
    data = [i.strip() for i in file.readlines()]

originalLength = len(''.join(data))

parsedLength = len(''.join(eval(i) for i in data))
print(originalLength - parsedLength)

deparsedLength = 0
for i in data:
    a = i.count('\\') + i.count('"') + 2
    deparsedLength += a
print(deparsedLength)
