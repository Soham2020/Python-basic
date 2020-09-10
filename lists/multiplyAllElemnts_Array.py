a = []
print("Enter the Array Elements::")
for i in range(5):
	n = int(input())
	a.append(n)
p = 1
for i in a:
	p = p*i
print("Product of all Elements are :: ", p)