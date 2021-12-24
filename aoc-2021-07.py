
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=7)
puzzle_data = [val for val in puzzle.input_data.splitlines()]
puzzle_crabs = [int(val) for val in puzzle_data[0].split(',')]

testcrabs = [16,1,2,0,4,2,7,1,2,14]

def horiz_cost(crabs, pos):
    return sum(abs(crab-pos) for crab in crabs)


def increasing_cost(crabs, pos):
    return sum([(base / 2) * (1 + base) for base in [abs(crab-pos) for crab in crabs]])
    

def find_costs(crabs, constant_cost=True):
    minpos = min(crabs)
    maxpos = max(crabs)
    costs = dict.fromkeys(range(minpos, maxpos+1))
    for pos in costs.keys():
        if constant_cost:
            costs[pos] = horiz_cost(crabs, pos)
        else:
            costs[pos] = increasing_cost(crabs, pos)
    return costs

# Pt 1. Constant movement cost
costs = find_costs(puzzle_crabs)
min(costs.values())

# Pt 2. Increasing movement cost
newcosts = find_costs(puzzle_crabs, constant_cost=False)
min(newcosts.values())

