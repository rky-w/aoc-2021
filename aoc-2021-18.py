
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


td1 = [[1,1],[2,2],[3,3],[4,4]]
td2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]


def adder(dd):
    sm = dd[0]
    for d in dd[1:]:
        sm = [sm, d]
    return sm
  

def boom(orgdd, bdd):
    print("BOOM")
    lv = bdd[0]
    rv = bdd[1]
    co = str(orgdd)
    cb = str(bdd)
    coi = co.index(cb)
    lf = co[:coi]
    lo = boomadd(lf[::-1], lv)[::-1]
    rf = co[coi+len(cb):]
    ro = boomadd(rf, rv)
    return ast.literal_eval(lo + '0' + ro)    


def boomadd(s, v):
    res = re.finditer('\d+', s)
    try:
        m = res.__next__()
        o = s[:m.start()] + str(int(m.group()) + v) + s[m.end():]
        return o
    except:
        print("No matches found")
        return s


def _exploder(dd, lvl=0, pth=None, orgdd=None):
    if orgdd == None:
        orgdd = dd
    print(f"Entering exploder\n\tdd: {dd}\n\tlvl: {lvl}\n\tpth: {pth}")
    if pth == None:
        pth = []    
    if lvl == 4 and isinstance(dd, list):
        print(f"Explode dd: {orgdd}, Boom dd: {dd}")
        return boom(orgdd, dd)
    if isinstance(dd, list):
        lvl += 1
        for id in range(len(dd)):
            pth.append(id)
            res = _exploder(dd[id], lvl, pth, orgdd)
            print(f"RESULT: {res}")
            if res is not None:
                return res


def exploder(dd):
    while dd is not None:
        hd = dd
        dd = _exploder(dd)
    return hd


    if hd is None:
        hd = dd
    if dd 
    res = _exploder(dd)
    if dd is None:


    hd = dd
    _exploder(dd)




    