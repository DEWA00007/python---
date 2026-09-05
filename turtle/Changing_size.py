import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue"]

size = 200

for i in range(20):

    t.color(colors[i % 2])

    for j in range(4):
        t.forward(size)
        t.right(90)

    size = size - 10
    t.right(18)

turtle.done()
