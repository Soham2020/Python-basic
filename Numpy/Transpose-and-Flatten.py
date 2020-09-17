# Transpose
# We can generate the transposition of an array using the tool numpy.transpose.
# It will not affect the original array, but it will create a new array.

# Flatten
# The tool flatten creates a copy of the input array flattened to one dimension.

# Task
# You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

import numpy 

# Input From User
n, m = map(int, input().split())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

# Output
my_arr = numpy.array(lines)
print(numpy.transpose(my_arr))
print(my_arr.flatten())