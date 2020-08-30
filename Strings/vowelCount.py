str1 = str(input("Please Enter the String:: "))
flag = 0
for i in str1:
	if(i=='A' or i=='a' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
		flag = flag + 1
print("Vowel count is :: ", flag)