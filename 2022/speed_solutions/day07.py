from aocd import lines as inp

lines.append('$')


def get_path(path):
    directory = file_system
    for folder in path:
        directory = directory[folder]
    return directory


current_path = []
file_system = {}
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith('$ cd'):
        folder = line.split()[-1]
        if folder == '/':
            current_path = []
        elif folder == '..':
            current_path.pop()
        else:
            current_path.append(folder)
    elif line == '$ ls':
        i += 1
        while not lines[i].startswith('$'):
            a, b = lines[i].split()
            if a == 'dir':
                get_path(current_path)[b] = {}
            else:
                get_path(current_path)[b] = int(a)
            i += 1
        i -= 1
    i += 1


def recurse(system):
    t = 0
    for k, v in system.items():
        if isinstance(v, int):
            t += v
        else:
            t += recurse(v)
    if t < 100_000:
        nonlocal part1
        part1 += t
    return t


def recurse2(system):
    t = 0
    for k, v in system.items():
        if isinstance(v, int):
            t += v
        else:
            t += recurse2(v)
    nonlocal part2
    if target <= t < part2:
        part2 = t
    return t


part1 = 0
size = recurse(file_system)
print(part1)
space = 70000000 - size
target = 30000000 - space
part2 = 70000000
recurse2(file_system)
print(part2)
