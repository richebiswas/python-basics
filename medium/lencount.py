#Count Digits Input:58392  Output: 5


def count_digit(num):
    cnt=0
    while num>0:
        cnt+=1
        num=num//10
    return cnt
print(count_digit(58392))