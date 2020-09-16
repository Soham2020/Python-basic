n = int(input("Enter the Number :: "))
if((n%12==0) and (n%16==0) and (n%20==0) ):
    print("Divisible by 12, 16 and 20")
else:
    print("Not Divisible")  