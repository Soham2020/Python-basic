str1 = str(input("Enter the List::"))
str2 = str(input("Enter the List::"))
for i in str1:
  if i not in str2:
    print(i)