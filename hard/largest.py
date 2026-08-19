#Find Largest in a List: Find the largest number in a list without using max().

def largest(list):
  large=0
  for i in list:
    if i>large:
      large=i
  return large
print(largest([1,5,7,9,2,8,11]) )