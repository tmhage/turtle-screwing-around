from turtle import Turtle, Screen
import random

jimmy = Turtle()


def change_color(turtle):
    r = random.random()
    b = random.random()
    g = random.random()
    turtle.color(r, b, g)


for corners in range(3, 10):
    turn = 360 / corners

    for x in range(corners):
        jimmy.forward(100)
        jimmy.right(turn)

    change_color(jimmy)

screen = Screen()
screen.exitonclick()
