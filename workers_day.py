# Import Package(s)
import turtle as t

# Create a function that does rectangle shape
def rectangle(horizontal, vertical, color)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    # This Loops through twice to make a rectangle shape
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

# Setting Turtle Speed and Background Color
t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

# Drawing The Feet of Our Worker
t.goto(-100,-150)
rectangle(50,20, 'blue')
t.goto(-30, -150)
rectangle(50,20, 'blue')

# Drawing The Legs of Our Worker
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')


