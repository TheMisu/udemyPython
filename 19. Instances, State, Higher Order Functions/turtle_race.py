# importing turtle
from turtle import Turtle, Screen

# turtle colours
colours = ["red", "orange", "yellow", "green", "blue"]

# init the screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose between red/orange/yellow/green/blue: ")


# init the turtles in the start position
y_position = -100
for colour in colours:
    t = Turtle(shape="turtle")
    t.color(colour)
    t.penup()
    t.goto(x=-240, y=y_position)
    y_position += 50

screen.exitonclick()