print("\nWelcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() ==  "no":
    quit()

print("\nAmazing! Let's play :)\n")

questions = [
    "1. What does CPU stand for? ",
    "2. What does GPU stand for? ",
    "3. What does RAM stand for? ",
    "4. What does PSU stand for? ",
]

answers = [
    "central processing unit",
    "graphics processing unit",
    "random access memory",
    "power supply"
]

score = 0

for q, a in zip(questions, answers):  
    answer = input(q)
    if answer.lower() == a:
        print("Correct!\n")
        score+=1
    else:
        print(f"Incorrect! It's {a}\n")

print("Congratulations, you finished the quiz!\n")

print(f"You answered correctly to {score} out of {len(questions)} questions!")
print(f"FINAL SCORE: {(score / len(questions)) * 100} %")