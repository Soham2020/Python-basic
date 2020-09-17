# Identity
# he identity tool returns an identity array. 
# An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0. 
# The default type of elements is float.

# Eye
# The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, 
# upper or lower depending on the optional parameter k. A positive k is for the upper diagonal, a negative k is for the lower, 
# and a 0k (default) is for the main diagonal.

# Task
# Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.

import numpy as np

n,m  = map(int, input().split())
np.set_printoptions(sign=' ')
print(np.eye(n, m, k=0))