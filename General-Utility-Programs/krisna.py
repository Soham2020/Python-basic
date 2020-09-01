def factorial(n):
	fact = 1
	for i in range(1, n+1):
		fact = fact * i
	return fact
def krishna(n):
	sum = 0
	temp = n
	while(temp > 0):
		rem = temp%10
		temp = temp//10
		sum = sum + factorial(rem)
	return(sum == n)
n = int(input("Enter the Number:: "))
if(krishna(n)):
	print("Happy Number")
else:
	print("Not a Happy Number")