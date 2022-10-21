data = [9,3,1,0,8,4]

def play(nums,length):
    nums.reverse()
    while len(nums) < length:
        prevNum = nums[-1]
        try:
            nums.append(nums.index(prevNum)+1,0)
        except:
            nums.append(0,0)
    return nums[-1]
print(play(data,2020))
print(play(data,30000000))
