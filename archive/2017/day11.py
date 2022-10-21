#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
with open('day11.txt') as file:
    data = file.read().split(',')

X = 0
Y = 0
maxS = 0
for direction in data:
    if 'e' in direction:
        X += 1
    elif 'w' in direction:
        X -= 1
    
    if direction == 'n':
        Y += 2
    elif direction == 's':
        Y -= 2
    elif 'n' in direction:
        Y += 1
    elif 's' in direction:
        Y -= 1
    if (abs(X)+abs(Y))//2 > maxS:
        maxS = (abs(X)+abs(Y))//2
print((abs(X)+abs(Y))//2)
print(maxS)
