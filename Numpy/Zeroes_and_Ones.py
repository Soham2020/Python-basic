# zeros
# The zeros tool returns a new array with a given shape and type filled with 0's.

# Ones
# The ones tool returns a new array with a given shape and type filled with 1's.

# Task
# You are given the shape of the array in the form of space-separated integers, 
# each integer representing the size of different dimensions, your task is to 
# print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

import numpy as np

dim = tuple(map(int, input().split()))

print (np.zeros(dim, dtype = np.int))
print (np.ones(dim, dtype = np.int))