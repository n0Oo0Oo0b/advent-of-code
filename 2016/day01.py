def solution(inp):
    position = 0j
    direction = 0j
    visited = set()
    part2 = None
    for instruction in inp.split(', '):
        rotation = instruction[0]
        distance = int(instruction[1:])
        if rotation == 'L':
            direction *= 1j
        elif rotation == 'R':
            direction *= -1j
        if part2 is None:
            for _ in range(distance):
                position += direction
                if position in visited:
                    part2 = position
                visited.add(position)
        else:
            position += distance * direction
    part1 = int(abs(position.real) + abs(position.imag))
    part2 = int(abs(part2.real) + abs(part2.imag))
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solution(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
