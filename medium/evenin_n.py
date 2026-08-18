#Count Even Numbers: Take N and count how many even numbers exist between 1 and N.

def count(n):
    i=1
    cnt=0
    while i<=n:
        if i%2==0:
             cnt+=1
        i+=1    
    print(cnt)
count(10)