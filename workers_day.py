# Import Package(s)
import turtle as t

# Set Screen Size
t.setup(1000,1000)
t.title("HAPPY INTERNATIONAL WORKERS DAY 👮🏽🎖")

# Create a function that does rectangle shape
def rectangle(horizontal, vertical, color):
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
t.bgcolor("#ecf1ff") # ecf5ff ecf1ff
# t.bgcolor("#b8e2f2")
# t.bgcolor('Dodger blue')

# Drawing The Feet of Our Worker
t.goto(-100,-150)
rectangle(50,20, 'blue')
t.goto(-30, -150)
rectangle(50,20, 'blue')

# Drawing The Legs of Our Worker
t.goto(-25, -50)
rectangle(15, 100, 'grey') # Left Leg
t.goto(-55, -50)
rectangle(-15, 100, 'grey') # Right Leg

# Drawing The Body of Our Worker
t.goto(-90, 100)
rectangle(100, 150, 'red')

# Drawing The Hands of Our Worker
t.goto(-150, 70)
rectangle(60, 15, 'grey') # Upper Right Hand
t.goto(-150, 110)
rectangle(15, 40, 'grey') # Lower Right Hand

t.goto(10, 70)
rectangle(60, 15, 'grey') # Upper Left Hand
t.goto(55, 110)
rectangle(15, 40, 'grey') # Lower Left Hand

# Drawing The Neck of Our Worker
t.goto(-50, 120)
rectangle(15, 20, 'grey')

# Drawing The Head of Our Worker
t.goto(-85, 170)
rectangle(80, 50, 'red')

# Drawing The Eyes of Our Worker
t.goto(-60, 160)
rectangle(30, 10, 'white') # The white part of the eyes
t.goto(-55, 155)
rectangle(5, 5, 'black') # The black part of the eyes (The Right Pupil)
t.goto(-40, 155)
rectangle(5, 5, 'black') # The black part of the eyes (The Left Pupil)

# Drawing The Mouth of Our Worker
t.goto(-65, 135)
rectangle(40, 5, 'black')

t.hideturtle() # Hide The Turtle Pointer

t.goto(-150, 220)
t.pendown()
t.color("#3e8dc0") # Set Pen Color
t.speed(0.5)
t.write("Happy Workers Day!", \
         font=("Courier", 20, 'normal', 'bold'))
t.penup()
t.goto(-340, 200)
t.pendown()
t.color('Dodger blue')
t.speed(0.5)
t.write("'Today we celebrate your hard work & immense contribution to society'", \
         font=("Courier", 15, 'italic'))

t.hideturtle() # Hide The Turtle Pointer
