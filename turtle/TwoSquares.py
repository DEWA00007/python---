# Making 2 different squares

import turtle
t = turtle.Turtle()
t.color("green")
for i in range(4):
    t.forward(100)
    t.right(90)
t.penup()

t.goto(0,120)
t.pendown()
t.color("blue")
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()