#Factorial Input:5 Output: 120
def factorial(n):
    cnt=n
    fact=1
    while n>0:
    
     fact=fact*cnt
     cnt-=1
     n-=1
    return fact

print(factorial(5))
