def execute(commands, **registers):
    pointer = 0
    while pointer < len(commands):
        cmd, arg = commands[pointer]
        step_size = 1
        if cmd == 'inc':
            registers[arg] += 1
        elif cmd == 'hlf':
            registers[arg] //= 2
        elif cmd == 'tpl':
            registers[arg] *= 3
        elif cmd == 'jmp':
            step_size = arg
        elif cmd == 'jie':
            reg, amount = arg
            if registers[reg] % 2 == 0:
                step_size = amount
        elif cmd == 'jio':
            reg, amount = arg
            if registers[reg] == 1:
                step_size = amount
        pointer += step_size
    return registers


def day23(inp):
    commands = []
    for line in inp.splitlines():
        cmd, arg = line.split(maxsplit=1)
        if cmd in ('jie', 'jio'):
            reg, amount = arg.split(', ')
            arg = (reg, int(amount))
        elif cmd == 'jmp':
            arg = int(arg)
        commands.append((cmd, arg))
    part1 = execute(commands, a=0, b=0)['b']
    part2 = execute(commands, a=1, b=0)['b']
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    print("Part 1: {}\nPart 2: {}".format(*day23(data)))
