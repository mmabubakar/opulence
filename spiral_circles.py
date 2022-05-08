# Import Packages
import turtle as t
import random
from itertools import cycle # This is a the statement that imports the cycle function

t.setup(1000,1000)

# This creates the cycle of colors in the list
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
color_list = ['#a6f79b', '#a80e03', '#FFDAB9', '#D8BFD8',\
              '#8A2BE2', '#E0FFFF', '#5F9EA0', '#f4668c',\
              '#181921', '#6b2c65', '#141414', '#c6c6c6']

"""
# Define a function that draws more circles
def draw_circle(size, angle, shift):
    t.bgcolor(random.choice(color_list)) # Selects random color in the color list for background
    t.pencolor(next(colors)) # This statement uses the next color in the cycle
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

"""

# Draws more circles with new patterns (s= +10, a= +10, sh= +1)
def draw_circle(size, angle, shift):
    t.bgcolor(random.choice(color_list)) # Selects random color in the color list for background
    t.pencolor(next(colors)) # This statement uses the next color in the cycle
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 10, angle + 10, shift + 1)

"""
# Draws more circles with new patterns (s= +5, a= -20, sh= -10)
def draw_circle(size, angle, shift):
    t.bgcolor(random.choice(color_list)) # Selects random color in the color list for background
    t.pencolor(next(colors)) # This statement uses the next color in the cycle
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle - 20, shift + 1)
"""

# Set Background, Speed and Size
# t.bgcolor('black') # with a fixed background color
t.speed('fast')
t.pensize(4)
draw_circle(30, 0, 1)

