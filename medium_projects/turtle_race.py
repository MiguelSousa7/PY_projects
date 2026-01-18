import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "cyan", "blue", "green", "purple", "pink", "orange", "yellow", "black", "brown"]

def init_turtle_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing game")

def get_num_turtles():
    turtles = 0
    while True:
        turtles = input("Enter the number of turtles in the race (2-10): ")
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print("\nPlease only enter numbers!\n")
            continue

        if 2 <= turtles <= 10:
            return turtles    
        else:
            print("\nPlease enter a number between 2 and 10!\n")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.penup()
        racer.left(90)
        racer.setpos(-WIDTH//2 + (spacingx*(i+1)), -(HEIGHT//2)+15)
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,10)
            racer.forward(distance)
            _, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]
    

def main():
    turtles_num = get_num_turtles()
    init_turtle_screen()
    random.shuffle(COLORS)
    colors = COLORS[:turtles_num]
    winner = race(colors)
    print(f"\n{winner} turtle won!\n")
    time.sleep(4)
main()        