dat={41: 0, 1: 90, 37: 35, 911: 41, 13: 54, 17: 55, 23: 64, 29: 70, 827: 72, 19: 91}
i = 100000000000000
w=True
while True:
    w = True
    for j in dat:
        k = dat[j]
        if i%j != k:
            w = False
    i += 1
print(i)
