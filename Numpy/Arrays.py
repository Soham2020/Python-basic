"""
The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.

To use the NumPy module, we need to import it using:
import numpy

A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.
Task
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
"""

import numpy

def arrays(arr):
    a = numpy.array(arr[::-1],float)
    return(a)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)