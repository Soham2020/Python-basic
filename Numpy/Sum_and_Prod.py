# sum
# The sum tool returns the sum of array elements over a given axis.

# prod
# The prod tool returns the product of array elements over a given axis.

# Task
# You are given a 2-D array with dimensions X.
# Your task is to perform the sum tool over axis 0 and then find the product of that result.

import numpy
n,m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)],int)
print(numpy.prod(numpy.sum(arr, axis=0)))