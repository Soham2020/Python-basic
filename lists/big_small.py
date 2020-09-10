a = []
print("Enter the Elements::")
for i in range(0,5):
	n = int(input())
	a.append(n)
print(a)
b = max(a)
c = min(a)
print("Maximum Element in the list is::", b)
print("Minimum Element in the list is::", c)