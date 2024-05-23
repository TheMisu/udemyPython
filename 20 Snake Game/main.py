# imports
from snake import Snake
from turtle import Turtle, Screen
import time

# init the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) # makes the screen not update on its own (helps with the moving animation)


# creating the snake
snake = Snake()


# while loop for the game
game_is_on = True

while game_is_on:
    screen.update() # upload/reload the screen
    time.sleep(0.1) # helps with the animation
    
    snake.move() 

# exit on click to facilitate testing
screen.exitonclick()