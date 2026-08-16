#Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
#print out the average of the numbers 
#Enter a number: 4
#Enter a number: 5
#Enter a number: 7
#Enter a number: done
#Average=5.33

total=0
cnt=0
avg=0
while True:
    num=(input("enter the number: "))  
    if num=="done":
        break

    else:
        num=int(num)
        total=total+num
        cnt+=1
avg=total/cnt        
print(avg)
 

        
        
        
    