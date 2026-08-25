#Count Character Occurrences : Given a string and a character, count how many times the character appears without using .count().

def string_count(s,char):
    i=len(s)-1
    count=0
    while i>=0:
    
     if char==s[i]:
        count+=1
     i-=1   
    print(count)    

string_count("The ball is in your court nani",'i') 