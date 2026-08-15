def fibonnaci(num):
    a=0
    b=1
    if num<=1:  #if num is 0 and 1 it will return 0 and 1 as it is
      return num
    else:
     return fibonnaci(num-1)+fibonnaci(num-2)  #formula for recursion

                                 #Using loop

                        #terms=input(int("enter the range of numbers"))
                         #if terms<=0:
                           # print("Please enter a positive integer ")
                         #else:
                                 # print("The fibonnaci series is: ")
                         #for i in range(terms):
 
                               #print(fibonnaci(i),ends=" ")

                                  #Using recursion
def print_series(term,i=0): #here we have two numbers term and i(the loop)
    if term==i:     #means if term is equal to i then we will return
        return
    print(fibonnaci(i),end=" ") #the number I have to PRINT
    print_series( term , i+1) # this is the recursive call to the function print_series with term and i+1 as arguments.
   #move to the NEXT number in simple meaning
print_series(8)