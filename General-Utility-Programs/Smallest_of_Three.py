# Program to Print Smallest of Three Numbers

def smallest(a, b, c):
    if(a<b and a<c):
        return a
    elif(b<a and b<c):
        return b
    else:
        return c

a,b,c = map(int, input("Enter Three Numbers : ").split(" "))
res = smallest(a,b,c)

print("Smallest of the Three Numbers is -",res)