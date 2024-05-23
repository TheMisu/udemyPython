# imports
from turtle import Turtle

# few useful constants
STARTING_BODY_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270 
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """
        Constructor for the snake object
        """
        self.body = []
        self.create_snake()
        self.head = self.body[0]    

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


    def up(self):
        """
        FUnction that turns the snake upwards
        """
        # only allow the snake to turn up if it is not moving downwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 

    def down(self):
        """
        FUnction that turns the snake downwards
        """
        # only allow the snake to turn if it is not moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        """
        FUnction that turns the snake to the left
        """
        # only allow the snake to turn if it is not moving to the right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        FUnction that turns the snake to the right
        """
        # only allow the snake to turn if it is not moving to the left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)