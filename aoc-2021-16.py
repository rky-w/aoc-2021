
import sys
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter
import numpy as np
import pandas as pd
import time

puzzle = Puzzle(year=2021, day=16)
puzldat = [val for val in puzzle.input_data.splitlines()]

hexbin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def h2b(hex) -> list:
    return [v for h in hex for v in hexbin[h]]

def header(p) -> tuple:
    v = int(''.join([p.pop(0) for i in range(3)]), 2)
    t = int(''.join([p.pop(0) for i in range(3)]), 2)
    return v, t

def litval(p) -> int:
    l = []
    while True:
        l.extend([p.pop(1) for i in range(4)])
        if not int(p.pop(0)):
            break
    return int(''.join(l), 2)

   
def reader(pk, debug=False):
    global versum
    pv, pt = header(pk)
    versum += pv
    if debug: print("\n---------------------------------------------------------------------")
    if debug: print(f"New reader. pv: {pv}, pt: {pt}, versum: {versum}, pk:\n   {''.join(pk)}")
    if pt == 4:
        lv = litval(pk)
        if debug: print(f"Litval hit: {lv}")
        return
    else:
        if int(pk.pop(0)):
            pkn = int(''.join([pk.pop(0) for i in range(11)]), 2)
            if debug: print(f"Operator[1] pkn: {pkn}")
            while pkn:
                if debug: print(f"op1 loopstart, pk:\n   {''.join(pk)}")
                reader(pk)
                pkn -= 1
                if debug: print(f"op1 loopend, pk:\n   {''.join(pk)}")
            if debug: print(f"Exiting op1, pk:\n   {''.join(pk)}")
        else:
            pkl = int(''.join([pk.pop(0) for i in range(15)]), 2)
            if debug: print(f"Operator[0] pkl: {pkl}, pk:\n   {''.join(pk)}")
            while pkl:
                pklh = len(pk)
                if debug: print(f"op0 loopstart, pk:\n   {''.join(pk)}")
                reader(pk)
                pkln = len(pk)
                pkl -= pklh - pkln
                if debug: print(f"op0 loopend, pk:\n   {''.join(pk)}")
            if debug: print(f"Exiting op0, pk: \n   {''.join(pk)}")
    return


veradd = 0
for packet in puzldat:
    versum = 0
    pk = h2b(packet)
    reader(pk)
    veradd += versum
veradd

print(f"Pt 1. Answer: {veradd}")


