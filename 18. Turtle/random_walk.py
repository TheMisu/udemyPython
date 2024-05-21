import random
from turtle import Turtle, Screen


# init the turtle
t = Turtle()
t.speed(0)
t.pensize(10)


def random_colour():
    """
    Function that returns a triple with randomly generated RGB values
    """
    red = random.randint(0, 255) / 255.0
    green = random.randint(0, 255) / 255.0
    blue = random.randint(0, 255) / 255.0
    rgb_triple = (red, green, blue)
    return rgb_triple


def random_walk(walk_len):
    """
    Function that makes the turtle generate a random walk
    """
    path_lens = [10, 20, 30, 40, 50]
    directions = [0, 90, 180, 270]

    for path in range(walk_len):
        # generate a new colour and a new path len for each path
        path_len = random.choice(path_lens)
        colour = random_colour()

        # generate the next direction
        next_dir = random.choice(directions)

        t.pencolor(colour)
        t.forward(path_len)
        t.setheading(next_dir)


# run the random_walk function
random_walk(200)


# init the screen
screen = Screen()
screen.exitonclick()