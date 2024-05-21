import random
from turtle import Turtle, Screen


# init the turtle
t = Turtle()


def draw_shape(num_of_sides):
    """
    Function that draws a shape based on the number of sides it should have
    """
    angle = 360 / num_of_sides
    for side in range(num_of_sides):
        t.forward(100)
        t.right(angle)


# draw every shape from triangle until decagon
for num_sides in range(3, 11):
    # generating a random colour for each shape
    random_red = random.randint(0, 255) / 255.0
    random_green = random.randint(0, 255) / 255.0
    random_blue = random.randint(0, 255) / 255.0
    rgb_tuple = (random_red, random_green, random_blue)
    t.pencolor(rgb_tuple)

    # drawing the shape
    draw_shape(num_sides)


# init the screen
screen = Screen()
screen.exitonclick() 