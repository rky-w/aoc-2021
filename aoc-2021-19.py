
import sys
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter
import itertools
import numpy as np
import pandas as pd
import time
import math as m
import re
import ast
from pprint import pprint
from scipy.spatial.transform import Rotation as R


puzzle = Puzzle(year=2021, day=19)
puzldat = [val for val in puzzle.input_data.splitlines()]
testdat = [line.rstrip() for line in open('testdat.txt')]
testdat2 = [line.rstrip() for line in open('testdat2.txt')]


def loader(dat):
    lst = []
    for d in dat:
        if d[:3] == '---':
            res = []
        elif d == '':
            lst.append(np.array(res, dtype = int))
            res = []
        else:
            res.append(d.split(','))
    return lst


def reorientor(arr):        
    pairs = [x[0]+x[1] for x in itertools.permutations(['x','y','z'], r = 2)]
    flips = [0, 90, 180, 270, 360]
    spins = [0, 90, 180, 270, 360]
    newarrs = [arr]
    for pair in pairs:
        for flip in flips:
            for spin in spins:
                r = R.from_euler(pair, [flip, spin], degrees=True)
                arr = r.apply(arr).round().astype(int)
                if not str(arr) in [str(r) for r in newarrs]:
                    newarrs.append(arr)
    return newarrs

pdat = loader(puzldat)
tdat = loader(testdat)
tdat2 = loader(testdat2)

ntdat = [reorientor(dat) for dat in tdat]

for x in ntdat[0]:
    print(x)

[len(x) for x in ntdat]
# Seems to be working for the first example case

# Second example - need to work out how to check for overlap...
scn0 = tdat2[0]
scnl = [reorientor(dat) for dat in tdat[1]]
