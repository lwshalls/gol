import math
import numpy
import random
"""Define binary states for alive status"""
DEAD = 0
ALIVE = 1


# Define inital empty board state
def initstate(width, height):
    return [[DEAD for _ in range(height)] for _ in range(width)]

def state_width(state):
   return len(state)

def state_length(state):
     return len(state[0])


