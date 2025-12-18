import random
import time

num = random.randrange(1, 101)

user_guess = 0
guesses = 0    
start = time.perf_counter()

while user_guess != num:
    user_guess = input("Insert number between 1 and 100: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100!\n")
        elif user_guess > num:
            print ("\nIt's a lower number!")
            guesses+=1
        elif user_guess < num:
            print ("\nIt's a higher number!")
            guesses+=1
    else: 
        print("Please insert a number!\n")

end = time.perf_counter()
print(f"\n----Good job! The number was {num}----")
print(f"You took {guesses+1} atempts and {end - start:.2f} seconds to guess!")