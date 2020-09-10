a = []
b = []
count = 0
print("Enter the Elements::")
for i in range(0,3):
	n = str(input())
	a.append(n)
print(a)
m = str(input("Enter the word ::"))
p = int(input("Enter the Occurance::"))
for i in a:
	if(i == m):
		count = count + 1
		if(count!=p):
			b.append(i)
		else:
			b.append(i)
if(count == 0):
	print("Item not found")
else:
	print("New list is :: ", b)