with open('day22.txt') as file:
    data = [i.strip() for i in file.readlines()]

grid = dict()
for colNum in range(len(data)):
    for charNum in range(len(data[colNum])):
        if data[colNum][charNum] == '#':
            grid[(charNum - len(data[colNum]) // 2, colNum - len(data) // 2)] = 2

X = 0
Y = 0
direction = 0
infections = 0


for _ in range(10000000):
    direction += grid.setdefault((X, Y), 0) - 1
    direction %= 4
    
    grid[(X, Y)] = (grid[(X, Y)] + 1) % 4
    if grid[(X, Y)] == 2:
        infections += 1
    
    if direction == 0:
        Y -= 1
    elif direction == 1:
        X += 1
    elif direction == 2:
        Y += 1
    else:
        X -= 1

print(infections)
