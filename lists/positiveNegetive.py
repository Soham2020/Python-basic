a = []
print("Enter the Array Elements::")
for i in range(5):
    n = int(input())
    a.append(n)
print("Our Array is::", a)
count = 0
flag = 0
for i in a:
    if(i<0):
        count = count + 1
    else:
        flag = flag + 1
print("Positive Elements in the Array are::", flag)
print("Negetive Element in the Array are::", count)