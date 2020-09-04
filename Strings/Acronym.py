# Program To Find Acronym of a String

str1 = str(input("Enter The String : "))

str2 = str1.split()

flag = ""
for i in str2:
	flag = flag + i[0].upper()
	
print("Acronym - ", flag)