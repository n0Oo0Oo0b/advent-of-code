from aocd import data as inp


a, _, b = inp.partition('\n\n')
stack = a.splitlines()
instructions = b.splitlines()

data = [[] for _ in range(9)]
for col in range(7, -1, -1):
    for i, x in enumerate(range(1, 34, 4)):
        if stack[col][x] == ' ':
            continue
        data[i].append(stack[col][x])
data2 = [i.copy() for i in data]

for line in instructions:
    a, b, c = (int(i) for i in re.findall(r'\d+', line))
    for _ in range(a):
        val = data[b - 1].pop(-1)
        data[c - 1].append(val)
    values = data2[b - 1][-a:]
    data2[b - 1] = data2[b - 1][:-a]
    data2[c - 1].extend(values)

print(''.join(l[-1] for l in data))
print(''.join(l[-1] for l in data2))
