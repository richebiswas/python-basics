#Sum from 1 to N  eg:- Take N and calculate : 1 + 2 + 3 + ... + N


def sum2(n):
    i=0
    s=0
    while i<=n:
     s=s+i
     i+=1
    return(s)
result=sum2(5)    
print(result)