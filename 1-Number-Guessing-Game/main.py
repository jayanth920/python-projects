# Random Number Guessing Game --------------------------------------


import random

top = input("ENTER A DIGIT !!\n")
if top.isdigit():
    top = int(top)
    if top <= 0:
        print("PLEASE ENTER A VALID NUMBER NEXT TIME !\n")
else:
    print("ENTER A VALID NUMBER NEXT TIME !!\n")

ans = random.randint(1,top)

answered = False

while answered == False:
    guess = input("GUESS A NUMBER !!\n")
    if guess.isdigit():
        guess = int(guess)
        if guess <= 0:
            print("PLEASE ENTER A VALID NUMBER NEXT TIME !\n")
    if guess == ans:
        print("YOU GUESSED IT CONGRATS !!!!!!!!!!!!!!!!!!!")
        answered = True
    elif guess > ans:
        print("AAH GO LOWER...")
    elif guess < ans:
        print("AAH GO MORE...")
    else:
        print("YOU GOT IT WRONG MY BRO.....TRY AGAIN !!\n")