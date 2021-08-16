import math
import numpy

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

def ranstate():
    a = initstate(4,4)

 # TODO: randomize each element of `state`
a = initstate(4,7)
b = state_width(a), state_length(a)
print(a, b)

