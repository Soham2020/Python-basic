a = []
print("Enter the Array Element::")
for i in range(5):
	n = int(input())
	a.append(n)
a.sort()
print("Second Largest is :: ", a[-2])