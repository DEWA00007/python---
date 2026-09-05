import turtle

t = turtle.Turtle()
turtle.tracer(0)  # Direct shows result 

colors = ["red", "blue"]

for i in range(100):

    t.color(colors[i % 2])

    for j in range(4):
        t.forward(100)
        t.right(90)

    t.right(3.6)

turtle.update()  # for that direct showing result
turtle.done()