# Import Packages
import turtle as t
from itertools import cycle # This is a the statement that imports the cycle function

t.setup(1000,1000)

# This creates the cycle of colors in the list
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# Define a function that draws more circles
def draw_circle(size, angle, shift):
    t.pencolor(next(colors)) # This statement uses the next color in the cycle
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

# Set Background, Speed and Size
t.bgcolor('black')
t.speed('fast')
t.pensize(4)
draw_circle(30, 0, 1)

