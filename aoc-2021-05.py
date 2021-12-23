
from aocd.models import Puzzle
import pandas as pd
import numpy as np
from collections import Counter

puzzle = Puzzle(year=2021, day=5)
puzzle_data = [val for val in puzzle.input_data.splitlines()]

testdat = [
'0,9 -> 5,9',
'8,0 -> 0,8',
'9,4 -> 3,4',
'2,2 -> 2,1',
'7,0 -> 7,4',
'6,4 -> 2,0',
'0,9 -> 2,9',
'3,4 -> 1,4',
'0,0 -> 8,8',
'5,5 -> 8,2'
]

# Convert input list to array of coordinates
def get_coords(lst):
    return np.array([[[int(i) for i in x.split(',')] for x in row.split(' -> ')] for row in lst], dtype=int)


def filter_coords(arr):
    return np.array([a for a in arr if a[0][0] == a[1][0] or a[0][1] == a[1][1]])


def line_eqn(coord):
    m = (coord[1][1] - coord[0][1]) / (coord[1][0] - coord[0][0])
    c = coord[0][1] - (m * coord[0][0])
    return m, c


def integral_coords(coord):
    m, c = line_eqn(coord)
    intcoords = []
    if coord[0][0] == coord[1][0]:
        miny = min(coord[:, 1])
        maxy = max(coord[:, 1])
        for y in range(miny, maxy+1):
            x = coord[0][0]
            intcoords.append([int(x), int(y)])
    else:
        minx = min(coord[:,0])
        maxx = max(coord[:,0])
        for x in range(minx,maxx+1):
            y = m * x + c
            if y % 1 == 0:
                intcoords.append([int(x), int(y)])
    return intcoords


def expand_coords(coords):
    all_coords = []
    for coord in coords:
        all_coords += integral_coords(coord)
    return all_coords     


def count_coords(coordlist):
    freqs =  Counter(tuple(item) for item in coordlist)
    return sum(np.array(list(freqs.values())) > 1)


coords = get_coords(puzzle_data)

# Pt 1. Filter to horizontal and vertical
print(count_coords(expand_coords(filter_coords(coords))))

# Pt 2. Consider diagonals too...
print(count_coords(expand_coords(coords)))
