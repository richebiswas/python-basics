#Reverse a String:Reverse a string without using [::-1].

def reverse_string(s):
    i=len(s)-1
    reverse=""
    while i>=0:
      reverse=reverse+s[i]
      i-=1
    print(reverse)

reverse_string("hello")