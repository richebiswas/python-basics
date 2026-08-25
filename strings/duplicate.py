#Find Duplicate Characters: Find characters that occur more than once without using set().

# sentence = "yo the food looks good do u want to have some"
# result = set(sentence)
# print(result)

def duplicate_string(s):
 i = 0
 n=len(s)
 printed=""
 while i < n:
    cnt=0
    j = 0

    while j < n:
        if s[i]==s[j]:
         cnt+=1
        j += 1

    if cnt > 1:
        if s[i] not in printed:
            print(s[i])
            printed =printed + s[i]

    i += 1
duplicate_string("banana")