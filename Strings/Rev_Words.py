# Program to Reverse Words of a String 

# Input - "i am a web developer"
# Output - "developer web a am i"
  
def rev_sentence(sentence): 
    words = sentence.split(' ')  
    output = ' '.join(reversed(words))  
    return output   
   
s = input()
print (rev_sentence(s))