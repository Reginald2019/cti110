# Create a 5- pointed shape using nested loop.
# 09/26/18
# CTI-110 P4HW3 - Tuition Increase
# Reginald Richardson

#Pentagon Parameters
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title('Pentagon')

# 5- point Pentagon
pentagon = turtle.Turtle()
pentagon.color("cyan")

# Fill (not required, but helps if for draw in range does not create a point) 
pentagon.begin_fill()

#Loop Controls
for draw in range(4):
    pentagon.left(90)
    pentagon.forward(140)
    pentagon.left(-130)
    # Makes open triangles such as '^', '<', and '>'
    for draw in range(3):
        pentagon.left(-130)

pentagon.end_fill()
wn.mainloop()

#___________________________________Psuedocode
# Pentagonal parameters
# optional fill
# Loop controls (nested 5-point)
# open triangle loop inside pentagon loop)
