# Basic mathematical functions operate element-wise on arrays. 
# They are available both as operator overloads and as functions in the NumPy module.

# Task
# You are given two integer arrays,  and  of dimensions X.
# Your task is to perform the following operations:
"""Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)"""

import numpy as np
n,m = map(int,input().split())

a=np.zeros((n,m),int)
b=np.zeros((n,m),int)

for i in range(n):
  a[i]=np.array(input().split(),int)
for i in range(n):
  b[i]=np.array(input().split(),int)  

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)