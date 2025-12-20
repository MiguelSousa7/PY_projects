import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players(2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:     
            break
        else:
            print(f"{players} is not valid! Must be 2-4 players.\n")
    else:   
        print(f"'{players}' is not valid! Enter a number instead.\n")

max_score = 50
players_score = [0 for _ in range(players)]


while max(players_score) < max_score:
    for p in range(players):
        current_score = 0

        while True:
            accept_roll = input(f"\nPLAYER_{p+1}: Would you like to roll the dice (y)/(n)? ").lower()
            
            if accept_roll in ("y", "yes"):
                value = roll()
                print(f"You rolled a {value}")
                if value == 1:
                    current_score = 0
                    print("So you lost all the accumulated points in this round!")
                    break
                else:
                    current_score += value
                    print(f"Score accumulated on this round: {current_score} points")

            elif accept_roll in ("n", "no"):
                break
            else: 
                print("Type only 'y' (yes) or 'n' (no).")
        
        players_score[p] += current_score

        print("\n----Total Points----")
        for player_index in range(players):
            print(f"PLAYER_{player_index+1}: {players_score[player_index]} points")
        print("--------------------")

for p in range(players):
    if players_score[p] >= 50:
        print(f"\n\nPLAYER_{p+1} won the game!")

print("\n----FINAL SCORE----")
for player_index in range(players):
    print(f"PLAYER_{player_index+1}: {players_score[player_index]} points")

