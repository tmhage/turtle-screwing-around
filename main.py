from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("red")

for x in range(50):
    jimmy.forward(10)
    if jimmy.isdown():
        jimmy.penup()
    else:
        jimmy.pendown()

screen = Screen()
screen.exitonclick()