# Program to Check Whether A Number is Perfect Square or Not

import math

n = int(input("Enter A Number : "))
root = int(math.sqrt(n))

if root*root == n:
    print("Perfect Square")
else:
    print("Not a Perfect Square")