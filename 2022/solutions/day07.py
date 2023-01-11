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
    part1 = sum(i for i in all_dir_sizes if i <= 1e5)
    root_size = stack[0]
    part2 = min(i for i in all_dir_sizes if i >= root_size - 4e7)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
