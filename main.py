from turtle import Turtle, Screen
import random

jimmy = Turtle()


def change_color(turtle):
    r = random.random()
    b = random.random()
    g = random.random()
    turtle.color(r, b, g)

def draw_shape(sides, turtle):
    change_color(turtle)
    turn = 360 / sides

    for _ in range(sides):
        turtle.forward(100)
        turtle.right(turn)


for sides in range(3, 11):
    draw_shape(sides, jimmy)


screen = Screen()
screen.exitonclick()
