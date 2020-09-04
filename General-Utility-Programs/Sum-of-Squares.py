# Python Program to find sum of square of first n natural numbers

# From the knowledge of mathematics, we know - 
# Sum of squares upto n = (n * (n+1) / 2) * (2 * n+1) / 3  
  
def sum_of_squares(n): 
    return (n * (n+1) / 2) * (2 * n+1) / 3
   
n = int(input())

print(sum_of_squares(n)) 