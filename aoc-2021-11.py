import numpy as np  
import copy
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=11)
puzldat = [val for val in puzzle.input_data.splitlines()]

testdat = [
'5483143223',
'2745854711',
'5264556173',
'6141336146',
'6357385478',
'4167524645',
'2176841721',
'6882881134',
'4846848554',
'5283751526'
]

def cleaner(lst):
    return np.array([list(line) for line in lst], dtype=int)

class Octopi:
    def __init__(self, octopi):
        self.octopi = copy.deepcopy(octopi)
        self.flashes = 0
        self.flashed = np.zeros(octopi.shape, dtype=bool)

    def stepper(self):
        self.octopi += 1
        self.flashes += self.flasher()
        self.octopi[self.octopi > 9] = 0
        self.flashed = np.zeros(self.octopi.shape, dtype=bool)
        return self.flashes
    
    def steptimes(self, times=1):
        for i in range(times):
            self.stepper()
        return self.flashes        
        
    def flasher(self):
        flashers = (~self.flashed) & (self.octopi > 9)
        if flashers.sum() > 0:
            self.flashed = self.flashed | flashers
            self.adder(flashers)
            return self.flasher()
        else:
            return self.flashed.sum()

    def adder(self, flashers):
        circ = [(-1,0), # N
                (-1,1), # NE
                (0,1),  # E
                (1,1),  # SE
                (1,0),  # S
                (1,-1), # SW
                (0,-1), # W
                (-1,-1)] # NW
        for coord in zip(*np.where(flashers)):
            for rev in circ:
                pos = tuple(map(sum, zip(coord, rev)))
                if 0 <= pos[0] < self.octopi.shape[0] and 0 <= pos[1] < self.octopi.shape[1]:
                    self.octopi[pos] += 1
    
    def findsync(self):
        i = 0
        while self.octopi.sum() != 0:
            i += 1
            self.stepper()
        return i
    
octopi = cleaner(puzldat)

# Pt 1. Answer
dumbos = Octopi(octopi)
dumbos.steptimes(100)

# Pt 2. Answer
dumbos2 = Octopi(octopi)
dumbos2.findsync()
