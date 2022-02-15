
import sys
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


# Brute force recursion approach works but would take too long
arr = getarr(testdat)

start = (0, 0)
ncs = [(1, 0), (0, 1), (0, -1), (-1, 0)] 

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

    for nxt in nxts:
        cost.append(arr[nxt])
        pather(nxt, deepcopy(seen), deepcopy(cost))
        cost.pop()

pather(start)
min(costs)



# Initialise cost for first row and column, then find minimum for interior cells
arr = getarr(puzldat)
nar = deepcopy(arr)
nar[0, 0] = 0

for i in range(1, nar.shape[0]):
    nar[i, 0] += nar[i-1, 0]

for j in range(1, nar.shape[1]):
    nar[0, j] += nar[0, j-1]

for y in range(1, nar.shape[0]):
    for x in range(1, nar.shape[1]):
        nar[x, y] = nar[x, y] + min(nar[x, y-1], nar[x-1, y])

# Incorrect result as paths can only go down and right
print(nar[nar.shape[0]-1, nar.shape[1]-1]-nar[0,0])



# Implementation of Dijkstra's algorithm
def grapher(array):
    nodes = []
    coords = []
    revcoords = []
    costs = [] 
    edges = []

    node = 0
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            nodes.append(node)
            coords.append((x, y))
            costs.append(array[x, y])
            node += 1

    revcoords = dict(zip(coords, nodes))
    
    tsts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for node in nodes:
        _edges = set()
        for tst in tsts:
            nc = tuple(map(sum, zip(coords[node], tst)))
            if nc in revcoords.keys():
                _edges.add(revcoords[nc])
        edges.append(_edges)

    Graph = {
        'nodes': nodes,
        'coords': coords,
        'revcoords': revcoords,
        'costs': costs,
        'edges': edges,
        'array': array
    }

    return Graph


def dijkstra(graph):

    Q = set(graph['nodes'])
    dist = defaultdict(lambda: np.inf)
    dist[0] = 0

    end = max(graph['nodes'])

    while Q:        
        newdist = {q: dist[q] for q in Q}
        u = min(newdist, key=newdist.get)
        Q.remove(u)

        cn = Q.intersection(graph['edges'][u])
        if end in cn:
            return dist[u] + graph['costs'][end]

        for v in Q.intersection(graph['edges'][u]):
            alt = dist[u] + graph['costs'][v]
            if alt < dist[v]:
                dist[v] = alt

    return dist[len(dist)-1]

arr = getarr(testdat)

# Pt 1. Answer
print(dijkstra(grapher(arr)))



# Pt 2. Is 5 times larger, may need to speed up the above implementation

def _adder(el, times = 1):
    return ((el + times - 1) % 9) + 1
adder = np.vectorize(_adder)

def mplyer(arr, factor=5, **kwargs):
    for i in range(factor):
        if i == 0:
            oarr = arr
        else:
            oarr = np.concatenate([oarr, adder(arr, times=i)], **kwargs)
    return oarr


arr = getarr(puzldat)
newarr = mplyer(mplyer(arr, axis=1), axis=0)

print(dijkstra(grapher(newarr)))