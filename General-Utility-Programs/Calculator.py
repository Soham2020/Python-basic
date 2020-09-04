# A Simple Calculator

# Function Declarations 
def add(x, y):  
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   return x * y 
def divide(x, y):  
   return x / y  

# Input From User  
print("Calculator \n\nSelect The Operation")  
print("1. Add")  
print("2. Subtract")  
print("3. Multiply")  
print("4. Divide")
print("5. Exponent & Power")  
  
choice = input("Enter Your Choice (1-5) :")  
  
n1 = int(input("Enter First Number: "))  
n2 = int(input("Enter Second Number: "))  
  
# Conditional Rendering
if choice == '1':  
   print(n1,"+",n2,"=", add(n1,n2))  
  
elif choice == '2':  
   print(n1,"-",n2,"=", subtract(n1,n2))  
  
elif choice == '3':  
   print(n1,"*",n2,"=", multiply(n1,n2))  

elif choice == '4':  
   print(n1,"/",n2,"=", divide(n1,n2))  

elif choice == '5':  
   print(n1,"^",n2,"=", n1**n2)  

else:  
   print("Invalid Input")  