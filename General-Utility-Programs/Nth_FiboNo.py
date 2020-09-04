# Program to Calculate nth Fibonacci number 
  
def Fibo(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibo(n-1)+Fibo(n-2) 
  
n = int(input())
print(Fibo(n)) 