#Sum of Digits Input: 58392  Output: 27

def sum_of_digits(num):

    rem=0
    rev=0
    while num>0:
          rem=num%10
          rev=rev+rem
          num=num//10
    return rev
print(sum_of_digits(58932))
        