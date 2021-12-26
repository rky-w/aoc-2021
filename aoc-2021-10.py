import statistics
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=10)
puzzle_data = [val for val in puzzle.input_data.splitlines()]

testdat = [
'[({(<(())[]>[[{[]{<()<>>',
'[(()[<>])]({[<{<<[]>>(',
'{([(<{}[<>[]}>{[]{[(<()>',
'(((({<>}<{<{<>}{[]{[]{}',
'[[<[([]))<([[{}[[()]]]',
'[{[{({}]{}}([{[{{{}}([]',
'{<[[]]>}<{[{[{[]{()[[[]',
'[<(<(<(<{}))><([]([]()',
'<{([([[(<>()){}]>(<<{{',
'<{([{{}}[<[[[<>{}]]]>[]]'
]

def stripper(line):
    # line = testdat[2]
    lb = ['(', '[', '{', '<']
    rb = [')', ']', '}', '>']
    lm = dict(zip(lb, rb))
    ll = list(line)
    # print(''.join(line))
    for i in range(len(ll)-1):
        # print(f"{i}: {ll[i]}")
        # print(''.join(ll))
        if lm[ll[i]] == ll[i+1]:
            nl = [ll[j] for j in range(len(ll)) if j not in [i, i+1]]
            return stripper(nl)
        elif ll[i+1] in rb:
            # print(f"Reached terminal: {i}: {ll[i]}")
            return ll[i+1], 'corrupted'
    return ''.join(line), 'incomplete'


pts = {')': 3, ']': 57, '}': 1197, '>': 25137}
pts2 = {'(': 1, '[': 2, '{': 3, '<': 4}

score_pt1 = 0
scores_pt2 = []
for line in puzzle_data:
    s2 = 0
    rv, st = stripper(line)
    if st != 'incomplete':
        score_pt1 += pts[rv]
    else:
        for x in rv[::-1]:
            s2 = (s2 * 5) + pts2[x]
        scores_pt2.append(s2)

print(f"Pt 1. Answer: {score_pt1}")

print(f"Pt 2. Answer: {statistics.median(scores_pt2)}")

