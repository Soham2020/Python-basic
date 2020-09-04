# Program to Calculate The Number of Vowels in a Given String

str1 = str(input("Enter A String : "))
count = 0
for i in str1:
	if(i=='A' or i=='a' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
		count = count + 1
print("Number of Vowels in the Entered String : ", count)