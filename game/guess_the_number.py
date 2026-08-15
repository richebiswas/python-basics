#here the user will guess the random number from 1 to 70 and the program will tell if the guess is correct or not and also hint if the number is higher 
# or lower than the guessed number.

import random

def guess_the_number():
 lucky_no = random.randint(1, 70)

 while True:
    user_input= int(input("Guess the number between 1 to 70: "))
    if lucky_no == user_input:
     print("you won the game")
     break
    elif lucky_no > user_input:
     print("number is too low:")
    else:
     print("number is too high:")
guess_the_number()  