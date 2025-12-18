import random

num = random.randrange(1, 101)

user_guess = 0

while user_guess != num:
    user_guess = int(input("Insert number between 1 and 100: "))

    if user_guess > num:
        print ("\nIt's a lower number!")
    
    elif user_guess < num:
        print ("\nIt's a higher number!")
    
print(f"\n---Good job! The number was {num}---")