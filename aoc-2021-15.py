
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter
import numpy as np
import pandas as pd

puzzle = Puzzle(year=2021, day=15)
puzldat = [val for val in puzzle.input_data.splitlines()]

testdat = [
    '1163751742',
    '1381373672',
    '2136511328',
    '3694931569',
    '7463417111',
    '1319128137',
    '1359912421',
    '3125421639',
    '1293138521',
    '2311944581'
]

def getarr(lst):
    return np.array([list(x) for x in lst], dtype=int)

arr = getarr(puzldat)
arr = arr[0:3, 0:3]

start = (0, 0)
seen = []
ncs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def pather(start, seen=None):
    print(f"Starting with start={start}")
    if seen == None:
        seen = []
    if start == (arr.shape[0]-1, arr.shape[1]-1):
        print(f"Terminal reached")
        return arr[start]

    seen.append(start)
    chklst = []
    for nc in ncs:
        nl = tuple([sum(x) for x in zip(start, nc)])
        if 0 <= nl[0] <= arr.shape[0]-1 and 0 <= nl[1] <= arr.shape[1]-1 and nl not in seen:
            chklst.append(nl)
    nxts = [x for x in chklst if arr[x] == min([arr[x] for x in chklst])]

    for nxt in nxts:
        return arr[start] + pather(nxt, deepcopy(seen))


pather(start)




costs = []
def pather(start, seen=None, cost=None):
    if cost == None:
        cost = []
    # print(f"Starting with start={start}, val={arr[start]}, cost={cost}")
    if seen == None:
        seen = []
    if len(costs) > 0 and sum(cost) > min(costs):
        return    
    if start == (arr.shape[0]-1, arr.shape[1]-1):
        costs.append(sum(cost))
        # print(f"Terminal reached:\n\tPath: {cost}\n\tCost: {sum(cost)}")
        return

    seen.append(start)
    chklst = []
    for nc in ncs:
        nl = tuple([sum(x) for x in zip(start, nc)])
        if 0 <= nl[0] <= arr.shape[0]-1 and 0 <= nl[1] <= arr.shape[1]-1 and nl not in seen:
            chklst.append(nl)
    # nxts = [x for x in chklst if arr[x] == min([arr[x] for x in chklst])]
    nxts = chklst
    
    arr

    for nxt in nxts:
        cost.append(arr[nxt])
        pather(nxt, deepcopy(seen), deepcopy(cost))
        cost.pop()

pather(start)
min(costs)
costs

