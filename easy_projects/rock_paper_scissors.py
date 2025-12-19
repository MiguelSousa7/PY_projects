import random

wins = 0
losses = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input ("Type rock/paper/scissors or 'q' to quit: ").lower()
    if user_pick == "q":
        break
    
    if user_pick not in options:
        continue
    else:
        rand_num = random.randint(0,2)
        pc_pick = options[rand_num]
        print(f"PC picked: {pc_pick}")

    if user_pick == pc_pick:
        print ("It's a tie!\n")
        ties+=1
    elif user_pick == "rock" and pc_pick == "scissors":
        print("You won!\n")
        wins+=1
    elif user_pick == "paper" and pc_pick == "rock":
        print("You won!\n")
        wins+=1
    elif user_pick == "scissors" and pc_pick == "paper":
        print("You won!\n")
        wins+=1
    else:
        print("You lost!\n")
        losses+=1

print("\n\n             FINAL SCORE")
print(f"---- wins:{wins} | losses:{losses} | ties:{ties} ----")
print("         Thanks for playing!\n")