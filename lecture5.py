#len function
#slicing
#count, find(gives the first index of the find element), replace
a = "Hello Soham Das Das Das Das Das!"
print(a[1])
sli = a[0:7]
print(sli)
length = len(a)
print(length)
b = "Das"
count = a.count(b)
print(count)
find = a.find(b)
print(find)
replace = a.replace(" ","-")
print(replace)
if(b in a):
	print("Yes")
else:
	print("No")
for b in a:
	print(b)
print(a.upper())
print(a.lower())