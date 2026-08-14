#Write a function (WAF) to count the number of vowels in a string

def vowels(s):
  cnt=0
  for ch in s:
    if ch.lower() in "aeiou":
      cnt+=1
    
  return cnt
    
print(vowels("Hello this is Krittika")) 