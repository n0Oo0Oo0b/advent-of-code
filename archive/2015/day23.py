from contextlib import suppress

with open('day23.txt') as file:
    data = [i.split() for i in file.read().splitlines()]

registers = {'a': 0, 'b': 0} 
# registers['a'] = 1  # uncomment for part 2

i = 0
with suppress(IndexError):
    while True:
        d = 1
        match data[i]:
            case 'hlf', r:
                registers[r] //= 2
            case 'tpl', r:
                registers[r] *= 3
            case 'inc', r:
                registers[r] += 1
            case 'jmp', n:
                d = int(n)
            case 'jie', r, n:
                if registers[r] % 2 == 0:
                    d = int(n)
            case 'jio', r, n:
                if registers[r] == 1:
                    d = int(n)
            case _:
                raise ValueError(data[i])
        i += d

print(registers)
