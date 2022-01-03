
from aocd.models import Puzzle
import numpy as np
import re

puzzle = Puzzle(year=2021, day=13)
puzldat = [val for val in puzzle.input_data.splitlines()]

testdat = [
'6,10',
'0,14',
'9,10',
'0,3',
'10,4',
'4,11',
'6,0',
'6,12',
'4,1',
'0,13',
'10,12',
'3,4',
'3,0',
'8,4',
'1,10',
'2,14',
'8,10',
'9,0',
'',
'fold along y=7',
'fold along x=5'
]


def datparse(lines):
    coords = []
    instructions = []
    for line in lines:
        if line != '':
            if line[0] != 'f':
                coords.append(line.split(','))
            elif line[0] == 'f':
                instructions.extend(re.findall(r'^fold along ([xy])=([-0-9]*)', line))
    arr = np.array(coords, dtype=int)     
    mat = np.zeros([max(arr[:, 1])+1, max(arr[:, 0])+1], dtype=int)
    for coord in arr:
        mat[coord[1], coord[0]] = 1

    return mat, instructions

def folder(m, d):
    if d[0] == 'x':
        m = m.T

    y = int(d[1])
    m1 = m[:y, :]
    m2 = m[y+1:, :]

    mx = m1.shape[1]
    m1s = m1.shape[0]
    m2s = m2.shape[0]
    adiff = abs(m1s - m2s)

    if adiff > 0:
        z = np.zeros([adiff, mx], dtype=int)
        if m1s < m2s:
            m1 = np.concatenate((z, m1))
        elif m2s < m1s:
            m2 = np.concatenate((m2, z))

    mn = np.array(m1 + m2[::-1, :] > 0, dtype=int)
    if d[0] == 'x':
        return mn.T
    else:
        return mn


mat, instructions = datparse(puzldat)

# Pt 1. Answer
print((folder(mat, instructions[0]) > 0).sum())

# Pt 2. Answer

for d in instructions:
    mat = folder(mat, d)


# Plot the characters
import matplotlib.pyplot as plt

plt.subplot()
plt.imshow(mat)
plt.show()
