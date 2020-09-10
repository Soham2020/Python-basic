a = []
print("Enter the Array Element::")
for i in range(5):
	n = int(input())
	a.append(n)
print("The Array is:: ", a)
b = int(input("Enter the Element you want to found the occurance::"))
count = 0
for i in a:
	if(b == i):
		count = count + 1
print("Number occured by ", count, " times.")