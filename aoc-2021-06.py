
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=6)
puzzle_data = [val for val in puzzle.input_data.splitlines()]
puzzle_fish = [int(val) for val in puzzle_data[0].split(',')]

testfish = [3,4,3,1,2]


class LanternFish:
    def __init__(self, age=8):
        self.age = age

    def grow(self):
        if self.age > 0:
            self.age -= 1
        else:
            self.age = 6
            return self.spawn()
    
    def spawn(self):
        return LanternFish()


class School:
    def __init__(self, fishages=[8]):
        self.day = 0
        self.population = []
        for fishage in fishages:
            self.population.append(LanternFish(fishage))

    def passday(self):
        popsize = len(self.population)
        for fishi in range(popsize):
            baby = self.population[fishi].grow()
            if baby != None:
                self.population.append(baby)
        self.day += 1

    def passdays(self, days=1):
        for i in range(days):
            self.passday()
    
    def ages(self):
        return [fish.age for fish in self.population]

    def popsize(self):
        return len(self.population)

# Pt 1. Stimulating lanternfish
sch = School(puzzle_fish)
sch.passdays(80)
sch.popsize()


# Pt 2. Stimulating lanternfish... forever!

class Fishes:
    """"More efficient approach"""
    def __init__(self, ages=[]):
        self.pop = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        for age in ages:
            self.pop[age] += 1
    
    def grow(self):
        spawns = self.pop[0]
        for i in range(1, 9):
            self.pop[i-1] = self.pop[i]
        self.pop[6] = self.pop[6] + spawns
        self.pop[8] = spawns
    
    def passdays(self, days=1):
        for day in range(days):
            self.grow()

    def popsize(self):
        return sum(list(self.pop.values()))

bigsch = Fishes(puzzle_fish)
bigsch.passdays(256)
bigsch.popsize()

