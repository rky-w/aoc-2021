import numpy as np
import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=9)
puzzle_data = [val for val in puzzle.input_data.splitlines()]

testdat = [
'2199943210',
'3987894921',
'9856789892',
'8767896789',
'9899965678'
]


def cleaner(input_data):
    return np.array([list(row) for row in input_data], dtype=int)
    
arr = cleaner(puzzle_data)

minimagrid = np.empty(arr.shape, dtype=bool)

for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
       
        neighbours = []
        if r > 0:
            neighbours.append(arr[r-1, c])
        if c < arr.shape[1] - 1:
            neighbours.append(arr[r, c+1])
        if r < arr.shape[0] - 1:
            neighbours.append(arr[r+1, c])
        if c > 0:
            neighbours.append(arr[r, c-1])

        minimagrid[r, c] = (arr[r, c] < neighbours).all()


# Pt 1. Answer
print((arr[minimagrid] + 1).sum())




def getbasin(start, history = None):
    if history == None:
        history = []
    basin = []
    circ = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for coord in circ:
        testcoord = tuple(map(sum, zip(start, coord)))
        #print(f"Testcoord is {testcoord}")
        if testcoord not in history and testcoord not in basin and all([i >= 0 and i <= j-1 for i, j in zip(testcoord, arr.shape)]):
            #print(f"Testcoord valid")
            if arr[testcoord] < 9: # and arr[testcoord] in [arr[start], arr[start]+1]:
                """
                Initially, the above conditional was set to only work on values the same or one up from the minima each time,
                thereby creating paths from the minima which did not allow jumps to numbers higher than one away.
                It turns out the basins are actually defined by all values between the minima and 9, regardless of step size.
                """
                #print(f"Testcoord in basin")
                history.append(testcoord)
                basin.append(testcoord)
                basin.extend(getbasin(testcoord, history))
    #print(f"Returning basin {basin}")
    return list(set(basin))

minima = [(i, j) for (i, j) in zip(*np.where(minimagrid))]


basins = []
for (i, j) in zip(*np.where(minimagrid)):
    basin = getbasin((i, j))
    # basin.append((i, j))
    basins.append(basin)

basin_lens = [len(basin) for basin in basins]

# Pt 2. Answer
print(math.prod(sorted(basin_lens, reverse=True)[:3]))





# Plotting the basins for debugging
import matplotlib.pyplot as plt

colgrid = np.zeros(arr.shape, dtype=int)
minima = [(i, j) for (i, j) in zip(*np.where(minimagrid))]

col = 0
for basin in basins:
    col += 1
    if col == 6:
        col = 1
    for coord in basin:
        colgrid[coord] = str(col)


fig, ax = plt.subplots(figsize=(50, 50))
im = ax.imshow(colgrid)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        text = ax.text(j, i, arr[i, j], ha="center", va="center", color="r" if (i, j) in minima else "w")
fig.tight_layout()
plt.show()




