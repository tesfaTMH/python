#Q1: if else for checking length of users input
string1 = input("Write some random characters: ")

if len(string1) < 5:
    print("Your text is less than 5 character")
elif len(string1) > 5:
    print("Your text is greater than 5 characters")
else:
    print("Your text is 5 characters long")

#Q2: guessing number challenge
from random import randint

guess = randint(1, 10)

guessed = int(input("I 'm thinking a number b/n 1 and 10. Guess which one: "))

if (guessed == guess):
    print("You Won!")
else:
    print("You lost!")