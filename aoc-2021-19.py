
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
scnl = reorientor(tdat2[1])
scn0
len(scnl)


# Different approach - findings pairwise distances
def dist(tup):
    """ tup = tuple of coordinate arrays """
    return np.sqrt(np.sum((tup[0] - tup[1])**2, axis=0))


ta = np.array([[1,2,3], [4,5,6], [7,8,9]])

tups = itertools.combinations(ta, r=2)
dsts = map(dist, tups)
[i for i in dsts]



for arr in tdat2:
    tups = map(dist, itertools.combinations(arr, r=2))

dists = [list(map(dist, itertools.combinations(arr, r=2))) for arr in tdat2]

