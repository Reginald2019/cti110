
# Creating a square and triangle 
# 09/24/18
# CTI-110 P4T1_Turtle Graphics
# Reginald Richardson
#

import turtle
# Set up the window attributes
wn = turtle.Screen()             
wn.title("Square and Rectangle")

# Create Triangle
Triangle = turtle.Turtle()

# Triangle attributes
Triangle.left(90)
Triangle.forward(80)             
Triangle.left(120)
Triangle.forward(80)
Triangle.left(120)
Triangle.forward(80)
Triangle.left(120)

 # Create Square
Square = turtle.Turtle()

 # Square attributes
Square.forward(50)               
Square.left(90)
Square.forward(50)
Square.left(90)
Square.forward(50)
Square.left(90)
Square.forward(50)
Square.left(90)

# End Command
turtle.exitonclick()


