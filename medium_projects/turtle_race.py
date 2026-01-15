import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
colors = ["red", "cyan", "blue", "green", "purple", "pink"]

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
         
def main():
    turtles_num = get_num_turtles()
    init_turtle_screen()
    for racer in range(turtles_num):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(colors[racer])
        racer.penup()
        racer.forward(100)
    time.sleep(5)

main()        