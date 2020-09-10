a = []
b = int(input("Enter the Array Size::"))
print("Enter the Array Elements::")
for i in range(b):
	n = int(input())
	a.append(n)
a.sort()
l = int(input("Enter the Nth largest Elements::"))
print("Largest Number is :: ", a[-l])