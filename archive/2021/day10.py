with open('day10.txt') as file:
    data = file.read().split('\n')

# Dictionary to return the start char of chunk with the end char
opposite = {']': '[', '}': '{', ')': '(', '>': '<'}

# Dictionary to store scores to calculate syntax score + autocomplete score
scores = {')': 3, ']': 57, '}': 1197, '>': 25137,  # Part 1 (syntax scores)
          '(': 1, '[': 2, '{': 3, '<': 4  # Part 2 (autocomplete scores)
          }


def validate(line):
    """
    Validates a line, and returns invalid character if line is corrupted or missing characters if line is incomplete
    """
    enteredChunks = []  # Stores which nested chunks the index is in
    for char in line:
        if char in ('[', '{', '(', '<'):  # Enter a chunk
            enteredChunks.append(char)
        else:  # (try to) Leave a chunk
            if enteredChunks[-1] == opposite[char]:
                enteredChunks.pop(-1)  # Character is valid (leave the chunk)
            else:
                return char  # Corrupted line due to invalid char (Part 1)
    return enteredChunks[::-1]  # Incomplete line (Part 2)


# Main loop using input data
t, t2 = 0, []
for line in data:
    if type(x := validate(line)) == str:  # Part 1 (syntax)
        t += scores[x]
    else:  # Part 2 (autocomplete)
        score = 0
        for missing in x:
            score = (score * 5) + scores[missing]
        t2.append(score)
t2.sort()

# Output
print(f'Part 1: {t}\nPart 2: {t2[len(t2)//2]}')
