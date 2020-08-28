# Fibonacci Series

a = 0
b = 1

n = int(input("Enter The Number of Terms : "))

print("FIBONACCI SERIES")

print(a," ",b,end="")

for i in range(n):
    c = a + b
    a = b
    b = c
    print(" ",c,end="") 