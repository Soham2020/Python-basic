# floor
""" The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i where i <= x. """

# ceil
"""The tool ceil returns the ceiling of the input element-wise.
The ceiling of x is the smallest integer i where i >= x."""

# rint
# The rint tool rounds to the nearest integer of input element-wise.

# Task
# You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.

import numpy
a = numpy.array(input().split(),float)
numpy.set_printoptions(sign=' ')
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))