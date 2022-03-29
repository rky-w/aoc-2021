
from resource import RLIMIT_FSIZE
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

puzzle = Puzzle(year=2021, day=18)
puzldat = [ast.literal_eval(val) for val in puzzle.input_data.splitlines()]


def boom(orgdd, bdd):
    c = len(str(orgdd))
    seg = orgdd
    for p in bdd:
        p = int(p)
        orgseg = seg
        seg = seg[p]
        if p == 0:
            c -= (len(str(orgseg[1]))+3)
        if p == 1:
            c -= 1
    lg = re.match('^.*(\[\d+, \d+\])$', str(orgdd)[:c])[1]
    lgl = ast.literal_eval(lg)
    lv = lgl[0]
    rv = lgl[1]
    co = str(orgdd)
    lf = co[:(c - len(lg))]
    lo = boomadd(lf, lv, drc='l')
    rf = co[c:]
    ro = boomadd(rf, rv, drc='r')
    return ast.literal_eval(lo + '0' + ro)    


def boomadd(s, v, drc = 'r'):
    res = re.finditer('\d+', s)
    lsr = [r for r in res]
    if len(lsr):
        if drc=='r':
            m = lsr[0]
        else:
            m = lsr[-1]
        o = s[:m.start()] + str(int(m.group()) + v) + s[m.end():]
        return o
    else:
        return s


def _exploder(dd, entry=None, lvl=0, pth='', orgdd=None):
    # print(f"Entering\n\tlvl: {lvl}\n\tdd: {dd}")
    if entry != None:
        pth += str(entry)
    if orgdd == None:
        orgdd = dd
    if lvl == 4 and isinstance(dd, list):
        # print(f"Exploding\n\tdd: {dd}\n\tpth: {pth}")
        return boom(orgdd, pth)
    if isinstance(dd, list):
        lvl += 1
        for id in range(len(dd)):
            res = _exploder(dd[id], id, lvl, pth, orgdd)
            if res is not None:
                return res


def exploder(dd):
    r = _exploder(dd)
    if r is None:
        return dd
    else:
        return r


def splitter(dd):
    cd = str(dd)
    sv = [v for v in re.sub('[\[\]\s]', '', cd).split(',') if int(v) > 9]
    if len(sv):    
        coi = cd.index(sv[0])
        lf = cd[:coi]
        rf = cd[coi+len(sv[0]):]
        r = int(sv[0]) / 2
        o = lf + f"[{math.floor(r)}, {math.ceil(r)}]" + rf
        return ast.literal_eval(o)
    else: 
        return dd


def reducer(dd):
    hd = dd
    dd = exploder(dd)
    # print(f"EXPLODER OUTPUT: {dd}")
    if dd != hd:
        return reducer(dd)
    dd = splitter(dd)
    # print(f"SPLITTER OUTPUT: {dd}")
    if dd != hd:
        return reducer(dd)
    return dd


def adder(dd):
    sm = dd[0]
    for d in dd[1:]:
        # print(f"ADDER INPUT:\n\tL: {sm}\n\tR: {d}")
        sm = [sm, d]
        # print(f"ADDER OUTPUT:\n\t{sm}")
        sm = reducer(sm)
    return sm


def magnitude(sm):
    if isinstance(sm, int):
        return sm
    else:
        return 3 * magnitude(sm[0]) + 2 * magnitude(sm[1])


# Pt 1. Answer
magnitude(adder(puzldat))


# Pt 2. Largest magnitude
max(magnitude(adder([x, y])) for x, y in itertools.permutations(puzldat, 2))



