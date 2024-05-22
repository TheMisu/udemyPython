# importing turtle
from turtle import Turtle, Screen
import random

def init_turtles():
    """
    Function that initializes the racing turtles and the screen.
    Returns a list of Turtle objects, the screen and user's ber
    """
    # turtle colours
    colours = ["red", "orange", "yellow", "green", "blue"]

    # init the screen
    screen = Screen()
    screen.clear()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose between red/orange/yellow/green/blue: ")


    # init the turtles in the start position
    y_position = -100
    turtles = []
    for colour in colours:
        t = Turtle(shape="turtle")
        t.color(colour)
        t.penup()
        t.goto(x=-240, y=y_position)
        y_position += 50
        turtles.append(t)

    return (turtles, screen, user_bet)

def start_race(turtles, screen, user_bet):
    """
    Function that makes the turtles race each other
    """
    race_finished = False

    # loop that makes the turtles race each other
    while not race_finished:
        for turtle in turtles:
            # move the turtle
            rand_movement = random.randint(0, 30)
            turtle.forward(rand_movement)
            
            # check if the turtle has won the race
            if turtle.xcor() > 220:
                winning_colour = turtle.pencolor()
                race_finished = True
        

    # announcing the winning turtle and letting the user know
    # if their bet was correct or not
    if winning_colour == user_bet:
        print(f"You've won! The winner is the {winning_colour} turtle.")
    else:
        print(f"You've lost. The winner is the {winning_colour} turtle.")

    # screen.exitonclick()


# loop that allows the user to rerun the game as many times as they want
play_game = True
while play_game:
    init_stuff = init_turtles()
    turtles = init_stuff[0]
    screen_to_use = init_stuff[1]
    user_bet = init_stuff[2]


    start_race(turtles, screen_to_use, user_bet)

    # user input to see if they want to play again
    user_choice = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if user_choice == "n":
        play_game = False
        print("Bye bye! See you next time.")
