show_process = False
iterations = 333


import turtle
import math
if not show_process:
    turtle.tracer(0)


t = turtle.Turtle()
t.lt(180)

for a in range(1, iterations):

    for i in range(4):
        t.pencolor("blue")
        t.forward(a * math.pi)
        t.right(90)
        t.left(math.pi * i)

    for i in range(4):
        t.pencolor("red")
        t.forward(a * math.pi)
        t.right(90)
        t.left(-math.pi)


turtle.update()
turtle.exitonclick()
