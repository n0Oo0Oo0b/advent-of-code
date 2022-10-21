from aocd.models import Puzzle, User

day = 25

cookie = '53616c7465645f5f636fe3cd9a66a3ab33f275ca26ecd2b61e1c3b0d58e6aa733cd2e388b3c62082c1a4f498bbce2a07'
puzzle = Puzzle(2021, day, User(cookie))
fileName = f'inputs/day{day}.txt'

with open(fileName, mode='w') as file:
    file.write(puzzle.input_data)
print(f'Day {day} ({puzzle.title})\n'
      f'Saved to: {fileName}')
