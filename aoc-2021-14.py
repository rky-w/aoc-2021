
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter

puzzle = Puzzle(year=2021, day=14)
puzldat = [val for val in puzzle.input_data.splitlines()]

testdat = [
'NNCB',
'',
'CH -> B',
'HH -> N',
'CB -> H',
'NH -> C',
'HB -> C',
'HC -> B',
'HN -> C',
'NN -> C',
'BH -> H',
'NC -> B',
'NB -> B',
'BN -> B',
'BB -> N',
'BC -> B',
'CC -> N',
'CN -> C'
]


def datparser(input):
    pt = input[0]
    ir = defaultdict(str, [x.split(' -> ') for x in input[2:]])
    return pt, ir
    
def inserter(pt, ir):
    pm = list(pt)
    j = 1
    for i in range(len(pt)-1):
        x = ir[pt[i] + pt[i+1]]
        if x != '':
            pm.insert(i+j, x)
            j += 1
    return ''.join(pm)

def repeater(pt, ir, times=1):
    pm = deepcopy(pt)
    for t in range(times):
        pm = inserter(pm, ir)
    return pm


pt, ir = datparser(puzldat)
chain = repeater(pt, ir, times=10)

ct = Counter(chain)

# Pt 1. Answer
print(max(ct.values()) - min(ct.values()))


# Pt 2. New approach must be more efficient

iir = {k: [k[0]+v, v+k[1]] for k, v in ir.items()}

nd = Counter()
for i in range(len(pt)-1):
    nd[pt[i]+pt[i+1]] += 1

els = Counter(pt)

for xi in range(40):
    n2 = deepcopy(nd)
    for k, v in n2.items():
        if v > 0:
            els[ir[k]] += v
            for ii in iir[k]:
                nd[ii] += v
            nd[k] -= v

print(max(els.values()) - min(els.values())) 
