
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




