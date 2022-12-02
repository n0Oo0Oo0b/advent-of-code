import aocd
from aocd.models import Puzzle
import solutions


for day_num in range(1, 26):
    solution = solutions.days.get(day_num)
    if solution is not None:
        puzzle = Puzzle(day=day_num, year=2022)
        part1, part2 = solution.solve(puzzle.input_data)
        puzzle.answer_a = part1
        print(puzzle.answer_a)
        if part2 is not None:
            puzzle.answer_b = part2
        print(f"Day {day_num}: {part1}, {part2}")
