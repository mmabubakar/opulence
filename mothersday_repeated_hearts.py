# Import Packages
import turtle as t
import random
from itertools import cycle # This is a the statement that imports the cycle function

t.setup(1000,1000)

# This creates the cycle of colors in the list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# Define a function that draws more hearts

def draw_heart():
    # t.pencolor(next(colors)) # This statement uses the next color in the cycle
    t.pencolor(random.choice(colors))
    t.pensize(5)
    t.left(50)
    t.forward(105)
    t.circle(40, 200)
    t.right(140)
    t.circle(40, 200)
    t.forward(105)
    draw_heart()


# Set Background, Speed and Size
t.bgcolor('black')
t.speed('fast')
t.pensize(4)
draw_heart()
