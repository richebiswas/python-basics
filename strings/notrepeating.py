#First Non-Repeating Character: Find the first character that occurs only once.

def not_repeating(s):
 i = 0
 n=len(s)

 while i < n:
    cnt=0
    j = 0

    while j < n:
        if s[i]==s[j]:
         cnt+=1
        j += 1

    if cnt == 1:
       print(s[i])
           

    i += 1
not_repeating("banana")