#Palindrome String: Check whether a string is a palindrome.

def plaindrome(s):
    reverse=""
    i=len(s)-1
    while i>=0:
      
      reverse=reverse+s[i]
      i-=1
    if(s==reverse):
         print(" The String is palindrome")
    else:
         print(" The String is not palindrome")

plaindrome("mad")