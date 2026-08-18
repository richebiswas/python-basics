# 1)print all odd number from 1  to 20
#2)print the table of 57
#3)print all multiple of 3 1 to 50 but skip 15
#4) take two integers a and b as input. find and print the first no btwn 1 to 1000 that is divisble by both numbers

#for i in range(1,21,2):
 #print(i)

#for i in range(1,201):
 #if(i%57==0):
 # print(i)

#for i in range (1,51):
 #if(i==15):
  #continue
 #if(i%3==0):
  #print(i)

a=int(input("ENTER A: "))
b=int(input("ENTER B: "))

for i in range(1,1001):
    if (i % a==0 and i % b ==0) :
        print(i)
        break