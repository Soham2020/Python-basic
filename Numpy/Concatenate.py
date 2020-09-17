# Concatenate
# Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined.
# If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. 
# By default, it is along the first dimension.

# Task
# You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

import numpy as np

n,m,p = map(int, input().split())

line = []
lines = []
for _ in range(n):
    line.append(list(map(int, input().split())))
for _ in range(m):
    lines.append(list(map(int, input().split())))

arr1 = np.array(line)
arr2 = np.array(lines)

print(np.concatenate((arr1, arr2),axis=0))