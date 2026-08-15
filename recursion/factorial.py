# factorial of a number using recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(" The factorial is", factorial(5))

#logic:- first u enter the number eg 4 so the condition checks if n is less than 0 or 1 if not the second condition works which is n*fact(n-1)
#so 4*fact(3)  then again check again second condition then it becomes 4*3 fact(2) then in second loop it becomes 4*3*2 fact(1)
# now the first loop works so it will return 1 which is 4*3*2*1 then we get the output 24 