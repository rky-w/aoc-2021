
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


def h2b(hex):
    return ''.join([hexbin[h] for h in hex])    

def ver(bin):
    return int(bin[:3], 2)

def typ(bin):
    return int(bin[3:6], 2)

def litval(bin):
    lv = bin[7:]
    vl = ''
    while True:
        cont = lv[0]
        vl.join(lv)
        
    pass

h2b('D2FE28')
ver(h2b('D2FE28'))
typ(h2b('D2FE28'))

