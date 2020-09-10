a = []
print("Enter the Array Element")
for i in range(5):
	n = int(input())
	a.append(n)
print("Array is :: ",a)
sum = 0
for i in a:
	sum = sum + i
print("Sum of Element is :: ", sum)