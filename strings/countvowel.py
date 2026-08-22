# 3. Count Vowels:Count how many vowels are present in a string.

text=str("hello world!")
text=text.lower()
cnt=0
for i in text:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u' :
     cnt+=1
print(cnt)     
