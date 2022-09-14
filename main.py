from turtle import Turtle, Screen
import random

jimmy = Turtle()


def random_colour():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def draw_shape(sides, turtle):
    turtle.pencolor(random_colour())
    turn = 360 / sides

    for _ in range(sides):
        turtle.forward(100)
        turtle.right(turn)


def random_walk(turtle):
    turtle.pencolor(random_colour())
    turtle.forward(10)
    turns = [0, 90, 180, 270]
    turtle.setheading(random.choice(turns))


def spirograph(turtle, gap_size):
    turtle.speed("fastest")
    for x in range(int(360 / gap_size)):
        turtle.pencolor(random_colour())
        turtle.circle(100)
        turtle.right(gap_size)


spirograph(jimmy, 5)

# for x in range(3, 11):
#     draw_shape(x, jimmy)

# while True:
#     random_walk(jimmy)


screen = Screen()
screen.exitonclick()
