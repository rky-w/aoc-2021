
import sys
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter
import numpy as np
import pandas as pd
import time
import math
import re

puzzle = Puzzle(year=2021, day=17)
puzldat = [val for val in puzzle.input_data.splitlines()]

testdat = ['target area: x=20..30, y=-10..-5']


def ta(line):
    res = re.findall('x=([0-9-]*)..([0-9-]*), y=([0-9-]*)..([0-9-]*)', line[0])
    resi = [int(val) for val in res[0]]
    return tuple(resi[:2]), tuple(resi[2:])
    

def tozero(v):
    if v==0:
        return 0
    elif v>0:
        return v-1
    elif v<0:
        return v+1


def traj(vx, vy, tx, ty):
    px, py = 0, 0
    while py > ty[0]:
        px += vx
        py += vy
        vx = tozero(vx)
        vy -= 1
        if tx[0] <= px <= tx[1] and ty[0] <= py <= ty[1]:
            return True
    return False


def trajy(ay):
    py = 0
    i = 0
    hy = ay
    while py > ty[0]:
        i += 1
        py += ay
        ay -= 1
        print(f"i: {i}, py: {py}, ay: {ay}")
        if ay==0:
            hp = py
        if ty[0] <= py <= ty[1]:
            return i, hp
    raise ValueError(f'Target not reached with initial y velocity: {hy}')



# Pt 1. Answer
tx, ty = ta(puzldat)
ay = -ty[0]-1
i, maxy = trajy(ay)
print(maxy)



# Find all starting trajectories

""" 
y's from ty[0] to maxy
x's from ... to tx[1]
"""

res = []
for x in range(1, tx[1]+1):
    for y in range(ty[0], maxy+1):
        if traj(x, y, tx, ty):
            res.append((x, y))

# Pt 2 answer, slow but works (could speed up by finding min x)
print(len(res))
