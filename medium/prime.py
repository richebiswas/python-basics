#Check Prime Number: Take a number and determine whether it is prime.

def prime(n):
    flag=0
    i=1
    while i<=n:
        if (n%i==0):
            flag+=1
        i+=1    
    if (flag==2):
          print("prime")
    else:
           print("not prime")   
prime(5)                
