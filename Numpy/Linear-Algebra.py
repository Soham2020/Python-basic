# The NumPy module also comes with a number of built-in routines for linear algebra calculations. 
# These can be found in the sub-module linalg.

# More Reference : https://www.geeksforgeeks.org/numpy-linear-algebra/

# Task
# You are given a square matrix A with dimensions N X N. Your task is to find the determinant. 
# Note: Round the answer to 2 places after the decimal.

import numpy
n = int(input()) 
A = numpy.array([input().split() for _ in range(n)], float) 
print(round(numpy.linalg.det(A),2))