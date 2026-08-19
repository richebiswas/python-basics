#Find Smallest in a List :Find the smallest number without using min().

def smallest(list):
    small=list[0]
    for i in list:
      if i<small:
       small=i
    return small
print(smallest([1,5,7,9,2,8,11]) )