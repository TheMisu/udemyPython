from turtle import Turtle, Screen
import random

# init turtle
t = Turtle()
t.speed(0)


def random_colour():
    """
    Function that generates a random colour to be used by Turtle
    """
    red = random.randint(0, 255) / 255.0
    green = random.randint(0, 255) / 255.0
    blue = random.randint(0, 255) / 255.0
    rgb = (red, green, blue)
    return rgb


def draw_spirograph(gap_between_circles):
    """
    Function that draws a spirograph based on the chosen gap between circles
    """
    iterations = 360 // gap_between_circles

    for i in range(iterations):
        t.pencolor(random_colour())
        t.circle(100)
        t.setheading(t.heading() + gap_between_circles)


# drawing the spirograph
draw_spirograph(5)


# making the screen exit on click
screen = Screen()
screen.exitonclick()