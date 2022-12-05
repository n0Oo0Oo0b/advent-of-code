import re


def solve(inp):
    # Relatively simple refactor of speedcode_solution
    raw_stack, _, instructions = inp.partition('\n\n')
    raw_stack = raw_stack.splitlines()
    instructions = instructions.splitlines()
    # Parse stacks
    stack_1 = [[] for _ in range(len(raw_stack[0]) // 4 + 1)]  # Part 1
    for row in raw_stack[-2::-1]:
        for i, e in enumerate(row[1::4]):
            if e == ' ':
                continue
            stack_1[i].append(e)
    stack_2 = [crates.copy() for crates in stack_1]  # Part 2
    # Run instructions
    for line in instructions:
        count, loc1, loc2 = (int(i) for i in re.findall(r'\d+', line))
        loc1 -= 1
        loc2 -= 1
        # Part 1
        for _ in range(count):
            value = stack_1[loc1].pop(-1)
            stack_1[loc2].append(value)
        # Part 2
        values = stack_2[loc1][-count:]
        stack_2[loc1] = stack_2[loc1][:-count]
        stack_2[loc2].extend(values)
    # Combine
    part1 = ''.join(i[-1] for i in stack_1)
    part2 = ''.join(i[-1] for i in stack_2)
    return part1, part2


def speedcode_solution(inp):
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
            val = data[b-1].pop(-1)
            data[c-1].append(val)
        values = data2[b-1][-a:]
        data2[b-1] = data2[b-1][:-a]
        data2[c-1].extend(values)

    part1 = ''.join(l[-1] for l in data)
    part2 = ''.join(l[-1] for l in data2)
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
