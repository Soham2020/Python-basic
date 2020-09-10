a = []
print("Enter the Array elements::")
for i in range(5):
	n = int(input())
	a.append(n)
print("Given Array is :: ", a)
count = 0
for i in a:
	count = count + 1
print("Total elements in the Array is ::", count)