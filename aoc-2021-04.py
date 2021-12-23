
from aocd.models import Puzzle
import pandas as pd
import numpy as np

puzzle = Puzzle(year=2021, day=4)
puzzle_data = [val for val in puzzle.input_data.splitlines()]

testnums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

testgrids=np.array([[
[22, 13, 17, 11,  0],
[ 8,  2, 23,  4, 24],
[21,  9, 14, 16,  7],
[ 6, 10,  3, 18,  5],
[ 1, 12, 20, 15, 19]],

[[3, 15,  0,  2, 22],
[ 9, 18, 13, 17,  5],
[19,  8,  7, 25, 23],
[20, 11, 10, 24,  4],
[14, 21, 16, 12,  6]],

[[14, 21, 17, 24,  4],
[10, 16, 15,  9, 19],
[18,  8, 23, 26, 20],
[22, 11, 13,  6,  5],
[ 2,  0, 12,  3,  7]]])


class Bingo:
    
    def __init__(self, numbers, grids):
        self.numbers = numbers.copy()
        self.grids = grids.copy()
        self.scores = []
        self.ignore = []

    def marker(self, number):
        for grid in self.grids:
            if number in grid:
                grid[grid == number] = -1
                
    def checker(self):
        winners = []
        for i in range(self.grids.shape[0]):
            if i not in self.ignore:
                boolgrid = ~(self.grids[i] >= 0)
                if any(boolgrid.sum(axis=0) == 5) | any(boolgrid.sum(axis=1) == 5):
                    winners.append(i)
                    self.ignore.append(i)
        if len(winners) > 0:
            return winners
        else:
            return None
            
    def scorer(self, winners, number):
        scores = []
        for winner in winners:
            wingrid = self.grids[winner]
            scores.append(wingrid[wingrid >= 0].sum() * number)
        return scores
    
    def play(self):        
        for number in self.numbers:
            self.marker(number)
            winners = self.checker()
            if winners is not None:
                return self.scorer(winners, number)
    
    def play_to_lose(self):
        for number in self.numbers:
            self.marker(number)
            winners = self.checker()
            if winners is not None:
                self.scores.append(self.scorer(winners, number))
        return self.scores[-1]


# Prepare submission data
rawnums = puzzle_data[0].split(',')
nums = [int(num) for num in rawnums]

rawgrid = puzzle_data[2:]
listgrid = []
tmpgrid = []
for i in range(len(rawgrid)):
    line = rawgrid[i]
    if line == '':
        listgrid.append(tmpgrid)
        tmpgrid = []        
    else:
        tmpgrid.append(line.split())
    
grids = np.array(listgrid).astype(int)


# Pt 1. Play bingo!              
bing = Bingo(nums, grids)
res = bing.play()
print(res)

# Pt 2. Let the squid win!
losebing = Bingo(nums, grids)
loseres = losebing.play_to_lose()
print(loseres)





