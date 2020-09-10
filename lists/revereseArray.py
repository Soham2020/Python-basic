a = []
print("Enter the Array Element::")
for i in range(5):
	n = int(input())
	a.append(n)
print("Original Array is :: ", a)
b = a[::-1]
print(b)