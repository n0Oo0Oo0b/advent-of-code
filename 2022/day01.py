from aocd import lines as inp

t = [0]
for x in inp:
    if x == '':
        t.append(0)
    else:
        t[-1] += int(x)

print(max(t))
print(sum(sorted(t)[-3:]))
