def get_n(x, y):
    return ((x+y)**2 - x - 3*y) // 2 + 1  # I spent 20 minutes on this

y, x = 3010, 3019

code = 20151125
for _ in range(get_n(x, y) - 1):
    code = (code * 252533) % 33554393

print(code)
