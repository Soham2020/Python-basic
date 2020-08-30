str1 = str(input("Enter the String:: "))
if (len(str1)>2):
	str2 = str1[0:2] + str1[-2:]
	print(str2)
else:
	print("String Empty")