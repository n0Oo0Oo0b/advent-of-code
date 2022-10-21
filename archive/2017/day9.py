data = [183, 0, 31, 146, 254, 240, 223, 150, 2, 206, 161, 1, 255, 232, 199, 88]
hash_list = '183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'

lst = list(range(256))
pos = 0


def reverseList(l, sI, eI):
    l = l.copy()
    shiftLength = eI - sI
    shiftValue = -sI
    l = l[sI:] + l[:sI]
    l = list(reversed(l[:shiftLength])) + l[shiftLength:]
    l = l[shiftValue:] + l[:shiftValue]
    return l


i = 0
while i < 64:
    j = 0
    skip = 0
    while j < len(hash_list):
        end = ((start + hash_list[j] - 1) % 256)
        lst = reverseList(lst, start, end)
        start = (start + hash_list[j] + skip) % 256
        skip += 1
        j += 1
    i += 1
