# imports 
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """
        Constructor for the Scoreboard class
        """
        super().__init__()
        self.score = 0
        self.color("limegreen")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.display_score()

    def increase_score(self):
        """
        Method that increases the user's score
        """
        self.score += 1
        self.clear()
        self.display_score()
    
    def display_score(self):
        """
        Method that displays the user's score 
        """
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        

    def game_over(self):
        """
        Method writes "GAME OVER" if the user lost the game 
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))