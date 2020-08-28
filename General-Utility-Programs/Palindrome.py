# Check Whether The Entered Number is a Palindrome or Not

n = int(input("Enter A Number : "))

temp = n
rev = 0
while(n>0):
    r = n % 10
    rev = rev*10 + r
    n = n // 10

if(temp == rev):
    print("Palindrome")
else:
    print("Not a Palindrome")