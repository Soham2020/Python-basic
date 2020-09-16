x = eval(input("Enter the List::"))
y = eval(input("Enter the List::"))
z = []
z = x+y
# print(z)
a = []
for i in z:
  if i not in a:
    a.append(i)
print(a)