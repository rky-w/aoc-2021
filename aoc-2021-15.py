
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter

puzzle = Puzzle(year=2021, day=15)
puzldat = [val for val in puzzle.input_data.splitlines()]
