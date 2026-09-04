import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("#071A2B")

# Feather stem
t.pensize(6)
t.color("#4CAF50")
t.goto(0, -300)
t.goto(0, 250)

# Feather outer shape
t.penup()
t.goto(0, 250)
t.pendown()
t.color("#168AAD")
t.pensize(3)

t.begin_fill()
t.setheading(110)

for i in range(80):
    t.forward(3)
    t.left(1)

for i in range(80):
    t.forward(3)
    t.left(1)

t.end_fill()

# Peacock eye
t.penup()
t.goto(0, 150)
t.pendown()

# Outer blue circle
t.color("#0066FF")
t.begin_fill()
t.circle(75)
t.end_fill()

# Green circle
t.penup()
t.goto(0, 165)
t.pendown()
t.color("#00AA55")
t.begin_fill()
t.circle(55)
t.end_fill()

# Gold/yellow circle
t.penup()
t.goto(0, 180)
t.pendown()
t.color("#FFD700")
t.begin_fill()
t.circle(40)
t.end_fill()

# Dark center
t.penup()
t.goto(0, 190)
t.pendown()
t.color("#003366")
t.begin_fill()
t.circle(28)
t.end_fill()

# Highlight
t.penup()
t.goto(-10, 220)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(7)
t.end_fill()

t.hideturtle()
turtle.done()
