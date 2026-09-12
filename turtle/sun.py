import turtle

t = turtle.Turtle()
t.speed(0)
t.color("orange")

for i in range(36):
    t.forward(100)
    t.backward(100)
    t.right(10)

turtle.done()
