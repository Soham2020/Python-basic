# Calculate LCM of Two Numbers

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

if(a>b):
    min = a
else:
    min = b

while(1):
    if(min%a == 0 and min%b == 0):
        print("LCM is",min)
        break
    min = min + 1