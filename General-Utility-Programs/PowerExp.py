# Calculate The Power

n = int(input("Enter The Number : "))
pow = int(input("Enter The Power : "))

result = 1
i = 1

while(i<=pow):
    result = result * n
    i = i + 1

print(n,"^",pow,"=",result)