
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


def boom(orgdd, bdd):
    lv = bdd[0]
    rv = bdd[1]
    co = str(orgdd)
    cb = str(bdd)
    coi = co.index(cb)
    lf = co[:coi]
    lo = boomadd(lf, lv, drc='l')
    rf = co[coi+len(cb):]
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


def _exploder(dd, lvl=0, pth=None, orgdd=None):
    if orgdd == None:
        orgdd = dd
    if pth == None:
        pth = []    
    if lvl == 4 and isinstance(dd, list):
        return boom(orgdd, dd)
    if isinstance(dd, list):
        lvl += 1
        for id in range(len(dd)):
            pth.append(id)
            res = _exploder(dd[id], lvl, pth, orgdd)
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
        sv = [11]
        r = int(sv[0]) / 2
        o = lf + f"[{math.floor(r)}, {math.ceil(r)}]" + rf
        return ast.literal_eval(o)
    else: 
        return dd


def reducer(dd):
    hd = dd
    dd = exploder(dd)
    if dd != hd:
        return reducer(dd)
    dd = splitter(dd)
    if dd != hd:
        return reducer(dd)
    return dd


def adder(dd):
    sm = dd[0]
    for d in dd[1:]:
        sm = [sm, d]
        sm = reducer(sm)
    return sm


td = [[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]]

td = [[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
[7,[5,[[3,8],[1,4]]]],
[[2,[2,2]],[8,[8,1]]],
[2,9],
[1,[[[9,3],9],[[9,0],[0,7]]]],
[[[5,[7,4]],7],1],
[[[[4,2],2],6],[8,7]]]

adder(td)
adder(td[:2])

"""
  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
"""
adder([[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]], [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]])
# [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
"""
  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
"""

adder([[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
])
#[[[6, 5], [[6, 5], [5, 6]]], [[6, [6, 6]], [[7, 0], [7, 8]]]]

reducer([[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]], [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]])

reducer