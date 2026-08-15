#Write a Python program that takes a paragraph as input through the terminal and returns the most common word in it.
# The entire paragraph should be entered by the user during program execution.
# Sample User Input #  Enter a paragraph: 
# Python is easy to learn. Python is powerful and Python is widely used for machine learning,  web development, and data analysis. Learning Python is fun.


para= input("Enter a Paragraph: ")

words=para.split() #split the paragraph into words eg:- 'Python', 'is', 'easy', 'to', 'learn.', 'Python', 'is', 'powerful',......
print(words)
count={}  #this creates an empty dictionary
highest=0
common_word=""

for  i in words: #i will take each word from the list of words one by one and check if it is already present in the dictionary or not.
    if i in count: # if the word is already present in the dictionary then increment its count by 1
        count[i]+=1
    else:
         count[i]=1 #  new word is added to the dictionary with count 1

    if count[i]>highest: #check if the count of the current word is greater than the highest count so far. If yes, then update the highest count and the common word.
        highest=count[i]
        common_word=i

print("the most common word is: ",common_word )       
print("the number of times it occurs is:" ,highest)