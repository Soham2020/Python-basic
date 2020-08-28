# Check Whether The Entered Number is a Perfect Number or NOT

n = int(input("Enter A Number : "))

i = 1
sum = 0

while(i < n):
    if(n%i == 0):
        sum = sum + i
    i += 1

if(sum == n):
    print("Perfect Number")
else:
    print("NOT a Perfect Number")