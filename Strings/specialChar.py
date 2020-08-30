str1 = str(input("Enter the string:: "))
for i in str1:
	if(i == '@' or i == '#' or i == '$' or i == '%' or i == '&'):
		print("Special Character found that is", i)