
from aocd.models import Puzzle
import pandas as pd
import numpy as np

puzzle = Puzzle(year=2021, day=3)
puzzle_data = [val for val in puzzle.input_data.splitlines()]

"""
gamma_rate = most common bit for each position
epsilon_rate = inverse of gamma_rate

power_rate = dec(gamma_rate) * dec(epsilon_rate)
"""

testdat = [
'00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010'
]

def arrayariser(lst):
    return np.array([list(string) for string in lst]).astype(int)


def boolariser(arr):
    gammabool = arr.sum(axis=0) / arr.shape[0] >= .5
    epsbool = ~gammabool
    return gammabool, epsbool


def decimaliser(arr):
    return int("".join(arr.astype(str).tolist()), 2)


def diagnostics(binin):
    
    arr = arrayariser(binin)    
    
    gammabool, epsbool = boolariser(arr)
    
    gammabin = gammabool.astype(int)
    epsbin = epsbool.astype(int)
    
    gamma = decimaliser(gammabin)
    epsilon = decimaliser(epsbin)
            
    return gamma * epsilon

# Pt 1.
print(diagnostics(puzzle_data))


class DiagnosticRecurse:
    def __init__(self, length=0):
        self.seq = []
        self.maxlen = length
    
    def recurseriser(self, arr, posdir):
        self.maxlen = max(self.maxlen, arr.shape[1])
        posinit, neginit = boolariser(arr)
        val = int(posinit[0] if posdir else neginit[0])
        self.seq.append(val)
        newarr = arr[arr[:, 0] == val, 1:]
        if newarr.shape[0] > 1:
            return self.recurseriser(newarr, posdir)
        else:
            if len(self.seq) != self.maxlen:
                self.seq = self.seq + newarr.tolist()[0]
            return None    


def more_diagnostics(binin):
    arr = arrayariser(binin)
    
    prec = DiagnosticRecurse()
    prec.recurseriser(arr, True)
    
    nrec = DiagnosticRecurse()
    nrec.recurseriser(arr, False)
    
    o2val = decimaliser(np.array(prec.seq))
    c02val = decimaliser(np.array(nrec.seq))
        
    return o2val * c02val

# Pt 2.
print(more_diagnostics(puzzle_data))
