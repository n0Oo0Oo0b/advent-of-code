from aocd import lines as inp

t = [0]
for x in inp:
    if x == '':
        t.append(0)
    else:
        t[-1] += int(x)
t.sort()

print(t[-1], sum(t[-3:]))
