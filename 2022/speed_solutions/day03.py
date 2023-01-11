from aocd import lines


def priority(a):
    if a.islower():
        return ord(a) - ord('a') + 1
    else:
        return ord(a) - ord('A') + 27


t = 0
for line in lines:
    s = len(line) // 2
    a = ''.join(set(line[:s]) & set(line[s:]))
    t += priority(a)
print(t)

t = 0
for x in range(0, len(lines), 3):
    d = lines[x:x + 3]
    t += priority(''.join(set(d[0]) & set(d[1]) & set(d[2])))
print(t)
