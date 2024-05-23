import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        """
        Constructor for the Food class
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # 20 units * 0.5 (makes it smaller)
        self.color("red")
        self.speed("fastest")
        self.change_pos()


    def change_pos(self):
        """
        Method that changes the food's position on screen
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        self.goto(random_x, random_y)        