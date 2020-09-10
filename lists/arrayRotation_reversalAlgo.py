def reverse(a,d):
	n = len(a)
	rotate(a, 0, d-1)
	rotate(a, d, n-1)
	rotate(a, 0, n-1)
def rotate(a,start,end):
	temp=0
	while(start<end):
		temp=a[start]
		a[start]=a[end]
		a[end]=temp
		start=start+1
		end=end-1
def printArray(a):
	print("Required Array is::",a)


a = []
print("Enter the Array element::")
x = int(input("Enter the Array Size::"))
for i in range(x):
	n = int(input())
	a.append(n)
d = int(input("Enter the rotate value::"))
print("Original Array::", a)
reverse(a,d)
printArray(a)
