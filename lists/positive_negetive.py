a = []
print("Enter the Array Elements::")
for i in range(5):
	n = int(input())
	a.append(n)
for i in a:
	if(i>0):
		print(i, " is a positive element")
	else:
		print(i, " is a negetive element")