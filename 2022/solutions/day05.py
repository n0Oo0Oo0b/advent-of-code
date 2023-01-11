import re


def solve(inp):
    # Relatively simple refactor of speedcode_solution
    raw_stack, _, instructions = inp.partition('\n\n')
    raw_stack = raw_stack.splitlines()
    instructions = instructions.splitlines()
    # Parse stacks
    stack_1 = [[] for _ in range(len(raw_stack[8]) // 4 + 1)]  # Part 1
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


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
