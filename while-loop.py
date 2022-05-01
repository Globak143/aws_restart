print("Welcome to Guess the Number!")
print(" The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ") #ask the user to guess a number
    if int(guess) == number: #execute when guess is equal to number
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else: #run when guess if not equal to number
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))