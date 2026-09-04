# t.penup()     stop drawing
# t.pendown()   start drawing again

import turtle
t = turtle.Turtle()

t.forward(100)  # draws line
t.penup()       # stop drawing
 
t.goto(50,70)   # Change the position
t.pendown()       # Draw again

t.forward(100)     # draw 

turtle.done()