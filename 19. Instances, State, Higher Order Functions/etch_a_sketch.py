# needed imports
from turtle import Turtle, Screen


# init the turtle
t = Turtle()


def go_forward():
    """
    Function that moves the turtle forward by 10 units
    """
    t.forward(10)


def go_backwards():
    """
    Function that moves the turtle backwards by 10 units
    """
    t.backward(10)


def turn_right():
    """
    Function that turns the turtle to the right by 10 degrees
    """
    t.setheading(t.heading() - 10)


def turn_left():
    """
    Function that turns the turtle to the left by 10 degrees
    """
    t.setheading(t.heading() + 10)


def clear():
    """
    Function that clears the screen and resets the turtle's position
    """
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# init the screen
screen = Screen()

# make the screen listen for user input
screen.listen()
screen.onkey(go_forward, "w") # making the turtle move forwards if we press w
screen.onkey(go_backwards, "s") # making the turtle move backwards if we press s
screen.onkey(turn_left, "a") # making the turtle turn left if we press a 
screen.onkey(turn_right, "d") # making the turtle turn right if we press d
screen.onkey(clear, "c") # resetting the screen if we press c
screen.exitonclick()