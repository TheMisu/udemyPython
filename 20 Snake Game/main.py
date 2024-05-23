# imports
from scoreboard import Scoreboard
from snake import Snake
from food import Food
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
food = Food()
scoreboard = Scoreboard()

# adding event listeners to the screen so that we can control the snake
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# while loop for the game
game_is_on = True

while game_is_on:
    screen.update() # upload/reload the screen
    time.sleep(0.1) # helps with the animation
    
    # moving the snake
    snake.move() 


    # checking if the snake ate/hit the food
    if snake.head.distance(food) < 20:
        # changing the foods position
        food.change_pos()
        scoreboard.increase_score()


    # checking if the snake hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


# exit on click to facilitate testing
screen.exitonclick()