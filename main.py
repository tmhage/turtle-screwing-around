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


def random_walk(turtle):
    change_color(turtle)
    turtle.forward(10)
    turns = [0, 90, 180, 270]
    turtle.setheading(random.choice(turns))


# for x in range(3, 11):
#     draw_shape(x, jimmy)
while True:
    random_walk(jimmy)


screen = Screen()
screen.exitonclick()
