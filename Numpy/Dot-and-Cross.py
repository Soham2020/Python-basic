"""
dot
The dot tool returns the dot product of two arrays.

cross
The cross tool returns the cross product of two arrays.
"""

# Task
# You are given two arrays A and B. Both have dimensions of N X M.
# Your task is to compute their matrix product.

import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)],int)
b = np.array([input().split() for _ in range(n)],int)

print(np.dot(a,b))