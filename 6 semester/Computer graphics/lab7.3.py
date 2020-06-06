show_process = False
iterations = 7


import turtle
import random
if not show_process:
    turtle.tracer(0)


def tree(t, depth, maxdepth):
    if depth > maxdepth:
        return
    else:
        for i in range(2):
            rand = random.randrange(-30, 30)
            t.left(rand)
            t.forward(50*(0.8)**depth)
            anotherTurtle = t.clone()
            tree(anotherTurtle, depth+1, maxdepth)
        return

t = turtle.Turtle()
t.penup()
t.goto(0, -200)
t.left(90)
t.pendown()
t.hideturtle()

tree(t, 0, iterations)


turtle.update()
turtle.exitonclick()
