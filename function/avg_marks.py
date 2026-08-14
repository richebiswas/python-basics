
#4. Write a function (WAF) to return the average marks when a list of marks is passed as a parameter.


def avg_marks(marks):
 
    average_marks=sum(marks)/len(marks)
    return(average_marks)   #pass the calculated average back to whoever called the function.
marks=[50,95,60,35,94,100,56,47,81,80,65,35]  
print(avg_marks(marks))    #avg_marks function called the marks