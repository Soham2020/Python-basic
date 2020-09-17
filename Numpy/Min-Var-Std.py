"""
mean
The mean tool computes the arithmetic mean along the specified axis.
By default, the axis is None. Therefore, it computes the mean of the flattened array.

var
The var tool computes the arithmetic variance along the specified axis.
By default, the axis is None. Therefore, it computes the variance of the flattened array.

std
The std tool computes the arithmetic standard deviation along the specified axis.
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.
"""

# Task
# You are given a 2-D array of size N X M.
# Your task is to find:
    # The mean along axis 1 
    # The var along axis 0
    # The std along axis none

import numpy
numpy.set_printoptions(legacy='1.13') #Optional
n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)],int)
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.std(arr))
