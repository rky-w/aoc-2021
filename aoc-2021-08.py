
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=8)
puzzle_data = [val for val in puzzle.input_data.splitlines()]

testdat = [
'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
]

testdat

def parser(lst):
    inout = [[seg.split(' ') for seg in row.split(' | ')] for row in lst]
    return inout

streams = parser(puzzle_data)


def getlens(streams, pos=1):
    lens = []
    for stream in streams:
        lens.append([len(digit) for digit in stream[pos]])
    return lens

output_lens = getlens(streams)

# Pt 1.
len([var for len in output_lens for var in len if var in [2, 3, 4, 7]])


# Pt 2.

def solver(streams):
    inlens = getlens(streams, pos=0)
    output_sum = 0
    for i in range(len(streams)):
        input = [frozenset(dig) for dig in streams[i][0]]
        lens  = inlens[i]

        digs21 = [i for (i, l) in zip(input, lens) if l == 2][0]
        digs37 = [i for (i, l) in zip(input, lens) if l == 3][0]
        digs44 = [i for (i, l) in zip(input, lens) if l == 4][0]
        digs5 = [i for (i, l) in zip(input, lens) if l == 5]
        digs6 = [i for (i, l) in zip(input, lens) if l == 6]
        digs78 = [i for (i, l) in zip(input, lens) if l == 7][0]

        digs69 = [digs for digs in digs6 if (digs37 | digs44) < digs][0] 
        digs60 = [digs for digs in digs6 if digs != digs69 and digs21 < digs][0]
        digs66 = [digs for digs in digs6 if digs != digs69 and digs != digs60][0]
        digs53 = [digs for digs in digs5 if digs21 < digs][0]
        digs52 = [digs for digs in digs5 if digs != digs53 and (digs78 - digs69) < digs][0]
        digs55 = [digs for digs in digs5 if digs != digs53 and digs != digs52][0]

        digdict = {digs60: 0, digs21: 1, digs52: 2, digs53: 3, digs44: 4, digs55: 5, digs66: 6, digs37: 7, digs78: 8, digs69: 9}

        output = int("".join([str(digdict[frozenset(dig)]) for dig in streams[i][1]]))
        output_sum += output
    return output_sum
        
solver(streams)

