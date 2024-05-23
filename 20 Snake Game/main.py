# imports
from turtle import Turtle, Screen


# init the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")


# creating the snake
snake_body = [(0, 0), (-20, 0), (-40, 0)]

for part_position in snake_body:
    new_snake_part = Turtle("square")
    new_snake_part.color("white")
    new_snake_part.goto(part_position)


# exit on click to facilitate testing
screen.exitonclick()