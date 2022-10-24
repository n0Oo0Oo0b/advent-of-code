def day2(data):
    # parse input
    boxes = []
    for row in data.splitlines():
        boxes.append(sorted(int(i) for i in row.split('x')))

    # solve
    total_paper = 0
    total_ribbon = 0
    for l, w, h in boxes:
        total_paper += 3*l*w + 2*h*(w+l)
        total_ribbon += 2*(l+w) + l*w*h
    return total_paper, total_ribbon

if __name__ == '__main__':
    with open('inputs/day2.txt') as file:
        data = file.read()
    print("Part 1: {}\nPart 2: {}".format(*day2(data)))
