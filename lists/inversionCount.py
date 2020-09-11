a = []
size = int(input("Enter the Size of the List=>"))
print("Enter the Array Elements::")
for i in range(size):
    n = int(input())
    a.append(n)
print("List is => ", a)
count = 0
for i in range(size):
    for j in range(size-1):
        if(a[i]>a[j]):
            count = count + 1
print("Inversion Counts are=>", count)