# imports
from turtle import Turtle
STARTING_BODY_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

class Snake:
    def __init__(self):
        """
        Constructor for the snake object
        """
        self.body = []
        self.create_snake()
    

    def create_snake(self):
        """
        Function that creates the snake object (seen by the user)
        """
        for body_part_position in STARTING_BODY_POS:
            new_snake_part = Turtle("square")
            new_snake_part.penup()
            new_snake_part.color("white")
            new_snake_part.goto(body_part_position)
            self.body.append(new_snake_part)
    

    def move(self):
        """
        Function that makes the snake move forward
        """
        # this loop makes the body_pieces follow the head
        for body_piece_idx in range(len(self.body) - 1, 0, -1):
            # get the x/y coords of the piece in front
            new_x = self.body[body_piece_idx - 1].xcor()
            new_y = self.body[body_piece_idx - 1].ycor()

            # move the curr piece to the other piece's pos
            self.body[body_piece_idx].goto(new_x, new_y)

        # move the snake's head
        self.body[0].forward(MOVE_DIST)