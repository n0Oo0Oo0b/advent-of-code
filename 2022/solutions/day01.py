def solve(inp):
    # Use input
    elves = []
    for elf_data in inp.split('\n\n'):
        # Calculate total calories for elf
        numbers = [int(i) for i in elf_data.split('\n')]
        elf_carrying = sum(numbers)
        elves.append(elf_carrying)
    elves.sort()
    # Calculate result
    part1 = elves[-1]
    part2 = sum(elves[-3:])
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
