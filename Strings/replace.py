str1 = str(input("Enter the String:: "))
result = ""
for i in range(len(str1)):
	if i%2 == 0:
		result = result + str1[i]
print("New String:: ", result)