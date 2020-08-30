str1 = str(input("Enter the String:: "))
str2 = str1.split()
flag = ""
for i in str2:
	flag = flag + i[0].upper()
print("Acronym is ::", flag)