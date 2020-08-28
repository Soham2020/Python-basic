# Calculate The Sum of Digits of a Number

n = int(input("Enter A Number : "))

sum = 0

while(n > 0):
    x = n % 10
    sum = sum + x
    n = n // 10

print("Sum of Digits of the entered number is ",sum)