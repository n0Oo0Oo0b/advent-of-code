with open('day13.txt') as file:
    data = [tuple(map(int, i.split(': '))) for i in file.readlines()]


t = 0
for layer, depth in data[1:]:
    if layer % ((depth-1)*2) == 0:
        t += layer*depth
print(t)


d = -1
c = True
while c:
    c = False
    for layer, depth in data:
        if layer % ((depth - 1) * 2) == 0:
            c = True
            break
    for i in range(len(data)):
        data[i] = (data[i][0]+1, data[i][1])
    d += 1
print(d)
