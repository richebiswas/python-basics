# Write a function (WAF) to print whether a number is prime or not.

def prime(num):
    flag=0
    for i in range(1,num+1):
        if num%i==0:
            flag+=1
    if(flag<=2):
        print("prime")
    else:
        print("non prime")
prime(11)
