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
        part1 += self + 1  # points for playing
        part1 += ((self - opponent + 1) % 3) * 3  # win/tie/loss
        # Part 2
        part2 += self * 3  # win/tie/loss
        part2 += (opponent + self - 1) % 3 + 1  # playing
    return part1, part2


def speedcode_solution(inp):
    # Spaghetti code warning
    lines = inp.splitlines()  # done with aocd.lines
    t = 0
    for i in lines:
        a, b = i.split()
        a = {'A': 'X', 'B': 'Y', 'C': 'Z'}[a]
        if a == b:
            t += 3
        elif (a, b) in [('X', 'Y'), ('Y', 'Z'), ('Z', 'X')]:
            t += 6
        if b == 'X':
            t += 1
        elif b == 'Y':
            t += 2
        else:
            t += 3
    part1 = t
    t = 0
    for i in lines:
        a, b = i.split()
        if b == 'Y':  # tie
            t += 3
            if a == 'A':
                t += 1
            elif a == 'B':
                t += 2
            else:
                t += 3
        elif b == 'Z':  # win
            t += 6
            if a == 'A':
                t += 2
            elif a == 'B':
                t += 3
            else:
                t += 1
        else:  # lose
            if a == 'A':
                t += 3
            elif a == 'B':
                t += 1
            else:
                t += 2
    part2 = t
    return part1, part2


if __name__ == '__main__':
    from aocd import data
    part1, part2 = solve(data)
    print(f"Part 1: {part1}\nPart 2: {part2}")
