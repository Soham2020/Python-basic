# Program To Check Whether The Entered String is Palindrome or Not

# First We Reverse The String Using List Slicing & Negative Index
# and then compare it with the original string.

def isPalindrome(str):
    return str == str[::-1]
 
str = input("Enter A String : ")
res = isPalindrome(str)
 
if res:
    print("Palindrome")
else:
    print("Not A Palindrome")