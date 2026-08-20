#  Write a Python program to generate a random password for the user. The password will contain at
# least one capital letter, one small letter, and one digit. The length of the password should be 10.
# You are allowed to use random.random() function for generating random numbers within the range of 0
# and 1.
# Use of any external direct package is not allowed.
# Note: You are allowed to use only the random.random() function to generate random numbers in the
# range 0 to 1. The use of any other random number generation functions (such as random.randint(),
# random.choice(), random.shuffle(), etc.) or any external packages is not allowed.


import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

password = ""


r = random.random()    # Generate at least one uppercase letter
index = int(r * len(uppercase))
password += uppercase[index]


r = random.random()  # Generate at least one lowercase letter
index = int(r * len(lowercase))
password += lowercase[index]


r = random.random()   # Generate at least one digit
index = int(r * len(digits))
password += digits[index]


characters = uppercase + lowercase + digits  # Generate the remaining 7 characters

for i in range(7):
    r = random.random()
    index = int(r * len(characters))
    password += characters[index]


password = list(password) # Convert the password into a list

for i in range(len(password) - 1, 0, -1):  #manual shuffling of the password list
    r = random.random()
    j = int(r * (i + 1))

    password[i], password[j] = password[j], password[i]

password = "".join(password)

print("Generated Password:", password)