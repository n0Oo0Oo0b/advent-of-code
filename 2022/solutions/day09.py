def clamp(x, min_, max_):
    if x < min_:
        return min_
    elif x > max_:
        return max_
    else:
        return x


def solve(inp):
    # Complex numbers ftw
    directions = {
        'U': -1j,
        'D': 1j,
        'L': -1,
        'R': 1
    }
    rope = [0] * 10
    visited = set()
    visited2 = set()
    for line in inp.splitlines():
        # Parse line
        direction, distance = line.split()
        direction = directions[direction]
        distance = int(distance)
        # Move rope
        for _ in range(distance):
            rope[0] += direction  # Move head
            for i in range(1, 10):  # Simulate each link
                front = rope[i - 1]
                current = rope[i]
                delta = front - current
                dx, dy = delta.real, delta.imag
                if abs(dx) > 1 or abs(dy) > 1:
                    dx = clamp(dx, -1, 1)
                    dy = clamp(dy, -1, 1)
                    rope[i] += dx + dy*1j
            # Save positions of 2nd and last knot
            visited.add(rope[1])
            visited2.add(rope[-1])
    return len(visited), len(visited2)


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
