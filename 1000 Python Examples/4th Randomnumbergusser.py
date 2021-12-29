# Using the random module the computer “thinks” about a
# whole number between 1 and 20.
# The user has to guess the number. After the user types in the
# guess the computer tells if this was bigger or smaller than the
# number it generated, or if was the same.
# The game ends after just one guess.

from random import random

seed = 100
x = int(random()*100)

y = int(input("Enter number to be guessed :"))
print("Greater than guessed number ") if x > y else print("Smaller then guessed number ")