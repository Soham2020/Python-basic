# Program to Print Largest of Three Numbers

def largest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a,b,c = map(int, input("Enter Three Numbers : ").split(" "))
res = largest(a,b,c)

print("Largest of the Three Numbers is -",res)