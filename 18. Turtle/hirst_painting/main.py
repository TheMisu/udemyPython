import colorgram
import random
import turtle as turtle_module

# # extract the colour palette from the hirst spots painting
# colour_palette = colorgram.extract("spots.jpg", 30)


# # changing the colours from hsl to rgb
# rgb_colours = []
# for colour in colour_palette:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_colour = (r, g, b)
#     rgb_colours.append(rgb_colour)

# print(rgb_colours)


colour_list = [(253, 251, 247), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]


# init turtle
turtle_module.colormode(255)
turtle_module.bgcolor("black")
t = turtle_module.Turtle()
t.speed(0)


# painting the picture
def paint_hirst_spots(rows, dots_per_row):
    """
    Function that draws a Hirst spot painting based on the 
    rows and number of dots per row chosen by the user
    """
    # set turtle's starting point
    t.penup()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)
    t.pendown()
    
    # setting the num of total dots
    total_dots = rows * dots_per_row


    # for loop that creats the painting
    for dot_count in range(1, total_dots + 1):
        # draw a dot and move 50
        t.dot(20, random.choice(colour_list))
        t.penup()
        t.forward(50)


        # if we drew one row, turn around and repeat
        if dot_count % dots_per_row == 0:
            # make the turtle go left
            if t.heading() == 0:
                t.setheading(90)
                t.forward(50)
                t.setheading(180)
                t.forward(50)
            # or make the turtle go right
            else:
                t.setheading(90)
                t.forward(50)
                t.setheading(0)
                t.forward(50)

        t.pendown()


# run the paint function
paint_hirst_spots(10, 10)

# making the screen exit on click 
screen = turtle_module.Screen()
screen.exitonclick()