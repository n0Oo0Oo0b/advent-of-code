from aocd import lines


part1 = 0
part2 = 0
for line in lines:
    a, b, c, d = list(int(i) for i in re.findall(r'\d+', line))
    e, f = set(range(a, b + 1)), set(range(c, d + 1))
    if e <= f or f <= e:
        part1 += 1
    if e & f:
        part2 += 1
