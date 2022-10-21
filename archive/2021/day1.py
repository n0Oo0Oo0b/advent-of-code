with open('day1.txt') as file:
    data = [int(i) for i in file.read().split('\n')]

t = 0
for i in range(1, len(data)):
    if data[i-1] < data[i]:
        t += 1

print(t)

t = 0
for i in range(3, len(data)):
    if sum(data[i-3:i]) < sum(data[i-2:i+1]):
        t += 1
print(t)
