from aocd import lines as inp

x = 1
tick = 0
screen = [[]]
s = 0
for line in inp:
    for _ in range(2 - ('noop' in line)):
        tick += 1
        if (tick - 20) % 40 == 0:
            s += tick * x
        if abs(len(screen[-1]) - x) < 2:
            screen[-1].append('#')
        else:
            screen[-1].append(' ')
        if len(screen[-1]) == 40:
            screen.append([])
    if 'addx' in line:
        x += int(line.split()[1])

print(s)
print('\n'.join(''.join(i) for i in screen))  # read part 2 from screen
