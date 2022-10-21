with open('day2.txt') as file:
    data = file.read().split('\n')

depth = 0
distance = 0
depth_2 = 0
distance_2 = 0
aim_2 = 0

for i in data:
    cmd, value = tuple(i.split(' '))
    value = int(value)
    if cmd == 'up':
        aim_2 -= value
        depth -= value
    elif cmd == 'down':
        aim_2 += value
        depth += value
    elif cmd == 'forward':
        distance_2 += value
        depth_2 += value * aim_2
        distance += value

print(distance * depth)
print(distance_2 * depth_2)
