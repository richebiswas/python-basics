#Write a program that takes a number and tells you if it's even/odd and positive/negative.

num=int(input("Enter a Number : "))
 #if num%2==0 and num>0 :
  # print ("Number is EVEN and Positive")
 #elif num%2==0 and num<0:
  #  print ("Number is EVEN and Negative")
 #elif num%2!=0 and num>0:
   # print ("Number is ODD and Positive")
 #elif num%2!=0 and num<0:
    #print ("Number is ODD and Negative")
#else:
  # print ("Number is zero")
    
    #shorter or more clear version is 

if num==0:
  print(" the number is zero")
else:
  if num%2==0:
   result="EVEN"
  else:
   result="ODD"

if(num>0):
       print("the number is", result," and positive")
else:
       print("the number is", result," and negative")


