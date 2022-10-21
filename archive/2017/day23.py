with open('day23.txt') as file:
    data = [i.strip().split(' ') for i in file.readlines()]

registers = {}
for char in 'abcdefgh':
    registers[char] = 0


def v(value):
    try:
        return int(value)
    except ValueError:
        return registers[value]


i = 0
t = 0
steps = 0
registers['a'] = 1
while i < len(data):
    cmd = data[i]
    func = cmd[0]
    X = cmd[1]
    Y = v(cmd[2])
    if func == 'set':
        registers[X] = Y
    elif func == 'sub':
        registers[X] -= Y
    elif func == 'mul':
        # t += 1
        registers[X] *= Y
    elif func == 'jnz':
        if v(X) != 0:
            i += Y - 1
    
    if steps < 1000:
        print(registers)
    if i == 10:
        registers['e'] += 50
        registers['g'] += 50
    
    i += 1
    steps += 1

print(t)
print(registers['h'])
