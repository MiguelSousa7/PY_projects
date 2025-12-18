import random

num = random.randrange(1, 101)

user_guess = 0

while user_guess != num:
    user_guess = input("Insert number between 1 and 100: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100!\n")
        elif user_guess > num:
            print ("\nIt's a lower number!")
        elif user_guess < num:
            print ("\nIt's a higher number!")
        
    else: 
        print("Please insert a number!\n")
        continue
    
print(f"\n----Good job! The number was {num}----")