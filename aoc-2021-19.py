
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


pdat = loader(puzldat)
tdat = loader(testdat)


def reorientor(vec):
    pairs = [x+y for x, y in itertools.permutations(['x', 'y', 'z'], r=2)]
    flips = [0, 90, 180, 270]
    spins = [0, 90, 180, 270]
    arrs = []
    for pair in pairs:
        for flip in flips:
            for spin in spins:
                # print(pair, flip, spin)
                r = R.from_euler(pair, [flip, spin], degrees=True)
                # print(r.as_euler('xyz', degrees=True))
                arr = np.array(np.round(r.apply(vec)), dtype=int)
                #if arr not in arrs:
                if str(arr) not in [str(x) for x in arrs]:
                    arrs.append(arr)
                # len(set([str(x) for x in res[0]]))
    return arrs

res = list(map(reorientor, tdat))








