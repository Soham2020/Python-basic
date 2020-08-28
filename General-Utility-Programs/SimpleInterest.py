# Simple Interest Calculation

p = int(input("Enter P : "))
r = float(input("Enter R : "))
t = int(input("Enter T : "))

i = (p*r*t) / 100

print("Interest is : {0:.2f}".format(i)) # Keeping The Answer Upto Two Decimal Places
