# Remove Spaces: Remove all spaces from a string without using .replace().
#//// using replace
# txt = "I like bananas"
# x = txt.replace(" ", "")
# print(x)


def spaces_rem(s):
    length=len(s)
    i=0
    result=""
    while i<length:
       if s[i]!=" ":
          result=result+s[i]

       i+=1     
    print(result)

spaces_rem("I like bananas,apples and fruit")   