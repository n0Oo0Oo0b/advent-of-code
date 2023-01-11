class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Node({self.value})"


nums = []
for i in open(0):
    n = Node(int(i))  # multiply by 811589153 for pt2
    nums.append(n)
    if n.value == 0:
        zero = n

order = nums.copy()
for node in order:  # order*10 for pt2
    i = nums.index(node)
    nums.pop(i)
    new = i + node.value
    nums.insert(new % len(nums), node)  # why are there no off by 1s here lmao

z_i = nums.index(zero)
print(sum(nums[i % len(nums)].value for i in (z_i+1000, z_i + 2000, z_i + 3000)))
