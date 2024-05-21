# importing from the turtle module
from turtle import Turtle, Screen

# init the turtle object
t = Turtle()


# making the turtle draw a square
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)


# init the screen and setting the exitonclick property
screen = Screen()
screen.exitonclick()