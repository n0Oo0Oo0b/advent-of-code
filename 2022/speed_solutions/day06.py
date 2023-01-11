from aocd import data as inp


for i in range(len(inp)):
    if len(set(inp[i:i + 4])) == 4:
        break
print(i+4)
for i in range(len(inp)):
    if len(set(inp[i:i + 14])) == 14:
        break
print(i+14)
