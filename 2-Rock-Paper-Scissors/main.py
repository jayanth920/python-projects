import random

# Outcomes
outcomes = ["rock", "paper", "scissors"]

# Initial scores
cscore = 0
pscore = 0

while True:
    player = input("Type Rock/Paper/Scissors to play or press Q to quit!\n").lower()
    
    if player == "q":
        break
    if player not in outcomes:
        print("Invalid input, please try again.")
        continue
    
    comp = random.choice(outcomes)
    print(f"Computer chose {comp}")

    if comp == player:
        print("TIE")
    elif (comp == "rock" and player == "scissors") or \
         (comp == "scissors" and player == "paper") or \
         (comp == "paper" and player == "rock"):
        print(f"Computer Wins! {comp} beats {player}")
        cscore += 1
    else:
        print(f"Player Wins! {player} beats {comp}")
        pscore += 1

    print(f"Player Score: {pscore}, Computer's Score: {cscore}")

print("Thanks for playing!")