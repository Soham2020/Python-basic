str1 = str(input("Enter the String:: "))
if(len(str1)<4):
	print(str1 + "ing")
elif(str1[-3:] == 'ing'):
	print(str1 + "ly")
else:
	print("Input Invalid")