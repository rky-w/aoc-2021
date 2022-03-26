
import sys
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter
import numpy as np
import pandas as pd
import time
import math
import re
import ast

puzzle = Puzzle(year=2021, day=18)
puzldat = [ast.literal_eval(val) for val in puzzle.input_data.splitlines()]


td = [[1,1],[2,2],[3,3],[4,4]]

def adder(d):
    sm = [d[0]]
    for lst in d[1:]:
        sm = [sm, lst]
    return sm

adder(td)

