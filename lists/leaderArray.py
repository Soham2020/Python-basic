a = []
size = int(input("Enter the Size::"))
print("Enter the Array Elements::")
for i in range(size):
    n = int(input())
    a.append(n)
print("Array is ::", a)
print("Leader of the Array is ::")
max = a[size-1]
print(max)
for i in range(size-2, -1, -1):
    if(a[i]>=max):
        print(a[i])
        max = a[i]