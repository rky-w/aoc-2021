
from resource import RLIMIT_FSIZE
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
td = [[1,1],[2,2],[3,3],[4,4], [5,5]]


def adder(dd):
    sm = dd[0]
    for d in dd[1:]:
        sm = [sm, d]
    return sm

dd = adder(td)


def exploder(dd, lvl=0, pth=None, orgdd=None):
    if orgdd == None:
        orgdd = dd
    print(f"Entering exploder\n\tdd: {dd}\n\tlvl: {lvl}\n\tpth: {pth}")
    if pth == None:
        pth = []
    if isinstance(dd[0], int) and isinstance(dd[1], int):
        print(f"Terminal\n\tdd: {dd}\n\tlvl: {lvl}\n\tpth: {pth}")
        # return
    lvl += 1
    if lvl == 4:
        print(f"Explode:\n\tdd: {dd[0]}\n\tlvl: {lvl}\n\tpth: {pth + [0]}")
        print(f"Original dd: {orgdd}")
        return "boom"
    for id in range(len(dd)):
        pth.append(id)
        return exploder(dd[id], lvl, pth, orgdd)
            
exploder(dd)
bdd = dd[0][0][0][0]
orgdd = dd

def boom(orgdd, bdd):
    lv = bdd[0]
    rv = bdd[1]
    co = str(orgdd)
    cb = str(bdd)

    coi = co.index(cb)
    
    lf = co[:coi]
    rlf = lf[::-1]
    boomadd(rlf, lv)


    rf = co[coi+len(cb):]
   

    lf + cb + rf
    co

def boomadd(s, v):
    res = re.finditer('\d+', s)
    try:
        m = res.__next__()
        o = s[:m.start()] + str(int(m.group()) + v) + s[m.end():]
        return o
    except:
        print("No matches found")
        return s
    


    