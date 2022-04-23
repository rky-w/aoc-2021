
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


pairs = ['zx', 'xy', 'yz']
flips = [0, 180]
spins = [0, 90, 180, 270]

for pair in pairs:
    for flip in flips:
        for spin in spins:
            print(pair, flip, spin)
            r = R.from_euler(pair, [flip, spin], degrees=True)
            print(r.as_euler('xyz', degrees=True))





