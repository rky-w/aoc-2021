
from aocd.models import Puzzle
import pandas as pd
from collections import Counter

puzzle = Puzzle(year=2021, day=12)
puzldat = [val for val in puzzle.input_data.splitlines()]

testdat = [
'start-A',
'start-b',
'A-c',
'A-b',
'b-d',
'A-end',
'b-end']

testdat2 = [
'dc-end',
'HN-start',
'start-kj',
'dc-start',
'dc-HN',
'LN-dc',
'HN-end',
'kj-sa',
'kj-HN',
'kj-dc']


testdat3 = [
'fs-end',
'he-DX',
'fs-he',
'start-DX',
'pj-DX',
'end-zg',
'zg-sl',
'zg-pj',
'pj-he',
'RW-he',
'fs-DX',
'pj-RW',
'zg-RW',
'start-pj',
'he-WI',
'zg-he',
'pj-fs',
'start-RW'
]



def cleaner(lst):
    return [it.split('-') for it in lst]

def solver(links, pt2=False):    
    sdf = pd.DataFrame({'l0': ['start']})
    results = []
    i = 0
    while i < 100:
        il = f"l{i}"
        i2 = f"l{i+1}"
        frms = list(sdf.iloc[:,i])

        # Find values in links to merge onto dataframe
        mg = pd.DataFrame({il: [], i2: []})
        for lk in links:
            for frm in set(frms):
                if frm in lk:
                    dest = list(set(lk) - set([frm]))[0]
                    mg = mg.append({il: frm, i2: dest}, ignore_index=True)
        sdf = pd.merge(sdf, mg, how='left', on=[il])

        # Keep only rows which do not return to smaller caves (or switch for pt 2 logic)
        keep = []
        for ls in sdf.values.tolist():
            cnts = Counter(ls)
            if pt2:
                keep.append(cnts['start'] == 1 and len([k for k, v in cnts.items() if v > 1 and k.islower()]) <= 1 and len([k for k, v in cnts.items() if v > 2 and k.islower()]) == 0)
            else:
                keep.append(len([k for k, v in cnts.items() if v > 1 and k.islower()])==0)
        sdf = sdf.loc[keep, :]           

        # Find and extract paths which reach the end
        ends = list(sdf[i2] == 'end')
        results.extend(sdf.loc[ends, :].values.tolist())
        sdf = sdf.loc[(not end for end in ends), :]

        i += 1
        if len(sdf) == 0:
            break
        
    return results

links = cleaner(puzldat)

# Pt 1. Answer
print(len(solver(links)))

# Pt 2. Answer
print(len(solver(links, pt2=True)))



