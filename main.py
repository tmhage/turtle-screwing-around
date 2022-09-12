from turtle import Turtle, Screen

jimmy = Turtle()

for corners in range(3, 10):
    turn = 360 / corners

    for x in range(corners):
        jimmy.forward(100)
        jimmy.right(turn)

screen = Screen()
screen.exitonclick()
