# n1 = int(input("Please enter the number:: "))
# n2 = int(input("Please enter the number:: "))
# a = n1%10
# b = n2%10
# if(a<b):
# 	print("So ", n1, " has lesser one's digit than ", n2)
# else:
# 	print("So ", n2, " has lesser one's digit than ", n1)
def ones(n1, n2):
	 a = n1%10
	 b = n2%10
	 if(a<b):
	 	print("So ", n1, " has lesser one's digit than ", n2)
	 else:
	 	print("So ", n2, " has lesser one's digit than ", n1)
n1 = int(input("Please enter the number:: "))
n2 = int(input("Please enter the number:: "))
ones(n1, n2)