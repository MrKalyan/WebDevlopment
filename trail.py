import turtle
#from turtle import clock
from turtle import Screen, Turtle
wn = turtle.Screen()
wn.bgcolor('black')
s = Screen()
#win = turtle.s
t = Turtle()
wn.setup(width=400, height=400)
red = turtle.Turtle() # Assigning "Red" as name of the turtle
pen = red
def curve(): # Method to draw curve
    for i in range(200): # To draw the curve step by step
        red.right(1)
        red.forward(1)

def heart():  # Method to draw full Heart
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve() # Left Curve
    red.left(120)
    curve() # Right Curve
    red.forward(112)
    red.end_fill()
def txt():

	# Move turtle to air
	pen.up()

	# Move turtle to a given position
	pen.setpos(-68, 95)

	# Move the turtle to the ground
	pen.down()

	# Set the text color to lightgreen
	pen.color('lightgreen')

	# Write the specified text in
	# specified font style and size
	pen.write("Love You ", font=(
	"Verdana", 12, "bold"))

heart()
txt()
red.ht() # Hiding Turtle
turtle.done()
