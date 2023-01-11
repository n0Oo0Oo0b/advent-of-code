from aocd import lines

# Spaghetti code warning
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
print(t)

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
print(t)
