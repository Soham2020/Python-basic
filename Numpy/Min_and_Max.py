"""
min
The tool min returns the minimum value along a given axis.
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

max
The tool max returns the maximum value along a given axis.
"""

# Task
# You are given a 2-D array with dimensions N X M.
# Your task is to perform the min function over axis 1 and then find the max of that.

import numpy as np
n,m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)],int)
print(np.max(np.min(arr,axis=1)))