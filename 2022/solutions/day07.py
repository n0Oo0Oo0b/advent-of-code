def solve(inp):
    stack = [0]
    all_dir_sizes = []
    for line in inp.splitlines():
        if line[0].isdigit():  # add file
            for i in range(len(stack)):
                stack[i] += int(line.split()[0])
        elif '$ cd' in line:
            if '..' in line:  # previous level
                dir_size = stack.pop()
                all_dir_sizes.append(dir_size)
            else:  # next level
                stack.append(0)
    all_dir_sizes += stack  # add remaining directories
    print(all_dir_sizes, stack, sep='\n')
    return None, None


def speedcode_solution(inp):
    lines = inp.splitlines()
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
    space = 70000000 - size
    target = 30000000 - space
    part2 = 70000000
    recurse2(file_system)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
