# Creating my own intials using turtle.
# 09/24/18
# CTI-110 P4T2_Intials
# Reginald Richardson
#

import turtle

# Set up the window attributes
wn = turtle.Screen()             
wn.title("R and R Intitals")
wn.bgcolor("lightblue")

# Create first intial
first_intial = turtle.Turtle()
first_intial.pensize(4)
first_intial.color('Red')
# Create second intial
second_intial = turtle.Turtle()
second_intial.pensize(4)
second_intial.color('Yellow')

#First intial attributes
first_intial.left(90)
first_intial.forward(200)             
first_intial.right(90)
first_intial.forward(100)
first_intial.right(45)
first_intial.forward(45)
first_intial.right(90)
first_intial.forward(90)
first_intial.right(45)
first_intial.forward(65)
first_intial.left(135)
first_intial.forward(150)



#Second intial attributes
second_intial.penup()
second_intial.right(1)
second_intial.forward(135)
second_intial.pendown()
second_intial.left(90)
second_intial.forward(200)             
second_intial.right(90)
second_intial.forward(100)
second_intial.right(45)
second_intial.forward(45)
second_intial.right(90)
second_intial.forward(90)
second_intial.right(45)
second_intial.forward(65)
second_intial.left(135)
second_intial.forward(150)




