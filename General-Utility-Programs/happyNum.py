def happy(num):
	sum = 0
	rem = 0
	while(num>0):
		rem = num%10
		num = num//10
		sum = sum + (rem**2)
	return sum
num = int(input("Enter the Number::"))
result = num
while(result!=1 and result!=4):
	result = happy(result)
if (result == 1):
	print("happy")
else:
	print("Not happy")