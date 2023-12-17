from util import *

lines = data.split("\n")

nums = list(map(get_ints, lines))

res = 0

for i in nums:
    res += int(str(i[0]) + str(i[-1]))
