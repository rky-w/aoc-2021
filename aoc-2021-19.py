
import sys
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter
import itertools
import numpy as np
import pandas as pd
import time
import math
import re
import ast
from pprint import pprint
from scipy.spatial.transform import Rotation as R


puzzle = Puzzle(year=2021, day=19)
puzldat = [val for val in puzzle.input_data.splitlines()]
testdat = [line.rstrip() for line in open('testdat.txt')]


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
    pairs = ['zx', 'xy', 'yz', 'yx', 'zy', 'xz']
    flips = [0, 90, 180, 270]
    spins = [0, 90, 180, 270]
    newarrs = []
    for pair in pairs:
        for flip in flips:
            for spin in spins:
                r = R.from_euler(pair, [flip, spin], degrees=True)
                newarrs.append(r.apply(arr).round())
    return newarrs


pdat = loader(puzldat)
tdat = loader(testdat)


<<<<<<< HEAD
ntdat = [reorientor(dat) for dat in tdat]
=======
def reorientor(vec):
    pairs = ['zx', 'xy', 'yz']
    flips = [0, 180]
    spins = [0, 90, 180, 270]
    arrs = []
    for pair in pairs:
        for flip in flips:
            for spin in spins:
                # print(pair, flip, spin)
                r = R.from_euler(pair, [flip, spin], degrees=True)
                # print(r.as_euler('xyz', degrees=True))
                arrs.append(np.array(np.round(r.apply(vec)), dtype=int))
    return arrs

res = list(map(reorientor, tdat))





>>>>>>> a382341f5e73be7d80d648e28956144d96d320a0

lst = [str(n[3]) for n in ntdat[0]]
pprint(lst)
len(lst)
len(set(lst))
pprint(set(lst))

[x[0]+x[1] for x in itertools.permutations(['x','y','z'], r = 2)]