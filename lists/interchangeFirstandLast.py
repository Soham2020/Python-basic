a = []
print("Enter the Elements::")
for i in range(0,5):
	n = int(input())
	a.append(n)
print("Before Swapping:: ", a)
b = len(a)
swap = a[0]
a[0] = a[b-1]
a[b-1] = swap
print("After Swapping :: ", a)