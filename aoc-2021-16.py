
import sys
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict, Counter
import numpy as np
import pandas as pd
import time


puzzle = Puzzle(year=2021, day=16)
puzldat = [val for val in puzzle.input_data.splitlines()]
