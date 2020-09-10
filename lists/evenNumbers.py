a = []
print("Enter the Array Element::")
for i in range(5):
	n = int(input())
	a.append(n)
for i in a:
	if(i%2==0):
		print("Even Number :: ", i)
	else:
		print("Odd Number  :: ", i)