
from aocd.models import Puzzle
import pandas as pd

puzzle = Puzzle(year=2021, day=2)
puzzle_data = [val for val in puzzle.input_data.splitlines()]

test_dat = [
'forward 5',
'down 5',
'forward 8',
'up 3',
'down 8',
'forward 2']

def mover(instructions):
    moves = pd.Series(instructions).str.split(expand=True)
    moves.columns = ['direction', 'magnitude']
    moves['magnitude'] = moves['magnitude'].astype(int)

    smry = moves.groupby('direction', as_index=False).sum('magnitude')

    horiz = 0
    depth = 0

    for i in range(len(smry)):
        if smry.iloc[i,0] == 'forward':
            horiz = smry.iloc[i,1]
        elif smry.iloc[i,0] == 'down':
            depth += smry.iloc[i,1]
        elif smry.iloc[i,0] == 'up':
            depth -= smry.iloc[i,1]
    
    bearings = (horiz, depth)
    return bearings[0] * bearings[1]


class Mover:
    def __init__(self):
        self.aim = 0
        self.horiz = 0
        self.depth = 0
        
    def reader(self, instructions):
        for line in instructions:
            (direction, _magnitude) = line.split()
            magnitude = int(_magnitude)
            
            if direction == 'forward':
                self.horiz += magnitude
                self.depth += self.aim * magnitude
            elif direction == 'down':
                self.aim += magnitude
            elif direction == 'up':
                self.aim -= magnitude
                
    def multval(self):
        return self.horiz * self.depth
            
           
           
           
sub = Mover()

sub.reader(puzzle_data)

# Pt 2. 
print(sub.multval())



    
    


