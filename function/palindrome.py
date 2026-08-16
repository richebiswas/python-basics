#check if a number is plaindrome or not if not then return false else return true

def palindrome(num):
    n=num
    rev=0
    while(num>0):
      rem=num%10
      rev=rev*10+rem
      num=num//10
    if n == rev:
      return True
    else:
       return False
    
num=int(input("Enter a number: "))
print(palindrome(num))