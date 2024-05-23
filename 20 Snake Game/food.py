import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        """
        Constructor for the Food class
        """
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # 20 units * 0.5 (makes it smaller)
        self.color("green")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)         