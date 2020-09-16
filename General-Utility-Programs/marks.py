print("/******Division Calculator********/")
print("Enter the Marks ::")
n1 = float(input("Enter the Marks of subject 1:: "))
n2 = float(input("Enter the Marks of subject 2:: "))
n3 = float(input("Enter the Marks of subject 3:: "))
n4 = float(input("Enter the Marks of subject 4:: "))

per = (n1+n2+n3+n4)/4 
if(per>=75):
    print("/*******Division 1*******/")
elif(per<75 and per>=65):
    print("/********Division 2********/")
elif(per<65 and per>=50):
    print("/********Division 3*******/")
else:
    print("Failed") 