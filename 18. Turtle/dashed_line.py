from turtle import Turtle, Screen


# init the turtle
t = Turtle()


# drawing a dashed line
for i in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


# init the screen
screen = Screen()
screen.exitonclick()