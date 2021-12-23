
from aocd.models import Puzzle

testdat = [199
,200
,208
,210
,200
,207
,240
,269
,260
,263]

def increase_counter(depths):
    return sum(b>a for a, b in zip(depths[:-1], depths[1:]))

def window_depths(depths, window=3):
    windsums = []
    for i in range(window-1, len(depths)):
        windsums.append(sum(depths[i-(window-1):i+1]))
    return windsums


puzzle = Puzzle(year=2021, day=1)
puzzle_data = [int(val) for val in puzzle.input_data.splitlines()]

# Pt 1.
print(increase_counter(puzzle_data))

# Pt 2.
print(increase_counter(window_depths(puzzle_data)))




