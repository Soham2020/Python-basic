a = []
print("Enter the Elements::")
for i in range(0,5):
	n = int(input())
	a.append(n)
print("Original Array is :: ", a)
p = int(input("Enter the address to be swapped::"))
q = int(input("Enter the address to be swapped::"))
swap = a[p]
a[p] = a[q]
a[q] = swap
print("New Array is :: ", a)