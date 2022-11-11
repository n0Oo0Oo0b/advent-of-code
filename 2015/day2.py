def day2(data):
    # Parse input
    boxes = []
    for row in data.splitlines():
        boxes.append(sorted(map(int, row.split('x'))))
    # Solve
    total_paper = 0
    total_ribbon = 0
    for l, w, h in boxes:
        total_paper += 3*l*w + 2*h*(l+w)  # 2*l*(l+w) = 2*w*h + 2*l*h
        total_ribbon += 2*(l+w) + l*w*h
    return total_paper, total_ribbon


if __name__ == '__main__':
    with open('inputs/day2.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day2(data)))
