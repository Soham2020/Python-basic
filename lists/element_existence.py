a = []
print("Enter the Array Elements::")
for i in range(5):
	n = int(input())
	a.append(n)
b = int(input("Enter the Element you want to be searched::"))
# count = 0
# for j in a:
# 	if(a == b):
# 		count = count + 1
# if(count != 0):
# 	print("Element found")
# else:
# 	print("Element not found")
if(b in a):
	print("Element found")
else:
	print("Element not found")