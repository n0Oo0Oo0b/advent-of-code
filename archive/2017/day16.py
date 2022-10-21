with open('day16.txt') as file:
    data = file.read()


def solve(raw_steps):
    steps = [d for d in raw_steps.split(',')]
    programs = [n for n in 'abcdefghijklmnop']
    seen = []
    for i in range(1000000000):
        h = tuple(programs)
        if h in seen:
            return ''.join(seen[1000000000 % len(seen)])
        seen += [h]
        for step in steps:
            if step[0] == 's':
                node = int(step[1:])
                programs = programs[-node:] + programs[:-node]
            if step[0] == 'x':
                n1, n2 = list(map(int, step[1:].split('/')))
                programs[n1], programs[n2] = programs[n2], programs[n1]
            if step[0] == 'p':
                n1, n2 = step[1:].split('/')
                d1, d2 = programs.index(n1), programs.index(n2)
                programs[d1], programs[d2] = n2, n1
    return ''.join(programs)


print(solve(data))
