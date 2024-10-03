import turtle
import numpy as np

# Setup
turtle.speed(100)
turtle.bgcolor("white")
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()

def subdivide_line_plus(length, level):
    if level == 0:
        # Base case
        turtle.forward(length)
    else:
        length /= np.sqrt(7)
        turtle.left(79.1)
        subdivide_line_minus(length, level - 1)
        turtle.right(60.0)
        subdivide_line_plus(length, level - 1)
        subdivide_line_plus(length, level - 1)
        turtle.right(120.0)
        subdivide_line_plus(length, level - 1)
        turtle.right(60.0)
        subdivide_line_minus(length, level - 1)
        turtle.left(120.0)
        subdivide_line_minus(length, level - 1)
        turtle.left(60.0)
        subdivide_line_plus(length, level - 1)
        turtle.right(19.1)

def subdivide_line_minus(length, level):
    if level == 0:
        # Base case
        turtle.forward(length)
    else:
        length /= np.sqrt(7)
        turtle.left(19.1)
        subdivide_line_minus(length, level - 1)
        turtle.right(60.0)
        subdivide_line_plus(length, level - 1)
        turtle.right(120.0)
        subdivide_line_plus(length, level - 1)
        turtle.left(60.0)
        subdivide_line_minus(length, level - 1)
        turtle.left(120.0)
        subdivide_line_minus(length, level - 1)
        subdivide_line_minus(length, level - 1)
        turtle.left(60.0)
        subdivide_line_plus(length, level - 1)
        turtle.right(79.1)


initial_length = 400.0
colors = ["red", "blue", "green", "purple"]
init_depth = 0

for depth, color in enumerate(colors):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    subdivide_line_plus(initial_length, depth + init_depth)

turtle.done()