#magic_number = input("What is the magic number? ")
#guess = input("What is your guess? ")
#
#while guess != magic_number:
#    if guess < magic_number:
#        print("Higher")
#    elif guess > magic_number:
#        print("Lower")
#    else: print("XD")
#    guess = input("What is your guess? ")
#
#print("You guessed it!")

import random

magic_number = random.randint(1,100)
guess = input("What is your guess? ")

while guess != magic_number:
    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else: print("XD")
    guess = input("What is your guess? ")

print("You guessed it!")