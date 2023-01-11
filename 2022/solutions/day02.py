def solve(inp):
    lines = inp.splitlines()
    part1 = 0
    part2 = 0
    for line in lines:
        opponent, self = line.split()
        # 0 = rock, 1 = paper, 2 = scissor
        opponent = 'ABC'.index(opponent)
        self = 'XYZ'.index(self)
        # Part 1
        part1 += self + 1  # r/p/s
        part1 += ((self - opponent + 1) % 3) * 3  # win/tie/loss
        # Part 2
        part2 += self * 3  # win/tie/loss
        part2 += (opponent + self - 1) % 3 + 1  # r/p/s
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
