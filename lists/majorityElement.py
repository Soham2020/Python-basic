#assumption-> always give a sorted list as input
a = []
print("Enter the Array Elements::")
for i in range(5):
    n = int(input())
    a.append(n)
print("List is->", a)
max = 0
index = -1
for i in range(5):
    count = 0
    for j in range(5):
        if(a[i]==a[j]):
            count = count + 1
    if(count>max):
        max = count
        index = i
if(max>n//2):
    print(a[index])
else:
    print("No Major elements")